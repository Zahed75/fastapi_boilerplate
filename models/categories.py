import datetime
from pydantic import BaseModel
from sqlalchemy import BigInteger, Column, TIMESTAMP, String, ForeignKey


class Category(BaseModel):
    __tablename__ = 'categories'
    id = Column(BigInteger, primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    user_id=Column(BigInteger,ForeignKey('users.id'),nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda: datetime.now(datetime.timezone.utc),
                        onupdate=datetime.timezone.utc)

