import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Double
from sqlalchemy.orm import relationship


class Invoice(BaseModel):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    total = Column(Double, default=0)
    discount = Column(Double, default=0)
    vat= Column(Double, default=0)
    payable = Column(Double, default=0)
    users=relationship("User", back_populates="invoices")
    customers=relationship("Customer", back_populates="invoices")
    invoice_products = relationship("InvoiceProduct", back_populates="invoices")
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
