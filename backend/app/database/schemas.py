"""
Pydantic Schemas

Defines request and response models
for API validation.

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


# ==========================================================
# Candidate Schemas
# ==========================================================

class CandidateBase(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: str


class CandidateCreate(CandidateBase):
    resume_path: str
    extracted_skills: Optional[str] = None


class CandidateResponse(CandidateBase):
    id: int
    resume_path: str
    extracted_skills: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# ==========================================================
# Resume Upload
# ==========================================================

class ResumeUploadResponse(BaseModel):
    candidate_id: int
    message: str
    extracted_skills: List[str]


# ==========================================================
# Interview Session
# ==========================================================

class InterviewSessionCreate(BaseModel):
    candidate_id: int


class InterviewSessionResponse(BaseModel):
    id: int
    candidate_id: int
    status: str
    started_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True


# ==========================================================
# Generate Questions
# ==========================================================

class GenerateQuestionRequest(BaseModel):
    session_id: int


class QuestionResponse(BaseModel):
    id: int
    question: str

    class Config:
        from_attributes = True


# ==========================================================
# Submit Answer
# ==========================================================

class AnswerRequest(BaseModel):
    question_id: int
    answer: str


class AnswerResponse(BaseModel):
    success: bool
    message: str


# ==========================================================
# Interview Summary
# ==========================================================

class SummaryResponse(BaseModel):
    score: int
    strengths: str
    weaknesses: str
    suggestions: str
    overall_feedback: str

    class Config:
        from_attributes = True


# ==========================================================
# Health Check
# ==========================================================

class HealthResponse(BaseModel):
    status: str
    version: str