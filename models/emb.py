from sqlalchemy import Column, String, Integer, BigInteger
from sqlalchemy.orm import relationship
from base import Base
from models.emb_product import EmbProduct
class Emb(Base):
    __tablename__ = 'Emb'
    id = Column(BigInteger, primary_key=True) 
    name = Column(String, nullable=False)
    products = relationship('Product', secondary='EmbProduct', back_populates='emb_codes')