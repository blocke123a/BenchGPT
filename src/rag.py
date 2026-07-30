"""
RAG pipeline.
"""

import os
import re

import streamlit as st
from groq import Groq, RateLimitError

@st.cache_resource
def get_client():

    return Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )


client = get_client()

from sentence_transformers import SentenceTransformer

from src.config import (
    EMBEDDING_MODEL,
    LLM_MODEL,
    TOP_K
)

from src.vector_database import load_database


# Load Resources
_embedding_model = None

_collection = None


def get_embedding_model():

    global _embedding_model

    if _embedding_model is None:

        _embedding_model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    return _embedding_model


def get_collection():

    global _collection

    if _collection is None:

        _collection = load_database()

    return _collection


# Retrieval
def retrieve(question, k=TOP_K):

    model = get_embedding_model()

    collection = get_collection()

    question = question.lower().strip()

    question = re.sub(r"[^\w\s]", "", question)

    query_embedding = model.encode(
        question,
        normalize_embeddings=True
    ).tolist()
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"]
    )

    retrieved = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):

        metadata["distance"] = distance

        retrieved.append(
            {
                "text": document,
                "metadata": metadata
            }
        )

    return retrieved


# Prompt Construction
def build_prompt(question, chunks):

    context = ""

    for i, chunk in enumerate(chunks, start=1):

        context += f"""
Category: {chunk['metadata']['category']}
File: {chunk['metadata']['filename']}

{chunk['text']}

--------------------------------------------------

"""
        
    prompt = f"""
    You are BenchGPT, a basketball knowledge assistant.
    
    Use the retrieved context as your primary source of information.
    
    If the context partially answers the question, combine the relevant pieces into a complete answer.
    
    You may make straightforward inferences that follow directly from the retrieved information.
    
    Do NOT invent basketball facts that are unsupported by the retrieved context.
    
    If the retrieved context truly does not contain enough information to answer confidently, say that additional information would be needed.
    
    When appropriate, explain concepts in simple basketball terms.
    
    If the question is about offensive concepts, answer with respect to offense. If the question is about defensive concepts, answer with respect to defense.
    
    If multiple retrieved documents present different viewpoints, explain both.

    Do not repeat phrases or sentences.

    The retrieved documents are provided for context only. Do not name the documents in your response.

    If the user asks time-sensitive questions like who won a recent game, do not answer from general world knowledge.

    Instead, explain that BenchGPT uses a curated basketball knowledge base and cannot reliably answer questions requiring current or live information.    
    
    Answer in 1-4 concise paragraphs.

    If the retrieved context is not relevant to the user's question, respond with ONLY: NO_RELEVANT_CONTEXT
    
    Retrieved Context:
    {context}
    
    Question:
    {question}

    Answer:
    """

    return prompt


# LLM
def generate_answer(prompt):
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=500,
            frequency_penalty=0.5,
            presence_penalty=0.2
        )
        return response.choices[0].message.content
    except RateLimitError:
        return (
            "BenchGPT is temporarily unavailable due to the AI service rate limit."
            " If you would like to use, please Venmo Blake Wood for API usage or come back tomorrow!"
        )


# Complete RAG Pipeline
def ask(question):

    chunks = retrieve(question)
    print("\nTop retrieved chunks:")
    for chunk in chunks:
        print(
            chunk["metadata"]["filename"],
            chunk["metadata"].get("distance")
        )

    best_distance = chunks[0]["metadata"]["distance"]

    if best_distance > 0.60:
        return (
            "I couldn't find enough relevant basketball information in my knowledge base to answer that question. Try asking about basketball rules, analytics, strategy, scouting, or NBA history.",
            []
        )

    prompt = build_prompt(question, chunks)
    print(best_distance)
    print(f"Using model: {LLM_MODEL}")
    
    answer = generate_answer(prompt)

    if answer.strip() == "NO_RELEVANT_CONTEXT":
        return (
            "I couldn't find enough relevant basketball information in my knowledge base to answer that question. Try asking about basketball rules, analytics, strategy, scouting, or NBA history.",
            []
        )

    return answer, chunks

