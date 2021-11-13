from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Brand(Base):
    __tablename__ = 'Brand'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='BrandProduct', back_populates='brands')