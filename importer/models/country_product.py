from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class CountryProduct(Base):
    __tablename__ = 'CountryProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    countryId = Column(BigInteger, ForeignKey('Country.id'))
    