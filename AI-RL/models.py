# models.py
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "User"

    UserID = Column(Integer, primary_key=True, index=True)
    UserName = Column(String, nullable=False)
    Email = Column(String, unique=True)
    CreatedAt = Column(DateTime, default=datetime.utcnow)

    details = relationship("UserDetail", back_populates="user")


class Product(Base):
    __tablename__ = "Product"

    ProductID = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String, nullable=False)
    Category = Column(String, nullable=False)
    Price = Column(DECIMAL(10,2), nullable=False)
    CreatedAt = Column(DateTime, default=datetime.utcnow)

    details = relationship("UserDetail", back_populates="product")


class UserDetail(Base):
    __tablename__ = "UserDetail"

    DetailID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("User.UserID"), nullable=False)
    ProductID = Column(Integer, ForeignKey("Product.ProductID"), nullable=False)
    Action = Column(String, nullable=False)
    Rating = Column(Integer)
    Timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="details")
    product = relationship("Product", back_populates="details")


class UserRecommendation(Base):
    __tablename__ = "UserRecommendation"

    ID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("User.UserID"), nullable=False)
    ProductID = Column(Integer, ForeignKey("Product.ProductID"), nullable=False)
    Score = Column(Float, nullable=False)
    CreatedAt = Column(DateTime, default=datetime.utcnow)
