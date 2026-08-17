"""
Interview Service

Central business logic for the AI Interview System.

Responsibilities
----------------
1. Parse uploaded resume
2. Extract skills
3. Save candidate
4. Start interview session
5. Generate interview questions
6. Save answers
7. Evaluate interview
8. Store interview summary

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List
from sqlalchemy.orm import Session

from app.database import crud
from app.resume.parser import ResumeParser
from app.resume.skill_extractor import SkillExtractor
from app.interview.question_generator import InterviewQuestionGenerator
from app.interview.evaluator import InterviewEvaluator


class InterviewService:

    def __init__(self):

        self.parser = ResumeParser()

        self.skill_extractor = SkillExtractor()

        self.question_generator = InterviewQuestionGenerator()

        self.evaluator = InterviewEvaluator()

    # --------------------------------------------------
    # Upload Resume
    # --------------------------------------------------

    def upload_resume(

        self,

        db: Session,

        name: str,

        email: str,

        role: str,

        resume_path: str,

    ):
        """
        Parse resume and create candidate.
        """

        resume_text = self.parser.parse_pdf(
            resume_path
        )

        skills = self.skill_extractor.extract_skills(
            resume_text
        )

        candidate = crud.create_candidate(

            db=db,

            name=name,

            email=email,

            role=role,

            resume_path=resume_path,

            extracted_skills=",".join(skills),

        )

        return {

            "candidate": candidate,

            "skills": skills,

            "resume_text": resume_text,

        }

    # --------------------------------------------------
    # Start Interview
    # --------------------------------------------------

    def start_interview(

        self,

        db: Session,

        candidate_id: int,

    ):

        session = crud.create_interview_session(

            db,

            candidate_id,

        )

        return session

    # --------------------------------------------------
    # Generate Questions
    # --------------------------------------------------
        # --------------------------------------------------
    # Generate Questions
    # --------------------------------------------------

    def generate_questions(
        self,
        db: Session,
        session_id: int,
    ):
        """
        Generate and store interview questions
        for an interview session.
        """

        # Get interview session
        session = crud.get_session(
            db,
            session_id,
        )

        if session is None:
            raise ValueError(
                "Interview session not found."
            )

        # Get candidate
        candidate = crud.get_candidate(
            db,
            session.candidate_id,
        )

        if candidate is None:
            raise ValueError(
                f"Candidate not found for session {session_id}. "
                f"candidate_id={session.candidate_id}"
            )

        # Extract candidate skills
        skills = []

        if candidate.extracted_skills:
            skills = [
                skill.strip()
                for skill in candidate.extracted_skills.split(",")
                if skill.strip()
            ]

        print("=" * 70)
        print("GENERATING INTERVIEW QUESTIONS")
        print("=" * 70)
        print(f"Session ID       : {session.id}")
        print(f"Candidate ID     : {candidate.id}")
        print(f"Candidate Name   : {candidate.name}")
        print(f"Candidate Role   : {candidate.role}")
        print(f"Extracted Skills : {skills}")
        print("=" * 70)

        # Generate questions using RAG + LLM
        questions = self.question_generator.generate_questions(
            candidate.role,
            skills,
        )

        if not questions:
            raise ValueError(
                "Question generator returned no questions."
            )

        print(
            f"Generated {len(questions)} questions."
        )

        # Store generated questions
        stored_questions = []

        for question in questions:

            record = crud.save_question(
                db=db,
                session_id=session.id,
                question=question,
                retrieved_context="Generated using RAG",
            )

            stored_questions.append(record)

        print(
            f"Stored {len(stored_questions)} questions "
            f"for session {session.id}."
        )

        return stored_questions
    # --------------------------------------------------
    # Save Answer
    # --------------------------------------------------

    def save_answer(

        self,

        db: Session,

        question_id: int,

        answer: str,

    ):

        return crud.save_answer(

            db,

            question_id,

            answer,

        )

    # --------------------------------------------------
    # Evaluate Interview
    # --------------------------------------------------

    def evaluate_interview(

        self,

        db: Session,

        session_id: int,

    ):

        questions = crud.get_questions(

            db,

            session_id,

        )

        session = crud.get_session(

            db,

            session_id,

        )

        candidate = session.candidate

        question_list = []

        answer_list = []

        for q in questions:

            question_list.append(q.question)

            answer_list.append(q.candidate_answer or "")

        report = self.evaluator.evaluate(

            candidate.role,

            question_list,

            answer_list,

        )

        crud.create_summary(

            db=db,

            session_id=session_id,

            strengths="\n".join(report["strengths"]),

            weaknesses="\n".join(report["weaknesses"]),

            suggestions="\n".join(report["suggestions"]),

            overall_feedback=report["overall_feedback"],

            score=report["overall_score"],

        )

        crud.complete_session(

            db,

            session_id,

        )

        return report

    # --------------------------------------------------
    # Interview Summary
    # --------------------------------------------------

    def get_summary(

        self,

        db: Session,

        session_id: int,

    ):

        return crud.get_summary(

            db,

            session_id,

        )