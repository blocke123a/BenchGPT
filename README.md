# 🏀 BenchGPT: A Basketball Knowledge Assistant Powered by RAG
## Built by Blake Wood (http://www.linkedin.com/in/blake-wood-584120231/)
BenchGPT is a Retrieval-Augmented Generation (RAG) application designed to answer basketball questions using a curated knowledge base of basketball rules, analytics, strategy, scouting reports, and NBA history.

The goal of this project was to build an end-to-end machine learning application that combines modern NLP techniques, vector search, and large language models to create a domain-specific knowledge assistant.

Live App: https://benchgpt.streamlit.app

## Overview

Large language models are powerful, but they have several limitations:

- They often hallucinate information.
- Their knowledge may not include recent or specialized information.
- They do not naturally provide traceable sources.

BenchGPT addresses these challenges by grounding responses in a curated basketball knowledge base through Retrieval-Augmented Generation.

Instead of relying only on the language model's internal knowledge, BenchGPT:

1. Converts basketball documents into searchable vector embeddings.
2. Retrieves the most relevant passages for a user's question.
3. Provides those passages as context to an LLM.
4. Generates a response grounded in the retrieved information.
5. Displays the relevant source documents.


## Architecture

User Question -> Streamlit Application -> Question Embedding -> ChromaDB Vector Search -> Relevant Basketball Documents -> Prompt Construction -> Groq-hosted LLM
(Llama 3.1 8B Instant) -> Generated Response + Sources

## Technology Stack

### Application
- Python
- Streamlit

### Machine Learning / NLP
- Sentence Transformers
- BAAI/bge-small-en-v1.5 embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database
- ChromaDB

### Large Language Model
- Llama 3.1 8B Instant
- Hosted through Groq API

### Deployment
- Streamlit Community Cloud


# Data Collection

BenchGPT was built using a curated collection of basketball resources across five major categories:

## 📖 Rules
Examples:
- NBA Official Playing Rules
- FIBA Official Basketball Rules

## 📊 Analytics
Examples:
- Basketball statistics concepts
- Advanced metrics
- Player evaluation frameworks

## 🧠 Strategy
Examples:
- Offensive concepts
- Defensive schemes
- Coaching concepts

## 📝 Scouting
Examples:
- NBA draft scouting reports (2022-26)

## 🏆 NBA History
Examples:
- Player histories (NBA Top 75 Players)
- Team histories (select historical teams)
- Historical events

## Data Pipeline

The project uses a multi-stage data pipeline:
Raw Documents -> Document Processing -> Text Chunking -> Embedding Generation -> ChromaDB Vector Database -> RAG Application

### Document Processing

Documents are collected and converted into a consistent format before ingestion. The rules and a couple other documents are simply downloaded pdfs. Everything else was hand-picked and web-scraped using the Python library Trafilatura.

### Chunking

Documents are split into smaller sections to improve retrieval quality.

Current configuration:

- Chunk size: 800 tokens
- Chunk overlap: 100 tokens


### Embeddings

Each chunk is converted into a vector representation using BAAI/bge-small-en-v1.5.


These embeddings allow semantic search rather than simple keyword matching.


### Vector Database

ChromaDB stores:

- Document embeddings
- Original text chunks
- Metadata

Metadata includes:

- Document category
- Filename
- Source URL


# Retrieval Pipeline

When a user asks a question:

1. The question is converted into an embedding.
2. ChromaDB searches for semantically similar chunks.
3. Retrieved documents are filtered using similarity thresholds.
4. Relevant context is added to the LLM prompt.
5. The LLM generates a response.


## Retrieval Improvements

Several safeguards were added to improve reliability:

### Relevance Filtering

BenchGPT evaluates retrieval similarity scores before generating responses.

If no sufficiently relevant basketball context is found, the system declines to answer rather than hallucinate.

Example:

> "Tell me about the planet Venus"  (which my friend used to break BenchGPT during development)

Response:

> BenchGPT uses a curated basketball knowledge base and cannot provide information outside of basketball.


### Time-Dependent Question Handling

BenchGPT avoids answering questions that require current information, such as:

- Who won the most recent NBA Finals?
- Who are the best defenders right now?
- Current player rankings

Because the knowledge base is curated and static, these questions are explicitly declined.


### Source Grounding

Responses are generated using retrieved documents only, and relevant sources are displayed when available.


# Example Questions

Try asking:

- "What is drop coverage?"
- "Explain true shooting percentage."
- "Why were the 2014 Spurs successful?"
- "What is the scouting report on Cooper Flagg?"
- "How does FIBA differ from NBA rules?"
- "Explain Box Plus Minus."


# Limitations

BenchGPT is intentionally designed as a domain-specific basketball assistant.

Current limitations:

- It does not have live NBA data.
- It cannot answer current events reliably.
- Its knowledge depends on the documents included in the knowledge base.
- Retrieval quality depends on the available source material.

These limitations are intentional design choices to reduce hallucinations and improve answer reliability.


# Running Locally

## 1. Clone Repository

```bash
git clone https://github.com/blocke123a/BenchGPT.git

cd BenchGPT

## 2. Create Environment

Example using Conda:

conda create -n benchgpt python=3.11

conda activate benchgpt

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Add API Keys

Create:

.streamlit/secrets.toml

with:

GROQ_API_KEY="your_api_key_here"

## 5. Run Application
streamlit run app.py

# Future Improvements

Potential improvements include:

Adding live NBA statistics integration
Expanding historical documents
Improving retrieval ranking
Adding conversational memory
Adding user feedback loops
Adding automated document ingestion pipelines
Project Structure
BenchGPT/
│
├── app.py                 # Streamlit application
├── pipeline.py            # Data ingestion pipeline
├── requirements.txt
│
├── documents/             # Source documents
│
├── artifacts/
│   └── chroma_db/         # Persistent vector database
│
└── src/
    ├── embeddings.py      # Embedding generation
    ├── rag.py             # Retrieval and generation pipeline
    ├── config.py          # Configuration
    └── vector_database.py # ChromaDB interface
Author

Blake Wood

Data Scientist / Machine Learning Engineer / Basketball Fan
