"""
Text Splitter

Splits LangChain documents into smaller chunks
for embedding and retrieval.

Author: Akksai Prathaan
Project: AI Interview System
"""

from typing import List

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from app.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextChunker:
    """
    Splits documents into overlapping chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ],
            length_function=len,
            is_separator_regex=False,
        )

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Split LangChain documents into chunks.

        Parameters
        ----------
        documents : List[Document]

        Returns
        -------
        List[Document]
        """

        chunks = self.splitter.split_documents(documents)

        print("=" * 60)
        print(f"Original Pages : {len(documents)}")
        print(f"Generated Chunks : {len(chunks)}")
        print("=" * 60)

        return chunks

    def split_text(
        self,
        text: str,
    ) -> List[str]:
        """
        Split plain text.

        Useful for testing.
        """

        chunks = self.splitter.split_text(text)

        return chunks


if __name__ == "__main__":

    from app.rag.document_loader import DocumentLoader

    loader = DocumentLoader()

    documents = loader.load_all_documents()

    splitter = TextChunker()

    chunks = splitter.split_documents(documents)

    print()

    print("=" * 60)
    print("FIRST CHUNK")
    print("=" * 60)

    print(chunks[0].page_content)

    print()

    print("=" * 60)
    print("METADATA")
    print("=" * 60)

    print(chunks[0].metadata)