from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Allergen(Base):
    __tablename__ = 'Allergen'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='AllergenProduct', back_populates='allergens')