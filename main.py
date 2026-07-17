from fastapi import FastAPI
from dotenv import load_dotenv
import os
import psycopg2
# Load variables from .env file 
load_dotenv()

app = FastAPI()
# Home route - just to check if server is running 
@app.get("/")
def read_root():
    return {"message": "Bootcamp API is running"}
# Test database connection route 
@app.get("/test-db")
def test_db():
    try:
# Connect to database using URL from ,env        
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"db_status": "Connected to bootcampdb ✅"}
    except Exception as e:
        return {"db_status": "Failed", "error": str(e)}