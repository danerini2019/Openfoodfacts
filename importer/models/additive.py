from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Additive(Base):
    __tablename__ = 'Additive'
    id = Column(BigInteger, primary_key=True) 
    name_en = Column(String, nullable=False)
    name_fr = Column(String, nullable=True)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='AdditiveProduct', back_populates='additives')