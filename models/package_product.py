from sqlalchemy import Column, String, BigInteger, ForeignKey
from base import Base

class PackageProduct(Base):
    __tablename__ = 'PackageProduct'
    id = Column(BigInteger, primary_key=True, index=True)
    productId = Column(String, ForeignKey('Product.code'))
    packageId = Column(BigInteger, ForeignKey('Package.id'))
    