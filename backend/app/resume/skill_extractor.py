"""
Skill Extractor

Extracts technical skills from resume text.

Responsibilities:
- Detect technical skills
- Remove duplicates
- Categorize skills
- Return structured skill list

Author: Akksai Prathaan
Project: AI Interview System
"""

import re
from typing import List, Dict


class SkillExtractor:
    """
    Extract technical skills from resume text.
    """

    def __init__(self):

        # Programming Languages
        self.programming_languages = [
            "Python",
            "Java",
            "C",
            "C++",
            "C#",
            "JavaScript",
            "TypeScript",
            "R",
            "Go",
            "Rust",
            "PHP",
            "Kotlin",
            "Swift"
        ]

        # AI / ML
        self.ai_ml = [
            "Machine Learning",
            "Deep Learning",
            "Artificial Intelligence",
            "Neural Networks",
            "Computer Vision",
            "NLP",
            "TensorFlow",
            "PyTorch",
            "Keras",
            "Scikit-learn",
            "OpenCV",
            "XGBoost",
            "LightGBM",
            "LLM",
            "Generative AI",
            "LangChain",
            "RAG",
            "Prompt Engineering"
        ]

        # Data Science
        self.data_science = [
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Seaborn",
            "SciPy",
            "Power BI",
            "Tableau",
            "Excel"
        ]

        # Backend
        self.backend = [
            "FastAPI",
            "Flask",
            "Django",
            "Spring Boot",
            "Node.js",
            "Express.js"
        ]

        # Database
        self.database = [
            "SQL",
            "MySQL",
            "PostgreSQL",
            "SQLite",
            "MongoDB",
            "Oracle",
            "Redis"
        ]

        # Cloud
        self.cloud = [
            "AWS",
            "Azure",
            "Google Cloud",
            "Docker",
            "Kubernetes"
        ]

        # Tools
        self.tools = [
            "Git",
            "GitHub",
            "Linux",
            "VS Code",
            "Jupyter",
            "Postman"
        ]

        self.all_skills = (
            self.programming_languages
            + self.ai_ml
            + self.data_science
            + self.backend
            + self.database
            + self.cloud
            + self.tools
        )

    # -------------------------------------------------------
    # Extract Skills
    # -------------------------------------------------------

    def extract_skills(
        self,
        resume_text: str
    ) -> List[str]:
        """
        Extract skills from resume text.
        """

        found_skills = []

        text = resume_text.lower()

        for skill in self.all_skills:

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):

                found_skills.append(skill)

        return sorted(list(set(found_skills)))

    # -------------------------------------------------------
    # Categorize Skills
    # -------------------------------------------------------

    def categorize_skills(
        self,
        skills: List[str]
    ) -> Dict:

        return {
            "Programming": [
                s for s in skills
                if s in self.programming_languages
            ],

            "AI_ML": [
                s for s in skills
                if s in self.ai_ml
            ],

            "Data_Science": [
                s for s in skills
                if s in self.data_science
            ],

            "Backend": [
                s for s in skills
                if s in self.backend
            ],

            "Database": [
                s for s in skills
                if s in self.database
            ],

            "Cloud": [
                s for s in skills
                if s in self.cloud
            ],

            "Tools": [
                s for s in skills
                if s in self.tools
            ]
        }

    # -------------------------------------------------------
    # Total Skills
    # -------------------------------------------------------

    def total_skills(
        self,
        skills: List[str]
    ) -> int:

        return len(skills)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    sample_resume = """
    Python Developer

    Skills

    Python
    TensorFlow
    Pandas
    NumPy
    Machine Learning
    FastAPI
    SQL
    Docker
    Git
    Linux
    """

    extractor = SkillExtractor()

    skills = extractor.extract_skills(sample_resume)

    print("=" * 60)
    print("Extracted Skills")
    print("=" * 60)

    print(skills)

    print()

    print("=" * 60)
    print("Skill Categories")
    print("=" * 60)

    categories = extractor.categorize_skills(skills)

    for category, values in categories.items():

        print(f"{category}: {values}")

    print()

    print("Total Skills:", extractor.total_skills(skills))