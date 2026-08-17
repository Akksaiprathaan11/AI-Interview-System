"""
Interview Question Generator

Uses Retrieval-Augmented Generation (RAG)
to generate role-specific interview questions.

Pipeline

Resume
    ↓
Skill Extractor
    ↓
Retriever
    ↓
Context
    ↓
Gemini
    ↓
Interview Questions

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List

from google import genai

from app.config import GEMINI_API_KEY, LLM_MODEL


class InterviewQuestionGenerator:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = LLM_MODEL

    # --------------------------------------------------
    # Build Prompt
    # --------------------------------------------------

    def build_prompt(
        self,
        role: str,
        skills: list[str],
    ):

        skills_text = ", ".join(skills)

        prompt = f"""
You are an expert technical interviewer.

Generate interview questions for the following candidate.

Role:
{role}

Skills:
{skills_text}

Requirements:

1. Generate exactly 10 interview questions.
2. Cover the candidate's listed skills.
3. Include conceptual questions.
4. Include practical implementation questions.
5. Include problem-solving questions.
6. Include real-world scenario questions.
7. Questions should be appropriate for the candidate's role.
8. Do not provide answers.
9. Return ONLY the questions.
10. Number them from 1 to 10.

Generate the interview questions now.
"""

        return prompt

    # --------------------------------------------------
    # Generate Questions
    # --------------------------------------------------

    def generate_questions(
        self,
        role: str,
        skills: list[str],
    ):

        prompt = self.build_prompt(
            role,
            skills,
        )

        print("=" * 60)
        print("Generated Query")
        print("=" * 60)
        print(prompt)

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        text = response.text.strip()

        questions = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            # Remove common numbering formats
            if line[0].isdigit():

                question = line

                if "." in question[:4]:
                    question = question.split(
                        ".",
                        1
                    )[1].strip()

                elif ")" in question[:4]:
                    question = question.split(
                        ")",
                        1
                    )[1].strip()

                questions.append(question)

            elif line.startswith("-"):
                questions.append(
                    line[1:].strip()
                )

        # Fallback if Gemini doesn't number the questions
        if not questions:
            questions = [
                q.strip()
                for q in text.split("\n")
                if q.strip()
            ]

        questions = questions[:10]

        print("=" * 60)
        print(f"Generated {len(questions)} Questions")
        print("=" * 60)

        self.print_questions(questions)

        return questions

    # --------------------------------------------------
    # Print Questions
    # --------------------------------------------------

    def print_questions(
        self,
        questions: list[str],
    ):

        for index, question in enumerate(
            questions,
            start=1
        ):
            print(
                f"{index}. {question}"
            )


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    generator = InterviewQuestionGenerator()

    role = "AI/ML Engineer"

    skills = [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Pandas",
        "NumPy",
        "FastAPI",
    ]

    questions = generator.generate_questions(
        role,
        skills,
    )

    generator.print_questions(
        questions
    )