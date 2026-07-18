from pydantic import BaseModel
from typing import List # Used for "List of Todos"
from datetime import datetime

# SCHEMA 1: What we need to CREATE a Todo
# This is what the client sends to POST /todos/
class TodoBase(BaseModel):
    task: str # Task must be text
    completed: bool = False # Defaults to False if not provided
    user_id: int # NEW: Every todo must be assigned to a user

# SCHEMA 2: What we SEND BACK when someone asks for a Todo
# This includes DB-generated fields like id and created_at
class Todo(TodoBase):
    id: int # When sending back, we also include the ID from DB
    created_at: datetime # Timestamp of when todo was created
    
    class Config:
        from_attributes = True # This lets Pydantic read from SQLAlchemy objects

# SCHEMA 3: What we need to CREATE a User
# This is what the client sends to POST /users/
class UserBase(BaseModel):
    name: str # Name must be text

# SCHEMA 4: What we SEND BACK when someone asks for a User
# This includes the user's ID and their list of todos
class User(UserBase):
    id: int # Include the ID
    todos: List[Todo] = [] # NEW: When we get a user, also show their list of todos
    
    class Config:
        from_attributes = True # Enables ORM mode for SQLAlchemy          