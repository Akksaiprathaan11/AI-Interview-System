"""
Retriever

Responsible for retrieving relevant context
from the Chroma Vector Database.

Responsibilities
----------------
1. Build dynamic search queries
2. Search ChromaDB
3. Return relevant context
4. Prepare context for the LLM

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List, Dict

from app.config import TOP_K_RESULTS
from app.rag.vector_store import VectorStore


class RAGRetriever:

    def __init__(self):

        self.vector_store = VectorStore()

    # ---------------------------------------------------
    # Build Search Query
    # ---------------------------------------------------

    def build_query(
        self,
        role: str,
        skills: List[str]
    ) -> str:
        """
        Creates a semantic search query
        from role + resume skills.
        """

        skills_text = ", ".join(skills)

        query = (
            f"{role} interview questions "
            f"covering {skills_text}. "
            f"Include concepts, practical implementation, "
            f"best practices and problem solving."
        )

        return query

    # ---------------------------------------------------
    # Retrieve Documents
    # ---------------------------------------------------

    def retrieve_documents(
        self,
        role: str,
        skills: List[str],
        top_k: int = TOP_K_RESULTS
    ):
        """
        Retrieve relevant chunks.
        """

        query = self.build_query(
            role,
            skills
        )

        print("=" * 60)
        print("Generated Query")
        print("=" * 60)
        print(query)
        print()

        results = self.vector_store.similarity_search(
            query=query,
            k=top_k
        )

        return results

    # ---------------------------------------------------
    # Context For LLM
    # ---------------------------------------------------

    def get_context(
        self,
        role: str,
        skills: List[str],
        top_k: int = TOP_K_RESULTS
    ) -> str:
        """
        Returns retrieved chunks as one context string.
        """

        documents = self.retrieve_documents(
            role,
            skills,
            top_k
        )

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context

    # ---------------------------------------------------
    # Metadata
    # ---------------------------------------------------

    def get_context_with_metadata(
        self,
        role: str,
        skills: List[str],
        top_k: int = TOP_K_RESULTS
    ) -> List[Dict]:
        """
        Returns context together with metadata.
        Useful for debugging and traceability.
        """

        documents = self.retrieve_documents(
            role,
            skills,
            top_k
        )

        results = []

        for doc in documents:

            results.append(
                {
                    "content": doc.page_content,
                    "metadata": doc.metadata,
                }
            )

        return results


# -------------------------------------------------------
# Testing
# -------------------------------------------------------

if __name__ == "__main__":

    retriever = RAGRetriever()

    role = "AI/ML Engineer"

    skills = [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "Pandas",
        "NumPy"
    ]

    context = retriever.get_context(
        role,
        skills
    )

    print("=" * 60)
    print("Retrieved Context")
    print("=" * 60)

    print(context[:3000])

    print()

    print("=" * 60)
    print("Metadata")
    print("=" * 60)

    metadata = retriever.get_context_with_metadata(
        role,
        skills
    )

    for item in metadata:

        print(item["metadata"])