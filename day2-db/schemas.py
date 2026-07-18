from pydantic import BaseModel

class TodoCreate(BaseModel):
    """
    Pydantic schema for creating a new Todo
    This validates data coming INTO the API
    """
    title: str  # Required field
    description: str | None = None  # Optional field

class TodoResponse(BaseModel):
    """
    Pydantic schema for returning a Todo from the API
    This defines data going OUT of the API
    """
    id: int  # Database ID
    title: str
    description: str | None = None

    class Config:
        # Allows Pydantic to read data from SQLAlchemy models directly
        from_attributes = True        