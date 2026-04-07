from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

engine = create_engine(DATABASE_URL,pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)