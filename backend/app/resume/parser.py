"""
Resume Parser

Extracts text from uploaded resume PDFs.

Responsibilities:
- Read PDF resumes
- Extract text page by page
- Clean extracted text
- Return plain text for skill extraction

Author: Akshay
Project: AI Interview System
"""

import re
from pathlib import Path

import fitz  # PyMuPDF


class ResumeParser:
    """
    Resume PDF Parser
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Parse Resume
    # ---------------------------------------------------------

    def parse_pdf(
        self,
        pdf_path: str
    ) -> str:
        """
        Extract text from PDF.

        Parameters
        ----------
        pdf_path : str

        Returns
        -------
        str
            Resume text
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"Resume not found: {pdf_path}"
            )

        document = fitz.open(pdf_path)

        text = ""

        for page in document:

            text += page.get_text()

            text += "\n"

        document.close()

        return self.clean_text(text)

    # ---------------------------------------------------------
    # Clean Resume Text
    # ---------------------------------------------------------

    def clean_text(
        self,
        text: str
    ) -> str:
        """
        Clean extracted text.
        """

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", text)

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove multiple blank lines
        text = re.sub(r"\n+", "\n", text)

        return text.strip()

    # ---------------------------------------------------------
    # Count Words
    # ---------------------------------------------------------

    def word_count(
        self,
        text: str
    ) -> int:

        return len(text.split())

    # ---------------------------------------------------------
    # Count Characters
    # ---------------------------------------------------------

    def character_count(
        self,
        text: str
    ) -> int:

        return len(text)


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    parser = ResumeParser()

    resume_path = "uploads/sample_resume.pdf"

    resume_text = parser.parse_pdf(
        resume_path
    )

    print("=" * 60)
    print("Resume Text")
    print("=" * 60)

    print(resume_text[:3000])

    print()

    print("=" * 60)
    print("Statistics")
    print("=" * 60)

    print(
        "Words:",
        parser.word_count(resume_text)
    )

    print(
        "Characters:",
        parser.character_count(resume_text)
    )