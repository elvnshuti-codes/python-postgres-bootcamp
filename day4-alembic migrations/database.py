# database.py
# This file handles the database connection for your FastAPI app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load variables from .env file so we don't hardcode password
load_dotenv()

# Get DB URL from .env file. If not found, use this default
DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://postgres:password@localhost:5432/day4_db")

# 1. Create the engine: this is the main entry point to the DB
# echo=True will print all SQL to terminal. Set to False later
engine = create_engine(DB_URL, echo=False)

# 2. Create a SessionLocal class: each instance is a DB session
# autocommit=False: we control when to commit
# autoflush=False: we control when to flush changes to DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create a Base class. All our models will inherit from this
# Alembic will look at Base.metadata to find all tables
Base = declarative_base()

# Dependency for FastAPI routes to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()