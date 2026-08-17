"""
Health API

Provides application health and status information.

Endpoints
---------
GET /api/health

Author: Akksai Prathaan
Project: AI Interview System
"""

from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import text

from app.database.db import SessionLocal
from app.rag.vector_store import VectorStore

router = APIRouter(
    prefix="/api",
    tags=["Health"]
)


@router.get("/health")
def health_check():
    """
    Application health check.
    """

    # -----------------------------------------
    # Database Health
    # -----------------------------------------

    database_status = "Healthy"

    try:

        db = SessionLocal()

        db.execute(text("SELECT 1"))

        db.close()

    except Exception:

        database_status = "Unavailable"

    # -----------------------------------------
    # ChromaDB Health
    # -----------------------------------------

    vector_db_status = "Healthy"

    total_vectors = 0

    try:

        store = VectorStore()

        total_vectors = store.count_documents()

    except Exception:

        vector_db_status = "Unavailable"

    # -----------------------------------------
    # Overall Response
    # -----------------------------------------

    return {

        "application": "AI Interview System",

        "status": "Running",

        "version": "1.0.0",

        "database": database_status,

        "vector_database": vector_db_status,

        "knowledge_base_vectors": total_vectors,

        "server_time": datetime.utcnow().isoformat(),

    }