import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, column, TIMESTAMP
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    password = Column(String, nullable=False)
    otp = Column(String, nullable=False)

    category = relationship("Category", back_populates='users')
    products = relationship("Product", back_populates='users')
    invoices = relationship("InvoiceProduct", back_populates='users')
    customer = relationship("Customer", back_populates='users')
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc),
                        onupdate=datetime.timezone.utc)
