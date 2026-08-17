"""
Database Configuration

This module configures the SQLAlchemy engine,
session management, and declarative base
for the AI Interview System.

Author: Akshay
Project: AI Interview System
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# ---------------------------------------------------------
# SQLite Configuration
# ---------------------------------------------------------
# SQLite requires this argument to allow multiple threads.
connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# ---------------------------------------------------------
# SQLAlchemy Engine
# ---------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False
)

# ---------------------------------------------------------
# Session Factory
# ---------------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ---------------------------------------------------------
# Base Class
# ---------------------------------------------------------

Base = declarative_base()

# ---------------------------------------------------------
# Dependency for FastAPI
# ---------------------------------------------------------

def get_db():
    """
    Creates a new database session for every request.

    Usage:
        db = Depends(get_db)
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ---------------------------------------------------------
# Initialize Database
# ---------------------------------------------------------

def init_db():
    """
    Creates all database tables.

    Call this function once when the application starts.
    """

    Base.metadata.create_all(bind=engine)