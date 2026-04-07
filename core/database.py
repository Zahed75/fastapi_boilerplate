from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base

DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

_engine = None
SessionLocal = None


def get_engine():
    global _engine, SessionLocal

    if _engine is None:
        _engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)

    return _engine


def get_db():
    session_factory = SessionLocal
    if session_factory is None:
        get_engine()
        session_factory = SessionLocal

    db = session_factory()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=get_engine())
