from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class LabelProduct(Base):
    __tablename__ = 'LabelProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    LabelId = Column(BigInteger, ForeignKey('Label.id'))
    