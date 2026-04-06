import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger, Column, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import relationship


class Category(BaseModel):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc),
                        onupdate=datetime.timezone.utc)

    users = relationship("User", back_populates="category")
    invoices = relationship("Invoice", back_populates="invoice")
