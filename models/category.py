from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Category(Base):
    __tablename__ = 'Category'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='CategoryProduct', back_populates='categories')