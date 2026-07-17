from fastapi import FastAPI  # Import FastAPI class to create our app

app = FastAPI()  # Create the FastAPI application instance

# This is our "database" for Day 1. Just a Python list in memory.
# It will reset every time we restart the server. Day 2 we use Postgres.
todos = []

@app.get("/")  # When someone visits http://127.0.0.1:8000/
def read_root():
    return {"message": "Hello FastAPI"}  # Return a simple test message

@app.get("/todos")  # GET request to see all todos
def get_todos():
    return todos  # Return the whole todos list

@app.post("/todos")  # POST request to create a new todo
def create_todo(todo: dict):  # `todo` will be the JSON we send from /docs
    todos.append(todo)  # Add the new todo to our list
    return todo  # Send back what we just created