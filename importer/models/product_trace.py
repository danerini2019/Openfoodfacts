from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class ProductTrace(Base):
    __tablename__ = 'ProductTrace'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    traceId = Column(BigInteger, ForeignKey('Trace.id'))
    