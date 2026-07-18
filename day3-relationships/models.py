from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# User model: Represents the 'users' table in the database
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True) # Unique ID for each user
    name = Column(String, index=True) # User's name

    # Relationship: One user can have many todos
    # cascade="all, delete-orphan" means if user is deleted, delete all their todos too
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")

# Todo model: Represents the 'todos' table in the database
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True) # Unique ID for each todo
    task = Column(String, index=True) # The task description
    completed = Column(Boolean, default=False) # Status of the todo
    created_at = Column(DateTime, default=datetime.utcnow) # NEW COLUMN: Auto timestamp
    user_id = Column(Integer, ForeignKey("users.id")) # Foreign key linking to User
    
    # Relationship: Each todo belongs to one user
    owner = relationship("User", back_populates="todos")
    

     