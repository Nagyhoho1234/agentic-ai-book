"""Orchestrator: classifies intent and routes to the appropriate agent."""

import re
from typing import Optional

import structlog

from backend.agents.rag_agent import answer_question
from backend.agents.quiz_agent import generate_quiz
from backend.agents.socratic_agent import guide_student
from backend.rag.concept_graph import get_concept_tree, get_concepts_for_chapter

logger = structlog.get_logger()


def classify_intent(query: str) -> str:
    """Classify user intent from their message. Returns agent name."""
    q = query.lower().strip()

    # Navigation / table of contents
    if re.search(r"table of contents|what topics|what chapters|list chapters|show me the topics|navigate", q):
        return "navigate"

    # Quiz requests
    if re.search(r"quiz|test me|test my|assessment|exam|practice questions|check my knowledge", q):
        return "quiz"

    # Socratic / confusion signals
    if re.search(r"i don.t understand|i.m confused|why does|how come|doesn.t make sense|help me understand|i.m stuck", q):
        return "socratic"

    # Default: RAG explanation
    return "rag"


async def handle_message(
    query: str,
    student_id: str = "default",
    conversation_history: Optional[list[dict]] = None,
    chapter_filter: Optional[int] = None,
    lang: str = "en",
) -> dict:
    """Route a student message to the appropriate agent.

    Returns a response dict with the agent's output plus routing metadata.
    """
    intent = classify_intent(query)

    await logger.ainfo("intent_classified", intent=intent, query=query[:80])

    if intent == "navigate":
        # Direct response — no LLM needed
        concept_tree = get_concept_tree()
        chapters = {}
        for key, concept in concept_tree.items():
            ch = concept["chapter"]
            if ch not in chapters:
                chapters[ch] = []
            chapters[ch].append({
                "key": key,
                "name": concept["name"],
                "section": concept["section"],
            })

        # Format as readable text
        lines = ["# Book Contents: Ágentikus AI Tudósoknak\n"]
        for ch_num in sorted(chapters.keys()):
            from backend.rag.chunker import CHAPTER_TITLES, CHAPTER_PARTS
            title = CHAPTER_TITLES.get(ch_num, f"Chapter {ch_num}")
            part = CHAPTER_PARTS.get(ch_num, "")
            lines.append(f"## Chapter {ch_num}: {title}")
            lines.append(f"*{part}*\n")
            for topic in chapters[ch_num]:
                lines.append(f"- **{topic['section']}** {topic['name']}")
            lines.append("")

        return {
            "answer": "\n".join(lines),
            "agent": "navigate",
            "sources": [],
            "cached": False,
        }

    elif intent == "quiz":
        # Extract topic from the query
        topic = re.sub(r"(quiz|test|me|on|about|my|knowledge|of|the|please)\s*", "", query, flags=re.IGNORECASE).strip()
        if not topic:
            topic = "AI agents in scientific research"

        result = await generate_quiz(
            topic=topic,
            num_questions=3,
            chapter_filter=chapter_filter,
        )
        result["agent"] = "quiz"
        return result

    elif intent == "socratic":
        # Count previous socratic attempts in conversation
        attempt_count = 0
        if conversation_history:
            for msg in conversation_history:
                if msg.get("agent") == "socratic":
                    attempt_count += 1

        result = await guide_student(
            query=query,
            conversation_history=conversation_history,
            attempt_count=attempt_count,
        )
        result["agent"] = "socratic"
        return result

    else:
        # Default: RAG
        result = await answer_question(
            query=query,
            conversation_history=conversation_history,
            chapter_filter=chapter_filter,
            lang=lang,
        )
        result["agent"] = "rag"
        return result
