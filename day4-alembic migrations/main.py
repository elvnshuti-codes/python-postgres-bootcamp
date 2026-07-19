# main.py
# This is the main entry point for our FastAPI app with full CRUD using Alembic

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Import our own modules
from database import get_db          # Dependency that gives us a DB session
from models import User              # SQLAlchemy table model
import schemas                       # Pydantic validation models

# 1. Create the FastAPI app instance
app = FastAPI(title="Day4 Alembic Bootcamp")

# 2. POST ROUTE: Create a new user
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user in the database.
    
    Args:
        user: Data from request body, validated by UserCreate schema
        db: Database session, automatically provided by Depends(get_db)
    
    Returns:
        The newly created user as UserResponse
    """
    # 1. Check if email already exists to avoid duplicates
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Create new SQLAlchemy User object
    new_user = User(email=user.email, name=user.name)
    
    # 3. Add to session, commit to DB, refresh to get the auto-generated id
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# 3. GET ROUTE: Get all users
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    """
    Fetches all users from the database.
    
    Args:
        db: Database session, automatically provided by Depends(get_db)
    
    Returns:
        A list of all users
    """
    users = db.query(User).all()  # SELECT * FROM users
    return users

# 4. GET ROUTE: Get one user by ID
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Fetches a single user by their ID.
    
    Args:
        user_id: The ID of the user to fetch
        db: Database session
    
    Returns:
        A single user
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 5. PUT ROUTE: Update a user
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user_update: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Updates an existing user's name and email.
    
    Args:
        user_id: The ID of the user to update
        user_update: New data from request body, validated by UserCreate schema
        db: Database session
    
    Returns:
        The updated user
    """
    # 1. Find the user in the DB
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 2. Check if new email conflicts with another user
    existing_user = db.query(User).filter(User.email == user_update.email, User.id != user_id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already taken")

    # 3. Update fields and save
    user.email = user_update.email
    user.name = user_update.name
    db.commit()
    db.refresh(user)
    
    return user

# 6. DELETE ROUTE: Delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Deletes a user from the database.
    
    Args:
        user_id: The ID of the user to delete
        db: Database session
    
    Returns:
        Success message
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}