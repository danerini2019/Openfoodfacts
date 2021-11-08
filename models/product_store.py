from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class ProductStore(Base):
    __tablename__ = 'ProductStore'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    storeId = Column(BigInteger, ForeignKey('Store.id'))
    