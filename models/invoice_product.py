import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Double, BigInteger, DateTime
from sqlalchemy.orm import relationship


class InvoiceProduct(BaseModel):
    __tablename__ = "invoice_product"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("user.id"))
    product_id = Column(BigInteger, ForeignKey("product.id"))
    invoice_id = Column(BigInteger, ForeignKey("invoice.id"))
    qty=Column(Double,nullable=False)
    sale_price = Column(Double,nullable=False)
    product = relationship("Product", back_populates="products")
    invoices= relationship("Invoice", back_populates="invoices")
    products = relationship("Product", back_populates="products")
    users = relationship("User", back_populates="users")
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
