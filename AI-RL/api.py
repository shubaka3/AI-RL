#api.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Product, UserDetail
from models import User, Product, UserDetail, UserRecommendation
from fastapi import HTTPException


import pickle

router = APIRouter()



# Load top products lúc khởi động router
with open("global_top_products.pkl", "rb") as f:
    top_products = pickle.load(f)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/products")
def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/userdetails")
def read_userdetails(db: Session = Depends(get_db)):
    return db.query(UserDetail).all()

# ✅ API gợi ý toàn cục
@router.get("/recommend/global")
def recommend_global():
    return {"recommended_product_ids": top_products}


@router.get("/recommend/personalized/{user_id}")
def recommend_personalized(user_id: int, db: Session = Depends(get_db)):
    recs = (
        db.query(UserRecommendation)
        .filter(UserRecommendation.UserID == user_id)
        .order_by(UserRecommendation.Score.desc())
        .all()
    )
    if not recs:
        raise HTTPException(status_code=404, detail="No recommendations found for this user.")
    product_ids = [r.ProductID for r in recs]
    return {"recommended_product_ids": product_ids}
