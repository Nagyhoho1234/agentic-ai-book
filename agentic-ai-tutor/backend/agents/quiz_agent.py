"""Quiz Agent: generates adaptive quiz questions from book content."""

from typing import Optional

from backend.models.gemini_client import gemini_client, LLMResponse
from backend.rag.retriever import retriever

QUIZ_SYSTEM_PROMPT = """You are a quiz generator for a course on AI for scientists based on the textbook
"Ágentikus AI Tudósoknak" (Agentic AI for Scientists) by Fehér Zsolt Zoltán.

Generate quiz questions based ONLY on the provided textbook content.

Format your response as JSON with this structure:
{
  "questions": [
    {
      "type": "multiple_choice",
      "question": "the question text",
      "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
      "correct_answer": "B",
      "explanation": "brief explanation referencing the textbook",
      "concept": "concept_key",
      "difficulty": "easy|medium|hard"
    }
  ]
}

Question types to generate:
- multiple_choice: 4 options, one correct
- true_false: statement with True/False answer
- fill_in_blank: sentence with a key term blanked out

Rules:
- Questions must be answerable from the provided context
- Include the chapter/section reference in the explanation
- Mix different question types
- Difficulty should match the requested level
"""


async def generate_quiz(
    topic: str,
    num_questions: int = 3,
    difficulty: str = "medium",
    chapter_filter: Optional[int] = None,
) -> dict:
    """Generate quiz questions on a topic.

    Returns dict with questions and metadata.
    """
    # Retrieve relevant content
    chunks = retriever.retrieve(
        query=topic,
        top_k=5,
        chapter_filter=chapter_filter,
    )

    context = retriever.build_context(chunks)

    prompt = f"""CONTEXT FROM TEXTBOOK:
{context}

Generate {num_questions} quiz questions about "{topic}" at {difficulty} difficulty.
Mix question types (multiple choice, true/false, fill-in-the-blank).
Return valid JSON only.
"""

    response: Optional[LLMResponse] = await gemini_client.generate(
        prompt=prompt,
        system_prompt=QUIZ_SYSTEM_PROMPT,
        complexity="medium",
    )

    if response is None:
        return {
            "questions": [],
            "error": "Could not generate quiz (API quota may be exhausted).",
            "sources": [],
        }

    # Try to parse JSON from response
    import json
    import re

    text = response.text
    # Extract JSON block if wrapped in markdown code fence
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_match:
        text = json_match.group(1)

    try:
        quiz_data = json.loads(text)
    except json.JSONDecodeError:
        quiz_data = {"questions": [], "raw_response": response.text}

    quiz_data["model_used"] = response.model_used
    quiz_data["sources"] = [
        {"chapter": c.chapter, "section": c.section, "score": c.score}
        for c in chunks
    ]

    return quiz_data
