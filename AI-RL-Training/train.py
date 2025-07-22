import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pickle

# Load env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Kết nối DB
engine = create_engine(DATABASE_URL)

# Lấy log user detail
query = """
SELECT ProductID, Action
FROM UserDetail
"""

df = pd.read_sql(query, engine)

# Chỉ tính số lần 'purchase'
df_purchase = df[df['Action'] == 'purchase']

# Đếm số lần mua mỗi Product
product_popularity = (
    df_purchase.groupby('ProductID')
    .size()
    .reset_index(name='purchase_count')
    .sort_values(by='purchase_count', ascending=False)
)

print(product_popularity)

# Lưu top 10 vào file pickle
top_products = product_popularity.head(10)['ProductID'].tolist()

with open("global_top_products.pkl", "wb") as f:
    pickle.dump(top_products, f)

print(f"Top products saved: {top_products}")
