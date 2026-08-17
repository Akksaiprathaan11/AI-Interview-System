"""
Embedding Generator

Generates embeddings for text chunks using
Sentence Transformers.

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

from app.config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Handles embedding model initialization
    and embedding generation.
    """
    def __init__(self):
        print("Step 1: Initializing HuggingFaceEmbeddings...")
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
            )

    print("Step 2: Embedding model initialized successfully.")

    def get_embedding_model(self):
        """
        Returns embedding model.

        Used by ChromaDB.
        """

        return self.embedding_model

    def embed_documents(
        self,
        documents: List[Document]
    ):
        """
        Convert document chunks into embeddings.

        Returns
        -------
        List[List[float]]
        """

        texts = [
            doc.page_content
            for doc in documents
        ]

        embeddings = self.embedding_model.embed_documents(
            texts
        )

        print("=" * 60)
        print(f"Embedded {len(texts)} chunks")
        print(f"Embedding Dimension : {len(embeddings[0])}")
        print("=" * 60)

        return embeddings

    def embed_query(
        self,
        query: str
    ):
        """
        Generate embedding for a search query.
        """

        embedding = self.embedding_model.embed_query(
            query
        )

        return embedding


if __name__ == "__main__":

    from app.rag.document_loader import DocumentLoader
    from app.rag.text_splitter import TextChunker

    loader = DocumentLoader()

    documents = loader.load_all_documents()

    splitter = TextChunker()

    chunks = splitter.split_documents(documents)

    embedding_generator = EmbeddingGenerator()

    embeddings = embedding_generator.embed_documents(chunks)

    print()

    print("=" * 60)

    print("First Embedding")

    print("=" * 60)

    print(embeddings[0][:20])

    print()

    print(f"Vector Length : {len(embeddings[0])}")