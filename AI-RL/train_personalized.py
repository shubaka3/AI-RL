import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Kết nối DB
engine = create_engine(DATABASE_URL)

# Lấy log user detail
query = """
SELECT UserID, ProductID, Action
FROM UserDetail
"""

df = pd.read_sql(query, engine)

# Chỉ tính số lần 'purchase'
df_purchase = df[df['Action'] == 'purchase']

# Đếm số lần mua mỗi sản phẩm theo user
user_product_score = (
    df_purchase.groupby(['UserID', 'ProductID'])
    .size()
    .reset_index(name='Score')
    .sort_values(['UserID', 'Score'], ascending=[True, False])
)

print(user_product_score.head())

# Ghi vào bảng UserRecommendation
with engine.begin() as conn:
    # Xoá data cũ (tuỳ bạn)
    conn.execute(text("DELETE FROM UserRecommendation"))

    # Insert mới
    for _, row in user_product_score.iterrows():
        conn.execute(
            text("""
                INSERT INTO UserRecommendation (UserID, ProductID, Score)
                VALUES (:user_id, :product_id, :score)
            """),
            {
                "user_id": int(row['UserID']),
                "product_id": int(row['ProductID']),
                "score": float(row['Score'])
            }
        )

print("✅ Done! Recommendation saved to DB.")
