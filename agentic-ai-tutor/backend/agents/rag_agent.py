"""RAG Agent: retrieves book content and generates grounded answers."""

import re
from typing import Optional

import structlog

from backend.models.gemini_client import gemini_client, LLMResponse
from backend.models.cache import response_cache
from backend.rag.retriever import retriever, RetrievedChunk

logger = structlog.get_logger()

SYSTEM_PROMPT = """You are a precision agriculture tutor. You help students learn from the textbook
"Precision Agriculture: From Sensors to Decisions" by Feher Zsolt Zoltan.

Rules:
1. Answer based ONLY on the provided context from the textbook.
2. If the context doesn't contain the answer, say so honestly: "The textbook doesn't cover this topic in the excerpts I found."
3. Reference the chapter and section when explaining (e.g., "As discussed in Chapter 8, Section 8.1...").
4. Use examples from the textbook when available.
5. Be clear and pedagogical — the student is learning.
6. When mathematical formulas appear in the context, explain them step by step.
7. Keep answers focused and well-structured. Use markdown formatting.
"""


def estimate_complexity(query: str) -> str:
    """Heuristic to estimate query complexity for model routing."""
    query_lower = query.lower()

    # High complexity: multi-concept, comparison, synthesis
    high_signals = ["compare", "difference between", "how does.*relate", "synthesize",
                    "evaluate", "analyze", "pros and cons", "advantages and disadvantages",
                    "explain the relationship", "integrate"]
    if any(re.search(pat, query_lower) for pat in high_signals):
        return "high"

    # Low complexity: simple lookups, definitions
    low_signals = ["what is", "define", "what does.*stand for", "list",
                   "who is", "when was", "where is", "name the"]
    if any(re.search(pat, query_lower) for pat in low_signals):
        return "low"

    # Default: medium
    return "medium"


async def answer_question(
    query: str,
    conversation_history: Optional[list[dict]] = None,
    chapter_filter: Optional[int] = None,
    lang: str = "en",
) -> dict:
    """Answer a question using RAG over the book content.

    Returns dict with:
        - answer: the generated text
        - sources: list of source chunks used
        - model_used: which Gemini model was used
        - cached: whether the answer came from cache
    """

    # Check cache first
    cached_response = await response_cache.get(query)
    if cached_response:
        return {
            "answer": cached_response,
            "sources": [],
            "model_used": "cache",
            "cached": True,
        }

    # Retrieve relevant chunks from the appropriate language collection
    chunks = retriever.retrieve(
        query=query,
        top_k=5,
        chapter_filter=chapter_filter,
        lang=lang,
    )

    # Build context from retrieved chunks
    context = retriever.build_context(chunks)

    # Build prompt with conversation history
    prompt_parts = [f"CONTEXT FROM TEXTBOOK:\n{context}\n"]

    if conversation_history:
        prompt_parts.append("RECENT CONVERSATION:")
        for msg in conversation_history[-5:]:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            prompt_parts.append(f"  {role}: {content}")
        prompt_parts.append("")

    prompt_parts.append(f"STUDENT QUESTION: {query}")
    prompt = "\n".join(prompt_parts)

    # Route to appropriate model
    complexity = estimate_complexity(query)

    # Generate answer
    response: Optional[LLMResponse] = await gemini_client.generate(
        prompt=prompt,
        system_prompt=SYSTEM_PROMPT,
        complexity=complexity,
    )

    if response is None:
        # Fallback: return the raw context
        fallback = "I'm unable to generate an answer right now (API quota may be exhausted). "
        fallback += "Here are the most relevant excerpts from the textbook:\n\n"
        for chunk in chunks[:3]:
            fallback += f"**Chapter {chunk.chapter}: {chunk.section}**\n{chunk.text[:500]}...\n\n"
        return {
            "answer": fallback,
            "sources": [_chunk_to_source(c) for c in chunks],
            "model_used": "fallback",
            "cached": False,
        }

    # Cache the response
    await response_cache.put(query, response.text, response.model_used)

    return {
        "answer": response.text,
        "sources": [_chunk_to_source(c) for c in chunks],
        "model_used": response.model_used,
        "cached": False,
    }


def _chunk_to_source(chunk: RetrievedChunk) -> dict:
    """Convert a RetrievedChunk to a source reference dict."""
    return {
        "chunk_id": chunk.chunk_id,
        "chapter": chunk.chapter,
        "chapter_title": chunk.chapter_title,
        "section": chunk.section,
        "subsection": chunk.subsection,
        "score": chunk.score,
        "preview": chunk.text[:150] + "..." if len(chunk.text) > 150 else chunk.text,
    }
