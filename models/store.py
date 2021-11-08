from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Store(Base):
    __tablename__ = 'Store'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    products = relationship('Product', secondary='ProductStore', back_populates='stores')