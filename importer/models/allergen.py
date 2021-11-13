from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Allergen(Base):
    __tablename__ = 'Allergen'
    id = Column(BigInteger, primary_key=True) 
    name_en = Column(String, nullable=False)
    name_fr = Column(String, nullable=True)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='AllergenProduct', back_populates='allergens')