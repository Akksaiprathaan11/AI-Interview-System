"""
Resume API

Handles resume upload and candidate registration.

Endpoints
---------
POST /api/resume/upload

Author: Akksai Prathaan
Project: AI Interview System
"""

import os
import shutil
from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.services.interview_service import InterviewService

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)

service = InterviewService()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# Upload Resume
# ---------------------------------------------------------

@router.post("/upload")
async def upload_resume(

    name: str = Form(...),

    email: str = Form(...),

    role: str = Form(...),

    resume: UploadFile = File(...),

    db: Session = Depends(get_db),

):
    """
    Upload candidate resume.
    """

    # ---------------------------------------------
    # Validate File
    # ---------------------------------------------

    if not resume.filename.endswith(".pdf"):

        raise HTTPException(

            status_code=400,

            detail="Only PDF resumes are supported."

        )

    # ---------------------------------------------
    # Save Resume
    # ---------------------------------------------

    file_path = UPLOAD_DIR / resume.filename

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            resume.file,
            buffer
        )

    # ---------------------------------------------
    # Process Resume
    # ---------------------------------------------

    result = service.upload_resume(

        db=db,

        name=name,

        email=email,

        role=role,

        resume_path=str(file_path),

    )

    return {

        "message": "Resume uploaded successfully.",

        "candidate_id": result["candidate"].id,

        "name": result["candidate"].name,

        "role": result["candidate"].role,

        "skills": result["skills"],

    }


# ---------------------------------------------------------
# Get Candidate
# ---------------------------------------------------------

@router.get("/{candidate_id}")

def get_candidate(

    candidate_id: int,

    db: Session = Depends(get_db),

):

    from app.database import crud

    candidate = crud.get_candidate(

        db,

        candidate_id,

    )

    if candidate is None:

        raise HTTPException(

            status_code=404,

            detail="Candidate not found."

        )

    return candidate


# ---------------------------------------------------------
# Get All Candidates
# ---------------------------------------------------------

@router.get("/")

def get_all_candidates(

    db: Session = Depends(get_db),

):

    from app.database import crud

    return crud.get_all_candidates(db)
