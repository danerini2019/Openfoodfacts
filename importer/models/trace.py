from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Trace(Base):
    __tablename__ = 'Trace'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    products = relationship('Product', secondary='ProductTrace', back_populates='traces')