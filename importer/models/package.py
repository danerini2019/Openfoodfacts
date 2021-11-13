from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base

class Package(Base):
    __tablename__ = 'Package'
    id = Column(BigInteger, primary_key=True) 
    name_en = Column(String, nullable=False)
    name_fr = Column(String, nullable=False)
    slug = Column(String, nullable=True)
    description = Column(String, nullable=True)
    products = relationship('Product', secondary='PackageProduct', back_populates='packages')