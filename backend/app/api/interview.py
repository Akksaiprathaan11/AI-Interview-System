"""
Interview API

Handles interview workflow.

Endpoints
---------
POST /api/interview/start
GET  /api/interview/questions/{session_id}
POST /api/interview/answer
POST /api/interview/evaluate
GET  /api/interview/summary/{session_id}

Author: Akksai Prathaan
Project: AI Interview System
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.services.interview_service import InterviewService
import app.services.interview_service as service_module
print(service_module.__file__)
router = APIRouter(
    prefix="/api/interview",
    tags=["Interview"]
)

service = InterviewService()


# ============================================================
# Request Models
# ============================================================

class StartInterviewRequest(BaseModel):
    candidate_id: int


class AnswerRequest(BaseModel):
    question_id: int
    answer: str


class EvaluateRequest(BaseModel):
    session_id: int


# ============================================================
# Start Interview
# ============================================================

@router.post("/start")

def start_interview(

    request: StartInterviewRequest,

    db: Session = Depends(get_db),

):
    """
    Create interview session.
    """

    session = service.start_interview(

        db,

        request.candidate_id,

    )

    return {

        "message": "Interview Started",

        "session_id": session.id,

        "status": session.status,

    }


# ============================================================
# Generate Questions
# ============================================================

@router.get("/questions/{session_id}")

def generate_questions(

    session_id: int,

    db: Session = Depends(get_db),

):
    """
    Generate interview questions.
    """

    questions = service.generate_questions(

        db,

        session_id,

    )

    return {

        "session_id": session_id,

        "questions": [

            {

                "id": q.id,

                "question": q.question

            }

            for q in questions

        ]

    }


# ============================================================
# Save Answer
# ============================================================

@router.post("/answer")

def submit_answer(

    request: AnswerRequest,

    db: Session = Depends(get_db),

):
    """
    Save candidate answer.
    """

    question = service.save_answer(

        db,

        request.question_id,

        request.answer,

    )

    if question is None:

        raise HTTPException(

            status_code=404,

            detail="Question not found."

        )

    return {

        "message": "Answer Saved"

    }


# ============================================================
# Evaluate Interview
# ============================================================

@router.post("/evaluate")

def evaluate(

    request: EvaluateRequest,

    db: Session = Depends(get_db),

):
    """
    Evaluate completed interview.
    """

    report = service.evaluate_interview(

        db,

        request.session_id,

    )

    return report


# ============================================================
# Interview Summary
# ============================================================

@router.get("/summary/{session_id}")

def summary(

    session_id: int,

    db: Session = Depends(get_db),

):
    """
    Return interview summary.
    """

    summary = service.get_summary(

        db,

        session_id,

    )

    if summary is None:

        raise HTTPException(

            status_code=404,

            detail="Summary not found."

        )

    return summary