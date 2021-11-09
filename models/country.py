from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base
from models.country_product import CountryProduct
from models.origin_product import OriginProduct
class Country(Base):
    __tablename__ = 'Country'
    id = Column(BigInteger, primary_key=True) 
    name_en = Column(String, nullable=False)
    name_fr = Column(String, nullable=True)
    # cities = relationship('City', back_populates='country')
    products = relationship('Product', secondary='CountryProduct', back_populates='countries')
    products_origins = relationship('Product', secondary='OriginProduct', back_populates='origins')