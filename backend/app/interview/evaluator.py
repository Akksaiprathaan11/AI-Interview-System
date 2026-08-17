"""
Interview Evaluator

Evaluates candidate answers using Gemini.

Responsibilities
----------------
1. Score each answer
2. Generate feedback
3. Identify strengths
4. Identify weaknesses
5. Produce interview summary

Author: Akksai Prathaan
Project: AI Interview System
"""

import json
from typing import List, Dict

from google import genai
from app.config import (GEMINI_API_KEY, LLM_MODEL)


class InterviewEvaluator:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    # ---------------------------------------------------
    # Prompt Builder
    # ---------------------------------------------------

    def build_prompt(
        self,
        questions: List[str],
        answers: List[str],
        role: str,
    ) -> str:

        qa = ""

        for index, (q, a) in enumerate(
            zip(questions, answers),
            start=1
        ):

            qa += f"""
Question {index}

{q}

Answer

{a}

"""

        prompt = f"""
You are an experienced technical interviewer.

Candidate Role:
{role}

Interview:
{qa}

Evaluate every answer carefully.

Return ONLY valid JSON.
Do not include markdown.
Do not include ```json.
Do not include explanations outside the JSON.

Use exactly this structure:

{{
    "overall_score": 90,

    "strengths": [
        "...",
        "..."
    ],

    "weaknesses": [
        "...",
        "..."
    ],

    "suggestions": [
        "...",
        "..."
    ],

    "question_scores": [
        {{
            "question": "...",
            "score": 90,
            "feedback": "..."
        }}
    ],

    "overall_feedback": "..."
}}

Scoring:

0-39   = Poor
40-59  = Average
60-79  = Good
80-100 = Excellent

Important:

- Score every question.
- Scores must be between 0 and 100.
- Evaluate answers based on technical correctness.
- Consider clarity and depth.
- Consider practical understanding.
- Do not give credit for information that is technically incorrect.
- Keep feedback specific to the candidate's answer.
- The overall_score should represent the candidate's overall performance.
"""

        return prompt

    # ---------------------------------------------------
    # Evaluate Interview
    # ---------------------------------------------------

    def evaluate(
        self,
        role: str,
        questions: List[str],
        answers: List[str],
    ) -> Dict:

        prompt = self.build_prompt(
            questions,
            answers,
            role,
        )

        print("=" * 70)
        print("EVALUATING INTERVIEW")
        print("=" * 70)
        print(f"Role: {role}")
        print(f"Questions: {len(questions)}")
        print(f"Answers: {len(answers)}")
        print("=" * 70)

        try:

            response = self.client.models.generate_content(
                model=LLM_MODEL,
                contents=prompt,
            )

            result = response.text.strip()

            print("=" * 70)
            print("GEMINI EVALUATION RESPONSE")
            print("=" * 70)
            print(result)
            print("=" * 70)

            # Remove markdown fences if Gemini returns them
            if result.startswith("```json"):
                result = result[7:]

            elif result.startswith("```"):
                result = result[3:]

            if result.endswith("```"):
                result = result[:-3]

            result = result.strip()

            return json.loads(result)

        except json.JSONDecodeError as e:

            print("JSON parsing failed:")
            print(e)

            return {
                "overall_score": 0,
                "strengths": [],
                "weaknesses": [],
                "suggestions": [],
                "question_scores": [],
                "overall_feedback":
                    "Evaluation parsing failed."
            }

        except Exception as e:

            print("=" * 70)
            print("GEMINI EVALUATION ERROR")
            print("=" * 70)
            print(type(e).__name__)
            print(str(e))
            print("=" * 70)

            raise

    # ---------------------------------------------------
    # Print Report
    # ---------------------------------------------------

    def print_report(
        self,
        report: Dict
    ):

        print()

        print("=" * 70)
        print("INTERVIEW REPORT")
        print("=" * 70)

        print()

        print(
            "Overall Score:",
            report["overall_score"]
        )

        print()

        print("Strengths")

        for item in report["strengths"]:
            print("-", item)

        print()

        print("Weaknesses")

        for item in report["weaknesses"]:
            print("-", item)

        print()

        print("Suggestions")

        for item in report["suggestions"]:
            print("-", item)

        print()

        print("Question Evaluation")

        print()

        for question in report["question_scores"]:

            print(
                question["question"]
            )

            print(
                "Score:",
                question["score"]
            )

            print(
                question["feedback"]
            )

            print()

        print("=" * 70)

        print("Overall Feedback")

        print("=" * 70)

        print(
            report["overall_feedback"]
        )


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    evaluator = InterviewEvaluator()

    role = "AI/ML Engineer"

    questions = [

        "Explain Gradient Descent.",

        "What is Overfitting?",

        "Difference between CNN and RNN?"

    ]

    answers = [

        "Gradient Descent minimizes loss by updating weights.",

        "Overfitting happens when the model memorizes training data.",

        "CNN is mainly used for images while RNN handles sequential data."

    ]

    report = evaluator.evaluate(
        role,
        questions,
        answers
    )

    evaluator.print_report(report)