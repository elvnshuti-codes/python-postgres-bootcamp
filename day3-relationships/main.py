from fastapi import HTTPException # For raising 404 errors when item not found
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List # Used for response_model List[schemas.User]
import models, schemas, database

# Create all tables in the database when the app starts
# This only runs if tables don't exist yet
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI() # Main FastAPI application instance

# Dependency function: Creates a new DB session for each request
# and ensures it's closed after the request is done
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ================= USER ENDPOINTS =================

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    """Create a new user and save it to the database"""
    # 1. Take the name from request body and create a new User object
    db_user = models.User(name=user.name)
    # 2. Add it to the database session
    db.add(db_user)
    # 3. Save changes to DB
    db.commit()
    # 4. Refresh to get the new ID and created_at from DB
    db.refresh(db_user)
    # 5. Return the new user to the client
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    """Get all users from the database. 
    Because of 'todos: List[Todo]' in schema, it will also show their todos"""
    return db.query(models.User).all()

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    """Update a user's name by their ID"""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = name
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user by ID. Cascade will also delete their todos"""
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted"}
    return {"error": "User not found"}


# ================= TODO ENDPOINTS =================

@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoBase, db: Session = Depends(get_db)):
    """Create a new todo and assign it to a user_id"""
    # **todo.dict() takes task, completed, user_id from request and puts it in Todo()
    db_todo = models.Todo(**todo.dict()) 
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/")
def read_todos(user_id: int = None, db: Session = Depends(get_db)):
    """Get all todos. If user_id is provided, return todos for that user only"""
    if user_id:
        todos = db.query(models.Todo).filter(models.Todo.user_id == user_id).all()
    else:
        todos = db.query(models.Todo).all()
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, completed: bool, db: Session = Depends(get_db)):
    """Update a todo's completed status by ID"""
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.completed = completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo by ID"""
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}