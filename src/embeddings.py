"""
Embedding generation for the Basketball RAG project.
"""

from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL

# Embedding Model
_model = None


def load_embedding_model():

    global _model

    if _model is None:

        print("Loading embedding model...")

        _model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    return _model

# Embedding
def embed_chunks(chunks):

    model = load_embedding_model()

    texts = [chunk.text for chunk in chunks]

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    for chunk, embedding in zip(chunks, embeddings):

        chunk.embedding = embedding.tolist()

    return chunks