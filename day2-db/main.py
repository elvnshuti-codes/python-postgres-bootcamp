from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

# Create all database tables on startup
# This runs once and makes the 'todos' table in Postgres if it doesn't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Todo Bootcamp API")

def get_db():
    """
    Dependency that provides a database session for each request
    Opens a session, yields it to the endpoint, then closes it
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    """
    GET /todos
    Fetch all todos from the database
    Returns a list of all Todo items
    """
    return db.query(models.Todo).all()

@app.post("/todos", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """
    POST /todos
    Create a new todo item
    - Takes title and description from request body
    - Saves to database
    - Returns the created todo with its new ID
    """
    db_todo = models.Todo(title=todo.title, description=todo.description)  # Create Todo object
    db.add(db_todo)      # Add to database session
    db.commit()          # Save changes to database
    db.refresh(db_todo)  # Refresh to get the auto-generated ID
    return db_todo