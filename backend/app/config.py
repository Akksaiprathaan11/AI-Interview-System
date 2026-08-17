from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Interview System")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.5-flash")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./interview_system.db"
)

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "../chroma_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "ai_interview_collection"
)

KNOWLEDGE_BASE_PATH = os.getenv(
    "KNOWLEDGE_BASE_PATH",
    "../knowledge_base"
)

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER",
    "uploads"
)

# Create upload folder if it doesn't exist
Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", 5))
MAX_QUESTIONS = int(os.getenv("MAX_QUESTIONS", 10))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")