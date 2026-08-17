# AI Interview System API Documentation

**Project:** AI Interview System  
**Author:** Akksai Prathaan  
**Backend:** FastAPI  
**Version:** 1.0.0

---

# Base URL

```
http://localhost:8000
```

---

# Authentication

Currently, authentication is **not implemented**.

---

# API Endpoints

## 1. Root Endpoint

### GET /

Returns basic application information.

### Response

```json
{
    "application": "AI Interview System",
    "author": "Akksai Prathaan",
    "version": "1.0.0",
    "status": "Running",
    "documentation": "/docs"
}
```

---

# 2. Health Check

### GET

```
/api/health
```

Checks application status.

### Response

```json
{
    "application":"AI Interview System",
    "status":"Running",
    "database":"Healthy",
    "vector_database":"Healthy",
    "version":"1.0.0"
}
```

---

# Resume APIs

## 3. Upload Resume

### POST

```
/api/resume/upload
```

Uploads a candidate resume, extracts text, identifies skills, and stores candidate details.

### Form Data

| Parameter | Type | Required |
|-----------|------|----------|
| name | String | Yes |
| email | String | Yes |
| role | String | Yes |
| resume | PDF File | Yes |

### Success Response

```json
{
    "message":"Resume uploaded successfully",
    "candidate_id":1,
    "name":"John Doe",
    "role":"AI Engineer",
    "skills":[
        "Python",
        "Machine Learning",
        "TensorFlow",
        "FastAPI"
    ]
}
```

---

## 4. Get Candidate

### GET

```
/api/resume/{candidate_id}
```

Returns candidate details.

Example

```
/api/resume/1
```

---

## 5. Get All Candidates

### GET

```
/api/resume/
```

Returns all registered candidates.

---

# Interview APIs

## 6. Start Interview

### POST

```
/api/interview/start
```

Creates a new interview session.

### Request

```json
{
    "candidate_id":1
}
```

### Response

```json
{
    "message":"Interview Started",
    "session_id":1,
    "status":"In Progress"
}
```

---

## 7. Generate Questions

### GET

```
/api/interview/questions/{session_id}
```

Returns AI-generated interview questions.

Example

```
/api/interview/questions/1
```

### Response

```json
{
    "session_id":1,
    "questions":[
        {
            "id":1,
            "question":"Explain Gradient Descent."
        },
        {
            "id":2,
            "question":"What is TensorFlow?"
        }
    ]
}
```

---

## 8. Submit Answer

### POST

```
/api/interview/answer
```

Stores the candidate's answer.

### Request

```json
{
    "question_id":1,
    "answer":"Gradient Descent minimizes the loss function."
}
```

### Response

```json
{
    "message":"Answer Saved"
}
```

---

## 9. Evaluate Interview

### POST

```
/api/interview/evaluate
```

Evaluates all answers using the LLM.

### Request

```json
{
    "session_id":1
}
```

### Response

```json
{
    "overall_score":91,
    "strengths":[
        "Good ML knowledge"
    ],
    "weaknesses":[
        "Needs deployment experience"
    ],
    "suggestions":[
        "Practice Docker"
    ],
    "overall_feedback":"Excellent performance."
}
```

---

## 10. Interview Summary

### GET

```
/api/interview/summary/{session_id}
```

Returns the final interview report.

Example

```
/api/interview/summary/1
```

---

# Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 404 | Resource Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Technology Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- OpenAI API
- LangChain
- ChromaDB

## AI Components

- Resume Parsing
- Skill Extraction
- Retrieval-Augmented Generation (RAG)
- LLM-based Question Generation
- AI Interview Evaluation

---

# API Workflow

```
Resume Upload
        │
        ▼
Resume Parsing
        │
        ▼
Skill Extraction
        │
        ▼
Store Candidate
        │
        ▼
Start Interview
        │
        ▼
Generate Questions
        │
        ▼
Candidate Answers
        │
        ▼
Evaluate Answers
        │
        ▼
Generate Summary
        │
        ▼
Return Report
```

---

# Swagger Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# Version

Current API Version

```
1.0.0
```

---

# Author

**Akksai Prathaan**

B.Tech Artificial Intelligence and Data Science

AI Interview System Project