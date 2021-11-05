from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base
from models.country_product import CountryProduct

class Country(Base):
    __tablename__ = 'Country'
    id = Column(BigInteger, primary_key=True) 
    name_en = Column(String, nullable=False)
    name_fr = Column(String, nullable=True)
    products = relationship('Product', secondary='CountryProduct', back_populates='countries')