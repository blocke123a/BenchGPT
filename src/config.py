"""
Configuration settings for the Basketball RAG project.
"""

from pathlib import Path

# Project Directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = PROJECT_ROOT / "documents"

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

CHROMA_DB_DIR = ARTIFACTS_DIR / "chroma_db"

# Embedding Model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# LLM
LLM_PROVIDER = "groq"

LLM_MODEL = "llama-3.1-8b-instant"

# Chunking
CHUNK_SIZE = 800

CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 6