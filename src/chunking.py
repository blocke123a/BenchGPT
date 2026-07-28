"""
Chunking utilities for the Basketball RAG project.
"""

from copy import deepcopy

from src.models import Chunk
from src.config import CHUNK_SIZE, CHUNK_OVERLAP


class Chunker:

    def __init__(
        self,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            document_chunks = self._chunk_document(document)

            chunks.extend(document_chunks)

        return chunks

    def _chunk_document(self, document):

        text = document.text

        chunks = []

        start = 0
        chunk_number = 0

        while start < len(text):
            end = start + self.chunk_size

            candidate = text[start:end]

            last_break = max(
                candidate.rfind("\n\n"),
                candidate.rfind(". "),
                candidate.rfind("? "),
                candidate.rfind("! ")
            )
            
            if last_break > self.chunk_size * 0.6:
                end = start + last_break + 1
                
            chunk_text = text[start:end]

            metadata = deepcopy(document.metadata)

            metadata["chunk_number"] = chunk_number

            chunks.append(
                Chunk(
                    text=chunk_text,
                    metadata=metadata
                )
            )

            chunk_number += 1

            start += self.chunk_size - self.chunk_overlap

        return chunks


# Convenience Function
def chunk_documents(documents):

    chunker = Chunker()

    return chunker.chunk_documents(documents)