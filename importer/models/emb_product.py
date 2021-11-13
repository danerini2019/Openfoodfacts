from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class EmbProduct(Base):
    __tablename__ = 'EmbProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    embId = Column(BigInteger, ForeignKey('Emb.id'))
    