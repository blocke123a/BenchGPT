"""
Chroma vector database utilities.
"""

import chromadb

from src.config import CHROMA_DB_DIR

# Database Creation
def build_database(chunks):

    client = chromadb.PersistentClient(
        path=str(CHROMA_DB_DIR)
    )

    try:

        collection = client.get_collection("basketball_rag")
    
    except:
    
        collection = client.create_collection("basketball_rag")

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(str(i))

        documents.append(chunk.text)

        embeddings.append(chunk.embedding)

        metadatas.append(chunk.metadata)

    batch_size = 1000

    for start in range(0, len(ids), batch_size):
    
        end = min(start + batch_size, len(ids))
    
        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )

        print(f"Added {end:,} / {len(ids):,}")

    print(f"Stored {len(chunks)} chunks.")

    return collection


# Load Existing Database
def load_database():

    client = chromadb.PersistentClient(
        path=str(CHROMA_DB_DIR)
    )

    return client.get_collection(
        "basketball_rag"
    )