from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.db import create_tables
from app.routes import patients

# Load environment variables
load_dotenv()

# FastAPI instance
app = FastAPI()

# Include patient routes
app.include_router(patients.router)

# Startup event to create tables
@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Patient Registration API - Technical interview Santiago Rossi",
        "environment": os.getenv("APP_ENV", "development"),
    }