from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database_models import Base


# ==========================================
# DATABASE CONFIGURATION
# ==========================================

DATABASE_URL = "sqlite:///./nirvana.db"


# ==========================================
# DATABASE ENGINE
# ==========================================

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# ==========================================
# DATABASE SESSION
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ==========================================
# GET DATABASE SESSION
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# CREATE DATABASE TABLES
# ==========================================

def create_database():

    Base.metadata.create_all(
        bind=engine
    )