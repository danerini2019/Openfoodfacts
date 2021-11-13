from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class AdditiveProduct(Base):
    __tablename__ = 'AdditiveProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    additiveId = Column(BigInteger, ForeignKey('Additive.id'))
    