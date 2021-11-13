from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class BrandProduct(Base):
    __tablename__ = 'BrandProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    brandId = Column(BigInteger, ForeignKey('Brand.id'))
    