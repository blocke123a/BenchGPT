"""
End-to-end pipeline for rebuilding the Basketball RAG database.
"""

from src.ingest import DocumentLoader
from src.chunking import chunk_documents
from src.embeddings import embed_chunks
from src.vector_database import build_database
from src.file_tracking import load_hashes, save_hashes

def main():

    print("=" * 60)
    print("Basketball RAG Pipeline")
    print("=" * 60)

    # Load Documents
    print("\nLoading documents...")

    known_hashes = load_hashes()

    loader = DocumentLoader()
    
    documents, current_hashes = loader.load_new_documents(
        known_hashes
    )
    
    if len(documents) == 0:
    
        print("Knowledge base already up to date.")
    
        exit()

    print(f"Found {len(documents)} new/updated documents.")

    # Chunk Documents
    print("\nChunking documents...")

    chunks = chunk_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    # Generate Embeddings
    print("\nGenerating embeddings...")

    chunks = embed_chunks(chunks)

    # Build Chroma Database
    print("\nBuilding vector database...")

    build_database(chunks)

    save_hashes(current_hashes)

    print("\nDone!")

    print("\nYou can now launch the app with:\n")

    print("streamlit run app.py")


if __name__ == "__main__":

    main()