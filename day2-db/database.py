from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection URL
# Format: postgresql://username:password@host:port/database_name
# IMPORTANT: Change YOUR_PASSWORD to the password you used for postgres
DATABASE_URL = "postgresql://postgres:password@localhost/bootcampdb"

# Create the database engine - this is the connection to Postgres
engine = create_engine(DATABASE_URL)

# SessionLocal is a factory for creating database sessions
# autocommit=False and autoflush=False are best practices for FastAPI
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all SQLAlchemy models will inherit from
Base = declarative_base()