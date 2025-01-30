from databases import DatabaseURL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from loguru import logger

# DATABASE_URL = "postgresql://postgres:admin@postgres_container:5432/spotify"
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/spotify"

engine = create_engine(DATABASE_URL, future=True)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def init_db() -> bool:
    Base.metadata.create_all(bind=engine)
    logger.info("Database Initialized")
    return True


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
