"""Socratic Agent: guides students through discovery via questions."""

from typing import Optional

from backend.models.gemini_client import gemini_client, LLMResponse
from backend.rag.retriever import retriever

SOCRATIC_SYSTEM_PROMPT = """You are a Socratic tutor for AI in scientific research. Instead of giving direct answers,
you guide students to discover the answer themselves through a series of carefully chosen questions.

Based on the textbook "Ágentikus AI Tudósoknak" (Agentic AI for Scientists) by Fehér Zsolt Zoltán:

Rules:
1. Start by asking a simpler, related question that builds toward understanding.
2. Acknowledge what the student already knows.
3. Break complex topics into smaller conceptual steps.
4. Use analogies from everyday life when helpful.
5. After 3-4 failed attempts to guide the student, provide the direct explanation.
6. Always reference specific chapters/sections from the textbook.
7. Be encouraging and patient.
8. Respond in Hungarian when the student writes in Hungarian.

Your response should contain:
- A guiding question OR a scaffolded explanation
- A hint (collapsed) that the student can reveal if stuck
- The concept being targeted
"""


async def guide_student(
    query: str,
    conversation_history: Optional[list[dict]] = None,
    attempt_count: int = 0,
) -> dict:
    """Guide a student through Socratic questioning.

    If attempt_count >= 3, switches to direct explanation.
    """
    # Retrieve relevant content
    chunks = retriever.retrieve(query=query, top_k=3)
    context = retriever.build_context(chunks)

    mode = "direct_explanation" if attempt_count >= 3 else "socratic_questioning"

    prompt_parts = [f"CONTEXT FROM TEXTBOOK:\n{context}\n"]

    if conversation_history:
        prompt_parts.append("CONVERSATION SO FAR:")
        for msg in conversation_history[-6:]:
            prompt_parts.append(f"  {msg.get('role', 'user')}: {msg.get('content', '')}")
        prompt_parts.append("")

    prompt_parts.append(f"STUDENT SAYS: {query}")
    prompt_parts.append(f"MODE: {mode}")
    prompt_parts.append(f"ATTEMPT: {attempt_count + 1}")

    if mode == "direct_explanation":
        prompt_parts.append("The student has struggled. Now give a clear, direct explanation.")
    else:
        prompt_parts.append("Ask a guiding question. Include a hidden hint.")

    prompt = "\n".join(prompt_parts)

    response: Optional[LLMResponse] = await gemini_client.generate(
        prompt=prompt,
        system_prompt=SOCRATIC_SYSTEM_PROMPT,
        complexity="medium",
    )

    if response is None:
        return {
            "response": "I'm having trouble connecting right now. Try re-reading the relevant section in the textbook.",
            "mode": "fallback",
            "sources": [],
        }

    return {
        "response": response.text,
        "mode": mode,
        "model_used": response.model_used,
        "sources": [
            {"chapter": c.chapter, "section": c.section}
            for c in chunks
        ],
    }
