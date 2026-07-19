# models.py
# This file defines all your database tables using SQLAlchemy ORM

from sqlalchemy import Column, Integer, String
from database import Base  # Import the Base from database.py

class User(Base):
    # __tablename__ is the actual table name in Postgres
    __tablename__ = "users"

    # id: Primary key, auto-incrementing integer
    id = Column(Integer, primary_key=True, index=True)
    
    # email: String, must be unique. index=True makes searches faster
    email = Column(String, unique=True, index=True, nullable=False)
    
    # name: Regular string column
    name = Column(String, nullable=False)