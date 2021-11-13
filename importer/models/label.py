from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Label(Base):
    __tablename__ = 'Label'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    products = relationship('Product', secondary='LabelProduct', back_populates='labels')