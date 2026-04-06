import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Double


class Invoice(BaseModel):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    customer_id = Column(Integer, ForeignKey("customer.id"))
    total = Column(Double, default=0)
    discount = Column(Double, default=0)
    vat= Column(Double, default=0)
    payable = Column(Double, default=0)
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
