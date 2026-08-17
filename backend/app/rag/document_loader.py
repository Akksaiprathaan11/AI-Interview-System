"""
Document Loader

Loads PDF documents from the knowledge_base folder
using LangChain's PyPDFLoader.

Author: Akksai Prathaan
Project: AI Interview System
"""

from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app.config import KNOWLEDGE_BASE_PATH


class DocumentLoader:
    """
    Loads one or more PDF files from the knowledge base.
    """

    def __init__(self, knowledge_base_path: str = KNOWLEDGE_BASE_PATH):
        self.knowledge_base_path = Path(knowledge_base_path)

    def load_pdf(self, pdf_path: str) -> List[Document]:
        """
        Load a single PDF.

        Parameters
        ----------
        pdf_path : str

        Returns
        -------
        List[Document]
        """

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        print(f"Loaded {len(documents)} pages from {pdf_path}")

        return documents

    def load_all_documents(self) -> List[Document]:
        """
        Load every PDF inside the knowledge_base folder.

        Returns
        -------
        List[Document]
        """

        all_documents = []

        pdf_files = list(
            self.knowledge_base_path.glob("*.pdf")
        )

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.knowledge_base_path}"
            )

        for pdf in pdf_files:

            print(f"Reading: {pdf.name}")

            loader = PyPDFLoader(str(pdf))

            docs = loader.load()

            all_documents.extend(docs)

        print(
            f"\nTotal PDFs Loaded : {len(pdf_files)}"
        )

        print(
            f"Total Pages Loaded : {len(all_documents)}"
        )

        return all_documents


if __name__ == "__main__":

    loader = DocumentLoader()

    documents = loader.load_all_documents()

    print()

    print("=" * 50)

    print("Sample Page")

    print("=" * 50)

    print(documents[0].page_content[:1000])

    print()

    print(documents[0].metadata)