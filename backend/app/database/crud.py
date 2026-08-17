"""
CRUD Operations

Contains all database operations for the
AI Interview System.

Author: Akksai Prathaan
Project: AI Interview System
"""

from datetime import datetime
from sqlalchemy.orm import Session

from app.database.models import (
    Candidate,
    InterviewSession,
    InterviewQuestion,
    InterviewSummary,
)


# ==========================================================
# Candidate CRUD
# ==========================================================

def create_candidate(
    db: Session,
    name: str,
    email: str,
    role: str,
    resume_path: str,
    extracted_skills: str,
):
    """
    Create a new candidate.
    """

    candidate = Candidate(
        name=name,
        email=email,
        role=role,
        resume_path=resume_path,
        extracted_skills=extracted_skills,
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


def get_candidate(
    db: Session,
    candidate_id: int,
):
    """
    Get candidate by ID.
    """

    return (
        db.query(Candidate)
        .filter(Candidate.id == candidate_id)
        .first()
    )


def get_all_candidates(db: Session):
    """
    Return all candidates.
    """

    return db.query(Candidate).all()


# ==========================================================
# Interview Session CRUD
# ==========================================================

def create_interview_session(
    db: Session,
    candidate_id: int,
):
    """
    Create interview session.
    """

    session = InterviewSession(
        candidate_id=candidate_id,
        status="In Progress",
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


def get_session(
    db: Session,
    session_id: int,
):
    """
    Fetch interview session.
    """

    return (
        db.query(InterviewSession)
        .filter(
            InterviewSession.id == session_id
        )
        .first()
    )


def complete_session(
    db: Session,
    session_id: int,
):
    """
    Mark interview as completed.
    """

    session = get_session(db, session_id)

    if session:

        session.status = "Completed"

        session.completed_at = datetime.utcnow()

        db.commit()

        db.refresh(session)

    return session


# ==========================================================
# Question CRUD
# ==========================================================

def save_question(
    db: Session,
    session_id: int,
    question: str,
    retrieved_context: str,
):
    """
    Store generated question.
    """

    interview_question = InterviewQuestion(
        session_id=session_id,
        question=question,
        retrieved_context=retrieved_context,
    )

    db.add(interview_question)

    db.commit()

    db.refresh(interview_question)

    return interview_question


def get_questions(
    db: Session,
    session_id: int,
):
    """
    Fetch all questions for a session.
    """

    return (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.session_id == session_id
        )
        .all()
    )


# ==========================================================
# Answer CRUD
# ==========================================================

def save_answer(
    db: Session,
    question_id: int,
    answer: str,
):
    """
    Save candidate answer.
    """

    question = (
        db.query(InterviewQuestion)
        .filter(
            InterviewQuestion.id == question_id
        )
        .first()
    )

    if question:

        question.candidate_answer = answer

        db.commit()

        db.refresh(question)

    return question


# ==========================================================
# Summary CRUD
# ==========================================================

def create_summary(
    db: Session,
    session_id: int,
    strengths: str,
    weaknesses: str,
    suggestions: str,
    overall_feedback: str,
    score: int,
):
    """
    Store interview summary.
    """

    summary = InterviewSummary(
        session_id=session_id,
        strengths=strengths,
        weaknesses=weaknesses,
        suggestions=suggestions,
        overall_feedback=overall_feedback,
        score=score,
    )

    db.add(summary)

    db.commit()

    db.refresh(summary)

    return summary


def get_summary(
    db: Session,
    session_id: int,
):
    """
    Retrieve interview summary.
    """

    return (
        db.query(InterviewSummary)
        .filter(
            InterviewSummary.session_id == session_id
        )
        .first()
    )


# ==========================================================
# Dashboard CRUD
# ==========================================================

def get_candidate_history(
    db: Session,
    candidate_id: int,
):
    """
    Get all interview sessions for a candidate.
    """

    return (
        db.query(InterviewSession)
        .filter(
            InterviewSession.candidate_id == candidate_id
        )
        .all()
    )


def get_total_candidates(db: Session):
    """
    Count total candidates.
    """

    return db.query(Candidate).count()


def get_total_sessions(db: Session):
    """
    Count total interview sessions.
    """

    return db.query(InterviewSession).count()