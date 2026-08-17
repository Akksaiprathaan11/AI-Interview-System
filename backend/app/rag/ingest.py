"""
Knowledge Base Ingestion Pipeline

This script ingests role-specific PDF documents into ChromaDB.

Pipeline:
    PDFs
      ↓
Document Loader
      ↓
Text Splitter
      ↓
Embeddings
      ↓
Chroma Vector Database

Run:
    python app/rag/ingest.py

Author: Akksai Prathaan
Project: AI Interview System
"""

from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextChunker
from app.rag.vector_store import VectorStore


class KnowledgeBaseIngestion:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = TextChunker()

        self.vector_store = VectorStore()

    # ----------------------------------------------------
    # Step 1 : Load PDFs
    # ----------------------------------------------------

    def load_documents(self):

        print("=" * 70)
        print("STEP 1 : Loading PDF Documents")
        print("=" * 70)

        documents = self.loader.load_all_documents()

        print(f"Loaded {len(documents)} pages.\n")

        return documents

    # ----------------------------------------------------
    # Step 2 : Split Documents
    # ----------------------------------------------------

    def split_documents(self, documents):

        print("=" * 70)
        print("STEP 2 : Splitting Documents")
        print("=" * 70)

        chunks = self.chunker.split_documents(documents)

        print(f"Generated {len(chunks)} chunks.\n")

        return chunks

    # ----------------------------------------------------
    # Step 3 : Store in Chroma
    # ----------------------------------------------------

    def store_embeddings(self, chunks):

        print("=" * 70)
        print("STEP 3 : Creating Embeddings")
        print("=" * 70)

        self.vector_store.add_documents(chunks)

        print()

        print("=" * 70)
        print("Embeddings Stored Successfully")
        print("=" * 70)

        print(
            f"Total Chunks Stored : "
            f"{self.vector_store.count_documents()}"
        )

    # ----------------------------------------------------
    # Complete Pipeline
    # ----------------------------------------------------

    def ingest(self):

        documents = self.load_documents()

        chunks = self.split_documents(documents)

        self.store_embeddings(chunks)

        print()

        print("=" * 70)
        print("Knowledge Base Ready")
        print("=" * 70)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    ingestion = KnowledgeBaseIngestion()

    ingestion.ingest()