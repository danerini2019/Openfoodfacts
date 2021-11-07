from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class CategoryProduct(Base):
    __tablename__ = 'CategoryProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    categoryId = Column(BigInteger, ForeignKey('Category.id'))
    