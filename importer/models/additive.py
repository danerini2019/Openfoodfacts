from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Additive(Base):
    __tablename__ = 'Additive'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    products = relationship('Product', secondary='AdditiveProduct', back_populates='additives')