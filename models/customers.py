import datetime

from pydantic import BaseModel
from sqlalchemy import BigInteger, Column, String, TIMESTAMP


class Customer(BaseModel):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at=Column(TIMESTAMP,nullable=False,default=lambda:datetime.now(datetime.timezone.utc))

