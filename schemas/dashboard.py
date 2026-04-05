from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from models.base import Base


class Dashboard(Base):
    __tablename__ = "dashboard"
    id = Column(Integer, primary_key=True)
    name = Column(String)