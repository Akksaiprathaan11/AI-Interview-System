"""
Application Constants

This file contains all reusable constants used throughout the
AI Interview System.

Author: Akksai Prathaan
Project: AI Interview System
"""

# ==========================================================
# Supported Job Roles
# ==========================================================

SUPPORTED_ROLES = [
    "AI/ML Engineer",
    "Backend Engineer",
    "Data Scientist",
    "Python Developer",
    "Machine Learning Engineer",
]

# ==========================================================
# Resume Configuration
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ".pdf",
    ".docx",
    ".txt",
]

MAX_FILE_SIZE_MB = 10

UPLOAD_DIRECTORY = "uploads"

# ==========================================================
# Interview Configuration
# ==========================================================

MAX_INTERVIEW_QUESTIONS = 10

QUESTION_DIFFICULTY = [
    "Easy",
    "Medium",
    "Hard",
]

SESSION_STATUS = {
    "STARTED": "In Progress",
    "COMPLETED": "Completed",
    "FAILED": "Failed",
}

# ==========================================================
# RAG Configuration
# ==========================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 5

VECTOR_COLLECTION_NAME = "ml_knowledge_base"

# ==========================================================
# Embedding Models
# ==========================================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================================
# LLM Models
# ==========================================================

OPENAI_MODEL = "gpt-4.1-mini"

# If using Gemini
GEMINI_MODEL = "gemini-2.5-flash"

# ==========================================================
# Prompt Limits
# ==========================================================

MAX_CONTEXT_LENGTH = 4000

MAX_RESPONSE_TOKENS = 800

TEMPERATURE = 0.7

# ==========================================================
# Database Tables
# ==========================================================

TABLE_CANDIDATE = "candidates"

TABLE_SESSION = "interview_sessions"

TABLE_QUESTION = "interview_questions"

TABLE_SUMMARY = "interview_summary"

# ==========================================================
# Logging
# ==========================================================

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

LOG_LEVEL = "INFO"

# ==========================================================
# Default Messages
# ==========================================================

SUCCESS_UPLOAD = "Resume uploaded successfully."

SUCCESS_QUESTIONS = "Interview questions generated successfully."

SUCCESS_SUMMARY = "Interview summary generated successfully."

ERROR_FILE = "Unsupported file type."

ERROR_DATABASE = "Database operation failed."

ERROR_RAG = "Failed to retrieve relevant knowledge."

ERROR_LLM = "Failed to generate interview questions."

# ==========================================================
# API Routes
# ==========================================================

API_PREFIX = "/api"

RESUME_ROUTE = "/resume"

INTERVIEW_ROUTE = "/interview"

SUMMARY_ROUTE = "/summary"

HEALTH_ROUTE = "/health"

# ==========================================================
# Evaluation Score Range
# ==========================================================

MIN_SCORE = 0

MAX_SCORE = 100

PASSING_SCORE = 60

# ==========================================================
# Knowledge Base
# ==========================================================

KNOWLEDGE_FOLDER = "knowledge_base"

DEFAULT_BOOK = "MachineLearningBook.pdf"

# ==========================================================
# Interview Flow
# ==========================================================

FLOW = [
    "Upload Resume",
    "Parse Resume",
    "Extract Skills",
    "Select Role",
    "Retrieve Context",
    "Generate Questions",
    "Answer Questions",
    "Generate Summary",
]