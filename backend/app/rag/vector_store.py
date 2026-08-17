"""
Vector Store

Creates and manages the Chroma Vector Database.

Responsibilities:
- Store document embeddings
- Persist vector database
- Perform similarity search

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
)

from app.rag.embedding import EmbeddingGenerator


class VectorStore:

    def __init__(self):

        self.embedding_generator = EmbeddingGenerator()

        self.embedding_model = (
            self.embedding_generator.get_embedding_model()
        )

        self.vector_db = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=self.embedding_model,
            persist_directory=CHROMA_DB_PATH,
        )

    # -----------------------------------------------------
    # Add Documents
    # -----------------------------------------------------

    def add_documents(
        self,
        documents: List[Document],
    ):
        """
        Store document chunks in ChromaDB.
        """

        self.vector_db.add_documents(documents)

        print("=" * 60)
        print(f"{len(documents)} chunks stored.")
        print("=" * 60)

    # -----------------------------------------------------
    # Similarity Search
    # -----------------------------------------------------

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ):
        """
        Retrieve the most relevant chunks.
        """

        results = self.vector_db.similarity_search(
            query=query,
            k=k,
        )

        return results

    # -----------------------------------------------------
    # Similarity Search with Scores
    # -----------------------------------------------------

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5,
    ):
        """
        Returns chunks with similarity scores.
        """

        results = self.vector_db.similarity_search_with_score(
            query=query,
            k=k,
        )

        return results

    # -----------------------------------------------------
    # Delete Collection
    # -----------------------------------------------------

    def reset_database(self):
        """
        Delete all stored vectors.
        """

        self.vector_db.delete_collection()

        print("Vector database cleared.")

    # -----------------------------------------------------
    # Get Vector Count
    # -----------------------------------------------------

    def count_documents(self):
        """
        Returns total vectors stored.
        """

        collection = self.vector_db._collection

        return collection.count()

    # -----------------------------------------------------
    # Get Retriever
    # -----------------------------------------------------

    def as_retriever(
        self,
        k: int = 5,
    ):
        """
        Returns LangChain Retriever.
        """

        return self.vector_db.as_retriever(
            search_kwargs={
                "k": k
            }
        )


# ---------------------------------------------------------
# Testing
# ---------------------------------------------------------

if __name__ == "__main__":

    from app.rag.document_loader import DocumentLoader
    from app.rag.text_splitter import TextChunker

    loader = DocumentLoader()

    documents = loader.load_all_documents()

    splitter = TextChunker()

    chunks = splitter.split_documents(documents)

    store = VectorStore()

    print("\nAdding chunks to ChromaDB...\n")

    store.add_documents(chunks)

    print()

    print("=" * 60)
    print("Total Stored Chunks")
    print("=" * 60)

    print(store.count_documents())

    print()

    query = "Explain Gradient Descent"

    print("=" * 60)
    print("Similarity Search")
    print("=" * 60)

    results = store.similarity_search(query)

    for i, doc in enumerate(results, start=1):

        print(f"\nResult {i}")

        print("-" * 50)

        print(doc.page_content[:500])

        print()

        print(doc.metadata)