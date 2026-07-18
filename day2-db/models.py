from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    """
    SQLAlchemy model for the 'todos' table
    This defines how each Todo is stored in PostgreSQL
    """
    __tablename__ = "todos"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each todo, auto-increments
    title = Column(String, index=True)  # Title of the todo item
    description = Column(String)  # Details about the todo. Can be None

    