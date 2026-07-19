# schemas.py
# Pydantic models are used to validate data coming IN and going OUT of the API

from pydantic import BaseModel

# 1. Schema for creating a user
# This validates the data the client sends to us in POST /users
class UserCreate(BaseModel):
    email: str  # required field
    name: str   # required field

    class Config:
        # Allows Pydantic to read data from SQLAlchemy models directly
        from_attributes = True

# 2. Schema for returning a user
# This defines the shape of data we send back to the client
class UserResponse(BaseModel):
    id: int     # Database auto-generated ID
    email: str
    name: str

    class Config:
        from_attributes = True