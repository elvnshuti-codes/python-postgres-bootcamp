# fastapi-bootcamp

A simple Todo API built with **FastAPI** and **PostgreSQL** as my first AIP full stuck project named my coding bootcamp.  
This project covers CRUD operations, database connection, Pydantic validation, and SQLAlchemy models.

## Features
- **FastAPI**: Modern, fast web framework for building APIs
- **PostgreSQL**: Relational database to store todos
- **SQLAlchemy**: ORM for database interactions
- **Pydantic**: Request/Response validation
- **CRUD Endpoints**: Create and Read todos

## Tech Stack
- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Uvicorn

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/elvnshuti-codes/fastapi-bootcamp.git
cd fastapi-bootcamp2. Create virtual environmentbashpython -m venv .venv
source .venv/bin/activate 
 # On Windows: .venv\Scripts\activate3. Install dependenciesbashpip install fastapi uvicorn sqlalchemy psycopg2-binary4. Setup PostgreSQLCreate a database called bootcampdb and update the password in database.py:pythonDATABASE_URL = "postgresql://postgres:yourpassword@localhost/bootcampdb"5. Run the serverbashuvicorn main:app --reload6. Test the APIOpen your browser: http://127.0.0.1:8000/docsThis opens the automatic FastAPI Swagger docs where you can test endpoints.📌 API EndpointsMethodEndpointDescriptionGET/todosGet all todosPOST/todosCreate a new todoExample POST request body:json{
  "title": "Learn FastAPI",
  "description": "Complete the bootcamp project"
}📂 Project Structurejavascriptfastapi-bootcamp/
├── main.py         # FastAPI routes and app logic
├── models.py       # SQLAlchemy database models
├── schemas.py      # Pydantic request/response models
├── database.py     # Database connection and session
├── .gitignore      # Files to ignore in git
└── README.md       # Project documentation🎯 Next StepsAdd UPDATE and DELETE endpointsAdd authentication with JWTDeploy to Render or RailwayBuilt during FastAPI Bootcamp 2026javascript
---

### **PUSH IT**
```bash
git add README.md
git commit -m "Added README with setup and API documentation"
git pushNow when someone opens your GitHub repo they’ll see exactly how to use it.
YESS LET'S MAKE IT 1-COMMAND INSTALL 

6. requirements.txtCreate a new file called requirements.txt and paste this:javascriptfastapi==0.115.0
uvicorn[standard]==0.30.6
sqlalchemy==2.0.35
psycopg2-binary==2.9.9
pydantic==2.9.2What each does:fastapi: The web frameworkuvicorn[standard]: The server to run FastAPIsqlalchemy: To talk to Postgrespsycopg2-binary: Postgres driver for Pythonpydantic: For data validation in FastAPIUPDATE YOUR README SETUP SECTIONChange step 3 in README to this:markdown### 3. Install dependencies
```bash
pip install -r requirements.txtjavascript
### **PUSH EVERYTHING**
```bash
git add requirements.txt README.md
git commit -m "Added requirements.txt for easy setup"
git pushNOW YOUR FULL BOOTCAMP REPO HAS:main.py - API routesmodels.py - Database tabledatabase.py - DB connectionschemas.py - Data validation.gitignore - Clean reporequirements.txt - Easy installREADME.md - DocumentationYou can literally send this GitHub link to anyone and they can run it in 5 mins.Test it: pip install -r requirements.txt then uvicorn main:app --reload
