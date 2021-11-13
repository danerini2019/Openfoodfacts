from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class City(Base):
    __tablename__ = 'City'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    countryId = Column(BigInteger, ForeignKey('Country.id')) 
    # country = relationship('Country', back_populates='cities')