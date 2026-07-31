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

    print("Collection count:", _collection.count())

    return _collection

def extract_named_phrase(question: str) -> str | None:
    """
    Extract a likely multi-word proper name from the original question.

    Examples:
        "Scout Cooper Flagg" -> "Cooper Flagg"
        "Tell me about Michael Jordan" -> "Michael Jordan"
    """
    matches = re.findall(
        r"\b(?:[A-Z][a-zA-Z'.-]*)(?:\s+[A-Z][a-zA-Z'.-]*)+\b",
        question
    )

    ignored_starts = {
        "What Is",
        "Tell Me",
        "How Does",
        "Who Was",
        "Who Is",
        "Explain The"
    }

    matches = [
        match.strip()
        for match in matches
        if not any(
            match.startswith(prefix)
            for prefix in ignored_starts
        )
    ]

    return max(matches, key=len) if matches else None

# Retrieval
def retrieve(question, k=TOP_K):

    model = get_embedding_model()
    collection = get_collection()

    original_question = question.strip()

    normalized_question = original_question.lower()
    normalized_question = re.sub(
        r"[^\w\s]",
        "",
        normalized_question
    )
    normalized_question = " ".join(
        normalized_question.split()
    )

    query_embedding = model.encode(
        normalized_question,
        normalize_embeddings=True
    ).tolist()

    semantic_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )

    retrieved = []
    seen = set()

    # Exact-name fallback
    named_phrase = extract_named_phrase(original_question)

    if named_phrase:

        exact_results = collection.get(
            where_document={
                "$contains": named_phrase
            },
            limit=k,
            include=["documents", "metadatas"]
        )

        for document, metadata, chunk_id in zip(
            exact_results.get("documents", []),
            exact_results.get("metadatas", []),
            exact_results.get("ids", [])
        ):

            if chunk_id in seen:
                continue

            seen.add(chunk_id)

            retrieved.append(
                {
                    "text": document,
                    "metadata": {
                        **metadata,
                        # Exact text matches should pass the relevance gate.
                        "distance": 0.0,
                        "match_type": "exact"
                    }
                }
            )

    # Semantic results
    for chunk_id, document, metadata, distance in zip(
        semantic_results["ids"][0],
        semantic_results["documents"][0],
        semantic_results["metadatas"][0],
        semantic_results["distances"][0]
    ):

        if chunk_id in seen:
            continue

        seen.add(chunk_id)

        retrieved.append(
            {
                "text": document,
                "metadata": {
                    **metadata,
                    "distance": distance,
                    "match_type": "semantic"
                }
            }
        )

    # Preserve exact matches first, then nearest semantic matches.
    return retrieved[:k]


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

    Treat a question as time-sensitive only when it explicitly asks for current,
    latest, live, recent, or ongoing information, such as current standings,
    recent game results, current rankings, injuries, trades, or the most recent
    champion.
    
    A general question about a player, team, draft class, scouting report,
    historical season, rule, statistic, or strategy is not automatically
    time-sensitive. Answer those questions from the retrieved context whenever
    the context supports an answer.
    
    For genuinely time-sensitive questions, do not use outside knowledge. Explain
    that BenchGPT uses a static, curated knowledge base and cannot reliably provide
    current or live information.   
    
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

    if best_distance > 0.70:
        return (
            "I couldn't find enough relevant basketball information in my knowledge base to answer that question. Try asking about basketball rules, analytics, strategy, scouting, or NBA history.",
            [], False
        )

    prompt = build_prompt(question, chunks)
    print(best_distance)
    print(f"Using model: {LLM_MODEL}")
    
    answer = generate_answer(prompt)

    if "NO_RELEVANT_CONTEXT" in answer:
        return (
            "I couldn't find enough relevant basketball information in my knowledge base to answer that question. "
            "Try asking about basketball rules, analytics, strategy, scouting, or NBA history.",
            [],
            False
        )

    decline_phrases = [
        "I couldn't find enough relevant basketball information",
        "cannot reliably answer questions requiring current or live information",
        "does not contain information about the most recent",
        "additional information would be needed"
    ]
    
    show_sources = True
    
    for phrase in decline_phrases:
        if phrase.lower() in answer.lower():
            show_sources = False
            break

    return answer, chunks, show_sources

