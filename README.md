# 🤖 AI Interview System

An AI-powered Interview Preparation and Evaluation Platform that generates role-specific technical interview questions based on a candidate's resume and evaluates responses using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

---

## 📌 Features

- 📄 Resume Upload (PDF)
- 🧠 Resume Parsing & Skill Extraction
- 🤖 AI-generated Technical Interview Questions
- 📚 RAG-based Knowledge Retrieval
- 💬 Candidate Answer Submission
- 📊 AI Interview Evaluation
- 📈 Performance Summary
- 💾 SQLite Database
- 🔍 ChromaDB Vector Store
- 🌐 React + FastAPI Architecture

---

## 🏗 Project Architecture

```
AI-Interview-System/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── interview/
│   │   ├── models/
│   │   ├── rag/
│   │   ├── resume/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── context/
│       ├── hooks/
│       ├── pages/
│       └── services/
│
├── knowledge_base/
├── chroma_db/
├── docs/
│
├── README.md
├── docker-compose.yml
└── LICENSE
```

---

# 🛠 Technology Stack

## Frontend

- React
- Vite
- Axios
- React Router

---

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

---

## AI & Machine Learning

- OpenAI GPT
- LangChain
- ChromaDB
- Sentence Transformers

---

## Document Processing

- PyPDF
- PDF Parsing
- Resume Skill Extraction

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Interview-System.git

cd AI-Interview-System
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

Create `.env`

```env
OPENAI_API_KEY=your_api_key

DATABASE_URL=sqlite:///./interview_system.db

CHROMA_DB_PATH=../chroma_db

COLLECTION_NAME=ai_interview_collection

KNOWLEDGE_BASE_PATH=../knowledge_base
```

---

Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger API

```
http://localhost:8000/docs
```

---

# Frontend Setup

```bash
cd frontend
```

Install Packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# Knowledge Base

Place technical PDFs inside

```
knowledge_base/
```

Example

```
AI_ML_Book.pdf

Backend_Engineering.pdf

Data_Structures.pdf
```

Then create embeddings

```bash
python -m app.rag.ingest
```

---

# Workflow

```
Resume Upload

↓

Resume Parsing

↓

Skill Extraction

↓

Knowledge Retrieval (RAG)

↓

Question Generation

↓

Candidate Answers

↓

AI Evaluation

↓

Performance Summary
```

---

# REST API

| Method | Endpoint | Description |
|----------|----------------------------|------------------------------|
| POST | /api/resume/upload | Upload Resume |
| POST | /api/interview/start | Start Interview |
| GET | /api/interview/questions/{id} | Get Questions |
| POST | /api/interview/answer | Submit Answer |
| POST | /api/interview/evaluate | Evaluate Interview |
| GET | /api/interview/summary/{id} | Interview Summary |
| GET | /api/health | Health Check |

---

# Database

SQLite stores

- Candidates
- Interview Sessions
- Questions
- Answers
- Evaluation Results

---

# RAG Pipeline

```
PDF Files

↓

Document Loader

↓

Text Splitter

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

LLM

↓

Interview Questions
```

---

# Future Improvements

- Voice-based Interview
- Video Interview Support
- Authentication
- Admin Dashboard
- PDF Report Generation
- Docker Deployment
- Cloud Storage
- Multi-LLM Support
- Leaderboard
- Analytics Dashboard

---

# Screenshots

Project Screenshots are available in

```
docs/
```

---

# Author

**Akksai Prathaan**

B.Tech Artificial Intelligence & Data Science

---

# License

This project is licensed under the MIT License.

```
MIT License
```