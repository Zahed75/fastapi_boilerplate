import datetime

from sqlalchemy import Column, BigInteger, ForeignKey, String, Float, TIMESTAMP
from sqlalchemy.orm import relationship

from models.base import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    category_id = Column(BigInteger, ForeignKey('categories.id'))
    name = Column(String,nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(Float, nullable=False)
    img_url = Column(String, nullable=False)
    users=relationship("User", back_populates="products")
    categories=relationship("Category", back_populates="products")
    invoice_products = relationship("InvoiceProduct", back_populates="products")
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))




