from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class AllergenProduct(Base):
    __tablename__ = 'AllergenProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    allergenId = Column(BigInteger, ForeignKey('Allergen.id'))
    