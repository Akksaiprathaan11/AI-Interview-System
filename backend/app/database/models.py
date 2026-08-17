"""
Database Models

Defines all database tables for the AI Interview System.

Author: Akshay
Project: AI Interview System
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.db import Base


# ==========================================================
# Candidate Table
# ==========================================================

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=True)

    email = Column(String(150), nullable=True)

    role = Column(String(100), nullable=False)

    resume_path = Column(String(255), nullable=False)

    extracted_skills = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    interview_sessions = relationship(
        "InterviewSession",
        back_populates="candidate",
        cascade="all, delete"
    )


# ==========================================================
# Interview Session
# ==========================================================

class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id")
    )

    status = Column(
        String(30),
        default="In Progress"
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )

    candidate = relationship(
        "Candidate",
        back_populates="interview_sessions"
    )

    questions = relationship(
        "InterviewQuestion",
        back_populates="session",
        cascade="all, delete"
    )

    summary = relationship(
        "InterviewSummary",
        back_populates="session",
        uselist=False,
        cascade="all, delete"
    )


# ==========================================================
# Interview Questions
# ==========================================================

class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("interview_sessions.id")
    )

    question = Column(Text)

    retrieved_context = Column(Text)

    candidate_answer = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    session = relationship(
        "InterviewSession",
        back_populates="questions"
    )


# ==========================================================
# Interview Summary
# ==========================================================

class InterviewSummary(Base):
    __tablename__ = "interview_summary"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("interview_sessions.id")
    )

    strengths = Column(Text)

    weaknesses = Column(Text)

    suggestions = Column(Text)

    overall_feedback = Column(Text)

    score = Column(Integer)

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    session = relationship(
        "InterviewSession",
        back_populates="summary"
    )