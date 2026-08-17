"""
Main Application

Entry point for the AI Interview System.

Responsibilities
----------------
1. Initialize FastAPI
2. Configure CORS
3. Register API Routers
4. Initialize Database
5. Startup Events
6. Root Endpoint

Author: Akksai Prathaan
Project: AI Interview System
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import Base, engine

from app.api.resume import router as resume_router
from app.api.interview import router as interview_router
from app.api.health import router as health_router


# ---------------------------------------------------------
# Database Initialization
# ---------------------------------------------------------

Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------
# Application Lifespan
# ---------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("=" * 70)
    print("AI Interview System Started")
    print("=" * 70)

    yield

    print("=" * 70)
    print("AI Interview System Stopped")
    print("=" * 70)


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(

    title="AI Interview System",

    description="""
AI-powered interview platform using

• Resume Parsing

• Skill Extraction

• Retrieval-Augmented Generation (RAG)

• OpenAI LLM

• Interview Evaluation

• SQLite Database

• FastAPI Backend
""",

    version="1.0.0",

    lifespan=lifespan,

    docs_url="/docs",

    redoc_url="/redoc",

)


# ---------------------------------------------------------
# CORS Configuration
# ---------------------------------------------------------

origins = [

    "http://localhost:3000",

    "http://127.0.0.1:3000",

    "http://localhost:5173",

    "http://127.0.0.1:5173",

]

app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


# ---------------------------------------------------------
# Register Routers
# ---------------------------------------------------------

app.include_router(resume_router)

app.include_router(interview_router)

app.include_router(health_router)


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")

def root():

    return {

        "application": "AI Interview System",

        "author": "Akksai Prathaan",

        "version": "1.0.0",

        "status": "Running",

        "documentation": "/docs",

    }


# ---------------------------------------------------------
# Application Info
# ---------------------------------------------------------

@app.get("/info")

def info():

    return {

        "project": "AI Interview System",

        "backend": "FastAPI",

        "database": "SQLite",

        "vector_database": "ChromaDB",

        "llm": "OpenAI",

        "rag": "Enabled",

        "resume_parser": "Enabled",

        "skill_extraction": "Enabled",

        "question_generation": "Enabled",

        "evaluation": "Enabled",

        "author": "Akksai Prathaan",

    }


# ---------------------------------------------------------
# Version Endpoint
# ---------------------------------------------------------

@app.get("/version")

def version():

    return {

        "version": "1.0.0"

    }