"""FastAPI entry point for the AgenticAI-Tutor backend."""

from contextlib import asynccontextmanager

from typing import Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from backend.config import settings
from backend.db.database import init_db
from backend.models.rate_limiter import rate_limiter
from backend.models.cache import response_cache
from backend.models.gemini_client import gemini_client, LLMResponse
from backend.agents.orchestrator import handle_message
from backend.student.models import (
    ChatRequest, ChatResponse, QuizRequest, QuizAnswerRequest,
    QuotaStatus, CacheStats,
)
from backend.student.knowledge_tracer import update_knowledge, get_mastery_summary, get_weak_topics
from backend.student.session import save_message, get_conversation_history
from backend.rag.concept_graph import get_concept_tree, CONCEPT_GRAPH
from backend.rag.chunker import CHAPTER_TITLES, CHAPTER_PARTS


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database on startup."""
    await init_db()
    yield


app = FastAPI(
    title="AgenticAI-Tutor API",
    description="RAG-based tutoring system for 'Ágentikus AI Tudósoknak'",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:3000", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve book images as static files
from pathlib import Path as _Path
_images_dir = _Path(r"C:\agenticAIBook\images\book")
if _images_dir.exists():
    app.mount("/images", StaticFiles(directory=str(_images_dir)), name="book-images")


# ---- Health & Status ----

@app.get("/health")
async def health():
    return {"status": "ok", "service": "agenticai-tutor", "version": "0.1.0"}


@app.get("/quota-status", response_model=QuotaStatus)
async def quota_status():
    status = await rate_limiter.get_quota_status()
    return QuotaStatus(models=status)


@app.get("/cache-stats", response_model=CacheStats)
async def cache_stats():
    stats = await response_cache.get_stats()
    return CacheStats(**stats)


# ---- Chat ----

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint — routes to the appropriate agent."""
    # Get conversation history from DB if not provided
    history = request.conversation_history
    if history is None:
        history = await get_conversation_history(request.student_id, limit=10)

    # Save user message
    await save_message(request.student_id, "user", request.message)

    # Route and generate
    result = await handle_message(
        query=request.message,
        student_id=request.student_id,
        conversation_history=history,
        chapter_filter=request.chapter_filter,
        lang=request.lang,
    )

    answer = result.get("answer", result.get("response", ""))
    agent = result.get("agent", "rag")

    # Save assistant response
    await save_message(request.student_id, "assistant", answer, agent=agent)

    return ChatResponse(
        answer=answer,
        agent=agent,
        sources=result.get("sources", []),
        model_used=result.get("model_used", ""),
        cached=result.get("cached", False),
    )


# ---- Quiz ----

@app.post("/quiz")
async def quiz(request: QuizRequest):
    """Generate quiz questions on a topic."""
    from backend.agents.quiz_agent import generate_quiz
    return await generate_quiz(
        topic=request.topic,
        num_questions=request.num_questions,
        difficulty=request.difficulty,
        chapter_filter=request.chapter_filter,
    )


@app.post("/quiz/answer")
async def quiz_answer(request: QuizAnswerRequest):
    """Submit a quiz answer and update knowledge state."""
    new_mastery = await update_knowledge(
        request.student_id, request.concept, request.correct
    )
    return {"concept": request.concept, "new_mastery": round(new_mastery, 3)}


# ---- Student Progress ----

@app.get("/student/{student_id}/mastery")
async def mastery(student_id: str):
    return await get_mastery_summary(student_id)


@app.get("/student/{student_id}/weak-topics")
async def weak_topics(student_id: str):
    topics = await get_weak_topics(student_id)
    return {"weak_topics": topics}


@app.get("/student/{student_id}/history")
async def history(student_id: str):
    return await get_conversation_history(student_id, limit=50)


# ---- Book Content ----

@app.get("/concepts")
async def concepts():
    """Return the full concept dependency graph."""
    return get_concept_tree()


@app.get("/concept-graph")
async def concept_graph():
    """Return the concept graph in {nodes, edges} format for the ConceptMap UI."""
    nodes = {}
    edges = []
    for key, concept in CONCEPT_GRAPH.items():
        nodes[key] = {
            "name": concept.name,
            "chapter_num": concept.chapter,
            "section": concept.section,
            "description": concept.description,
        }
        for prereq in concept.prerequisites:
            edges.append({"from": prereq, "to": key})
    return {"nodes": nodes, "edges": edges}


@app.get("/toc")
async def table_of_contents():
    """Return the book table of contents."""
    toc = []
    for ch_num in sorted(CHAPTER_TITLES.keys()):
        toc.append({
            "chapter": ch_num,
            "title": CHAPTER_TITLES[ch_num],
            "part": CHAPTER_PARTS.get(ch_num, ""),
        })
    return {"chapters": toc}


CHAPTER_TITLES_HU: dict[int, str] = {
    1: "Az AI forradalom a tudományos kutatásban",
    2: "Társalgási AI — Az első kutatási partnered",
    3: "AI a tudományos írásban és kommunikációban",
    4: "AI-vel végzett adatelemzés — Kódolás nélkül",
    5: "AI kódolási asszisztensek — Kód írása programozás nélkül",
    6: "AI-támogatott matematikai modellezés és szimuláció",
    7: "Adat-pipeline-ok és automatizálás",
    8: "Vizuális programozás és munkafolyamat-tervezés",
    9: "RAG — Tanítsuk meg az AI-t a saját adatainkra",
    10: "Digitális ikrek: Valós rendszerek virtuális másolatai",
    11: "Az AI ágensek megértése",
    12: "AI ágensek építése kutatáshoz",
    13: "Saját programok és eszközök készítése",
    14: "Az AI-val felszerelt kutatólabor",
    15: "AI az egyetemen — Oktatás, tanulás és intézményi átalakulás",
    16: "Etika, reprodukálhatóság és az AI jövője a tudományban",
    17: "AI a precíziós mezőgazdaságban",
    18: "AI a hidroinformatikában",
    19: "AI a térinformatikában",
}


CHAPTER_PARTS_HU: dict[int, str] = {
    1: "I. rész: Ismerkedés az AI-val", 2: "I. rész: Ismerkedés az AI-val",
    3: "I. rész: Ismerkedés az AI-val", 4: "I. rész: Ismerkedés az AI-val",
    5: "II. rész: Mindennapi tudományos munka", 6: "II. rész: Mindennapi tudományos munka",
    7: "II. rész: Mindennapi tudományos munka",
    8: "III. rész: Domain-specifikus AI", 9: "III. rész: Domain-specifikus AI",
    10: "III. rész: Domain-specifikus AI",
    11: "IV. rész: Ágentikus AI", 12: "IV. rész: Ágentikus AI",
    13: "IV. rész: Ágentikus AI",
    14: "V. rész: Felelős AI-adoptáció", 15: "V. rész: Felelős AI-adoptáció",
    16: "V. rész: Felelős AI-adoptáció",
    17: "VI. rész: Szakterületi alkalmazások", 18: "VI. rész: Szakterületi alkalmazások",
    19: "VI. rész: Szakterületi alkalmazások",
}


@app.get("/book/chapters")
async def book_chapters(lang: str = Query("en")):
    """Return the list of book chapters with their concepts.

    Returns a flat list (not wrapped in {"chapters": ...}) so the frontend
    Flashcards component can iterate directly.  Each entry has both
    'chapter_num' / 'chapter_title' keys (used by Flashcards) and the
    legacy 'chapter' / 'title' aliases.
    """
    titles = CHAPTER_TITLES_HU if lang == "hu" else CHAPTER_TITLES
    ch_prefix = "fejezet" if lang == "hu" else "Chapter"
    chapters = []
    for ch_num in sorted(CHAPTER_TITLES.keys()):
        ch_concepts = [
            {"key": k, "name": c.name, "section": c.section}
            for k, c in CONCEPT_GRAPH.items() if c.chapter == ch_num
        ]
        numbered_title = f"{ch_num}. {ch_prefix}: {titles[ch_num]}"
        chapters.append({
            "chapter_num": ch_num,
            "chapter_title": numbered_title,
            "chapter": ch_num,
            "title": numbered_title,
            "part": (CHAPTER_PARTS_HU if lang == "hu" else CHAPTER_PARTS).get(ch_num, ""),
            "concepts": ch_concepts,
        })

    # Add appendices at the end
    appendices = [
        (0, "Preface" if lang == "en" else "Előszó", "ch00_preface.md"),
        (-1, "Exercises" if lang == "en" else "Gyakorlatok", "appendix_exercises.md"),
        (-2, "Glossary" if lang == "en" else "Szójegyzék", "appendix_glossary.md"),
        (-3, "Data Sources" if lang == "en" else "Adatforrások", "appendix_data_sources.md"),
        (-4, "Software Guide" if lang == "en" else "Szoftverismertető", "appendix_software.md"),
    ]
    app_part = "Appendices" if lang == "en" else "Függelékek"
    for app_num, app_title, _fname in appendices:
        chapters.append({
            "chapter_num": app_num,
            "chapter_title": app_title,
            "chapter": app_num,
            "title": app_title,
            "part": app_part,
            "concepts": [],
        })

    return chapters


APPENDIX_FILES = {
    0: "ch00_preface.md",
    -1: "appendix_exercises.md",
    -2: "appendix_glossary.md",
    -3: "appendix_data_sources.md",
    -4: "appendix_software.md",
}


@app.get("/book/chapter/{chapter_num}")
async def book_chapter(chapter_num: int, lang: str = Query("en")):
    """Return the full markdown content of a single chapter or appendix.

    Reads the .md file from chapters_en/ (en) or chapters_hu/ (hu),
    extracts heading-based TOC, and returns {chapter_num, chapter_title, part, markdown, toc}.
    """
    import re as _re
    from pathlib import Path

    # Handle appendices (chapter_num <= 0)
    if chapter_num in APPENDIX_FILES:
        app_filename = APPENDIX_FILES[chapter_num]
        if lang == "hu":
            app_dir = settings.resolve_path(settings.chapters_path_hu)
        else:
            app_dir = settings.resolve_path(settings.chapters_path)
        app_path = app_dir / app_filename
        if not app_path.exists() and lang == "hu":
            app_dir = settings.resolve_path(settings.chapters_path)
            app_path = app_dir / app_filename
        if app_path.exists():
            markdown = app_path.read_text(encoding="utf-8")
            markdown = markdown.replace("\\newpage", "").strip()
            markdown = markdown.replace(" -- ", " \u2014 ")
            title_match = _re.match(r"^#\s+(.+)$", markdown, _re.MULTILINE)
            title = title_match.group(1) if title_match else app_filename
            markdown = _re.sub(r"^#\s+.*\n*", "", markdown, count=1).strip()
            toc = []
            for m in _re.finditer(r"^(#{2,3})\s+(.+)$", markdown, _re.MULTILINE):
                level = len(m.group(1))
                heading_text = m.group(2).strip()
                slug = heading_text.lower()
                slug = _re.sub(r"[^\w\s-]", "", slug)
                slug = _re.sub(r"\s+", "-", slug)
                slug = slug.strip("-")[:60]
                toc.append({"level": level, "text": heading_text, "id": slug})
            return {"chapter_num": chapter_num, "chapter_title": title, "part": "", "markdown": markdown, "toc": toc}

    if chapter_num < 1 or chapter_num > 19:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Chapter {chapter_num} not found")

    titles = CHAPTER_TITLES_HU if lang == "hu" else CHAPTER_TITLES
    chapter_title = titles.get(chapter_num, f"Chapter {chapter_num}")
    part = CHAPTER_PARTS.get(chapter_num, "")

    # Try to read the markdown file — use chapters_hu/ for Hungarian
    if lang == "hu":
        chapters_dir = settings.resolve_path(settings.chapters_path_hu)
    else:
        chapters_dir = settings.resolve_path(settings.chapters_path)
    filepath = chapters_dir / f"ch{chapter_num:02d}.md"

    # Try glob pattern for ch01_*.md style filenames
    if not filepath.exists():
        import glob as _glob
        pattern = str(chapters_dir / f"ch{chapter_num:02d}_*.md")
        matches = sorted(_glob.glob(pattern))
        if matches:
            filepath = Path(matches[0])

    # If Hungarian version doesn't exist, fall back to English
    if not filepath.exists() and lang == "hu":
        chapters_dir = settings.resolve_path(settings.chapters_path)
        filepath = chapters_dir / f"ch{chapter_num:02d}.md"
        if not filepath.exists():
            import glob as _glob
            pattern = str(chapters_dir / f"ch{chapter_num:02d}_*.md")
            matches = sorted(_glob.glob(pattern))
            if matches:
                filepath = Path(matches[0])

    if not filepath.exists():
        # Fallback: reconstruct from chunks index
        chunks_index = settings.resolve_path(Path("./data/chunks/chunks_index.json"))
        markdown = ""
        if chunks_index.exists():
            import json
            with open(chunks_index, "r", encoding="utf-8") as f:
                all_chunks = json.load(f)
            ch_chunks = [c for c in all_chunks if c.get("chapter") == chapter_num]
            markdown = "\n\n".join(c["text"] for c in ch_chunks)
        if not markdown:
            markdown = f"# {chapter_title}\n\n*Chapter content not yet available.*"
    else:
        markdown = filepath.read_text(encoding="utf-8")
        # Strip \newpage LaTeX commands
        markdown = markdown.replace("\\newpage", "").strip()
        # Strip the chapter title heading (first # line) to avoid duplication
        markdown = _re.sub(r"^#\s+.*\n*", "", markdown, count=1).strip()
        # Convert -- (double dash) to proper em-dash
        markdown = markdown.replace(" -- ", " \u2014 ")

    # Convert <!-- FIGURE N.M: ... --> comments into placeholders
    def _figure_placeholder(m):
        body = m.group(1).strip()
        label_match = _re.search(r"FIGURE\s+(\d+)\.(\d+)", body)
        if label_match:
            label = f"Figure {label_match.group(1)}.{label_match.group(2)}"
        else:
            label = "Figure"
        return f'\n\n<div class="figure-placeholder">{label} — image not yet available</div>\n\n'
    markdown = _re.sub(r"<!--\s*(FIGURE.*?)-->", _figure_placeholder, markdown, flags=_re.DOTALL)

    # Build a table of contents from ## and ### headings
    toc = []
    for m in _re.finditer(r"^(#{2,3})\s+(.+)$", markdown, _re.MULTILINE):
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        slug = heading_text.lower()
        slug = _re.sub(r"[^\w\s-]", "", slug)
        slug = _re.sub(r"\s+", "-", slug)
        slug = slug.strip("-")[:60]
        toc.append({"level": level, "text": heading_text, "id": slug})

    # Prepend chapter number to title for display
    ch_prefix = "fejezet" if lang == "hu" else "Chapter"
    display_title = f"{chapter_num}. {ch_prefix}: {chapter_title}"

    return {
        "chapter_num": chapter_num,
        "chapter_title": display_title,
        "part": part,
        "markdown": markdown,
        "toc": toc,
    }


class SummaryRequest(BaseModel):
    """Request model for /book/summary endpoint."""
    chapter_num: int


@app.post("/book/summary")
async def book_summary(request: SummaryRequest):
    """Generate an AI summary of a book chapter.

    Uses the Gemini client to produce a concise summary of the chapter content.
    Falls back to a basic extractive summary if the API quota is exhausted.
    """
    chapter_num = request.chapter_num
    if chapter_num < 1 or chapter_num > 19:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail=f"Chapter {chapter_num} not found")

    chapter_title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")

    # Get chapter text from chunks
    from backend.rag.retriever import retriever
    chunks = retriever.retrieve(
        query=f"summary of chapter {chapter_num} {chapter_title}",
        top_k=8,
        chapter_filter=chapter_num,
    )

    chapter_text = "\n\n".join(c.text for c in chunks)

    if not chapter_text.strip():
        return {"summary": f"No content available for Chapter {chapter_num}: {chapter_title}."}

    # Try to generate AI summary
    prompt = (
        f"Summarize Chapter {chapter_num}: '{chapter_title}' from 'Ágentikus AI Tudósoknak'. "
        f"Write a concise summary (5-8 bullet points) covering the key concepts and takeaways. "
        f"Use markdown formatting.\n\n"
        f"Chapter content:\n{chapter_text[:4000]}"
    )

    try:
        response = await gemini_client.generate(prompt=prompt, complexity="medium")
        if response and response.text:
            return {"summary": response.text}
    except Exception:
        pass

    # Fallback: extractive summary from first few chunks
    fallback = f"**Chapter {chapter_num}: {chapter_title}**\n\n"
    for c in chunks[:3]:
        excerpt = c.text[:200].strip()
        if excerpt:
            fallback += f"- {excerpt}...\n"
    return {"summary": fallback}


@app.get("/book/summary/{chapter_num}")
async def book_summary_get(chapter_num: int):
    """GET variant of the summary endpoint for convenience."""
    request = SummaryRequest(chapter_num=chapter_num)
    return await book_summary(request)


class QuizGenerateRequest(BaseModel):
    """Request model for /quiz/generate endpoint."""
    chapter_nums: Optional[list[int]] = None
    chapter_num: Optional[int] = None
    num_questions: int = 20
    count: int = 3
    student_id: str = "default"
    question_types: Optional[list[str]] = None
    topic: Optional[str] = None
    difficulty: str = "medium"
    lang: str = "en"


def _load_question_bank(lang: str = "en"):
    """Load and cache the question bank from per-chapter JSON files."""
    import json as _json
    from pathlib import Path
    import glob as _glob

    cache_attr = f"_cache_{lang}"
    if not hasattr(_load_question_bank, cache_attr):
        bank = []
        subdir = "qbank_parts_hu" if lang == "hu" else "qbank_parts"
        parts_dir = settings.resolve_path(Path(f"./data/{subdir}"))
        # Fall back to English if Hungarian dir doesn't exist or is empty
        if not parts_dir.exists() or not list(parts_dir.glob("ch*.json")):
            parts_dir = settings.resolve_path(Path("./data/qbank_parts"))
        for f in sorted(_glob.glob(str(parts_dir / "ch*.json"))):
            fname = Path(f).name
            # Only load main chapter files (ch01.json), not supplements
            if "_" in fname.replace("ch", "", 1):
                # Include supplement files too (ch13_supp.json)
                pass
            try:
                with open(f, encoding="utf-8") as fh:
                    data = _json.load(fh)
                if isinstance(data, dict):
                    data = data.get("questions", [])
                # Ensure chapter_num is set from filename if missing
                ch_num_str = fname.replace(".json", "").replace("ch", "").split("_")[0]
                ch_num = int(ch_num_str)
                for q in data:
                    if "chapter_num" not in q:
                        q["chapter_num"] = ch_num
                    if "bank_type" not in q:
                        q["bank_type"] = q.get("type", "mcq")
                bank.extend(data)
            except Exception:
                pass
        setattr(_load_question_bank, cache_attr, bank)
    return getattr(_load_question_bank, cache_attr)


@app.post("/quiz/generate")
async def quiz_generate(request: QuizGenerateRequest):
    """Serve quiz questions from the pre-generated question bank.

    Falls back to LLM generation only if the bank has no matching questions.
    """
    import random

    bank = _load_question_bank(request.lang)

    # Determine chapters to filter
    ch_nums = request.chapter_nums or []
    if not ch_nums and request.chapter_num:
        ch_nums = [request.chapter_num]

    # Filter by chapter
    pool = [q for q in bank if q.get("chapter_num") in ch_nums] if ch_nums else list(bank)

    # Filter by question type if requested
    type_map = {"mcq": "mcq", "true_false": "true_false", "fill_blank": "fill_blank", "essay": "essay",
                "multiple_choice": "mcq", "true-false": "true_false", "fill-blank": "fill_blank"}
    if request.question_types:
        allowed = {type_map.get(t, t) for t in request.question_types}
        pool = [q for q in pool if q.get("type") in allowed or q.get("bank_type") in allowed]

    # Determine count
    n = request.num_questions if request.num_questions != 20 else max(request.count, request.num_questions)

    if not pool:
        return {"questions": [], "error": "No questions available for the selected chapters.", "sources": []}

    # Sample randomly
    selected = random.sample(pool, min(n, len(pool)))

    # Normalize field names for frontend compatibility
    questions = []
    for i, q in enumerate(selected):
        out = {
            "id": i,
            "type": q.get("type", "mcq"),
            "question": q.get("question", ""),
            "explanation": q.get("explanation", ""),
            "chapter_num": q.get("chapter_num"),
        }
        if q.get("type") == "mcq":
            out["options"] = q.get("options", [])
            out["correct_answer"] = q.get("correct", q.get("correct_answer", "A"))
        elif q.get("type") == "true_false":
            out["correct_answer"] = q.get("correct", True)
        elif q.get("type") == "fill_blank":
            out["correct_answer"] = q.get("correct", q.get("correct_answer", ""))
        elif q.get("type") == "essay":
            out["correct_answer"] = q.get("correct", q.get("correct_answer", ""))
        questions.append(out)

    return {"questions": questions, "sources": []}


class QuizEvaluateRequest(BaseModel):
    question: dict
    answer: str
    session_id: Optional[str] = None


@app.post("/quiz/evaluate")
async def quiz_evaluate(request: QuizEvaluateRequest):
    """Evaluate a quiz answer locally by comparing to the correct answer."""
    q = request.question
    answer = request.answer.strip()
    q_type = q.get("type", "mcq")
    correct_answer = q.get("correct_answer", "")
    explanation = q.get("explanation", "")

    if q_type == "mcq":
        is_correct = answer.upper() == str(correct_answer).upper()
        return {
            "correct": is_correct,
            "correct_answer": correct_answer,
            "explanation": explanation,
        }
    elif q_type == "true_false":
        # Normalize both to string comparison
        user_val = answer.lower() in ("true", "igaz", "1", "yes")
        correct_val = str(correct_answer).lower() in ("true", "igaz", "1", "yes")
        is_correct = user_val == correct_val
        return {
            "correct": is_correct,
            "correct_answer": "True" if correct_val else "False",
            "explanation": explanation,
        }
    elif q_type == "fill_blank":
        # Fuzzy match — case-insensitive, strip whitespace
        is_correct = answer.lower().strip() == str(correct_answer).lower().strip()
        return {
            "correct": is_correct,
            "correct_answer": correct_answer,
            "explanation": explanation,
        }
    elif q_type == "essay":
        # Essay: just return the model answer, no auto-grading
        return {
            "correct": True,
            "score": 50,
            "feedback": f"Model answer: {correct_answer}",
            "explanation": explanation,
        }
    else:
        return {"correct": False, "explanation": "Unknown question type"}


@app.get("/book/search")
async def book_search(q: str = Query(..., min_length=1), lang: str = Query("en")):
    """Search the book's vector store for relevant chunks.

    Returns results with 'chapter_num', 'chapter_title', 'section', and
    'excerpt' fields that the SearchBar component expects.
    """
    import re as _re
    from backend.rag.retriever import retriever
    chunks = retriever.retrieve(query=q, top_k=10, lang=lang)

    def _highlight(text: str, query: str) -> str:
        """Wrap query terms in <mark> tags for the frontend."""
        excerpt = text[:300] + "..." if len(text) > 300 else text
        for word in query.split():
            if len(word) >= 2:
                excerpt = _re.sub(
                    f"({_re.escape(word)})",
                    r"<mark>\1</mark>",
                    excerpt,
                    flags=_re.IGNORECASE,
                )
        return excerpt

    return {
        "query": q,
        "results": [
            {
                "chunk_id": c.chunk_id,
                "chapter_num": c.chapter,
                "chapter": c.chapter,
                "chapter_title": c.chapter_title,
                "section": c.section,
                "subsection": c.subsection,
                "chunk_type": c.chunk_type,
                "score": c.score,
                "excerpt": _highlight(c.text, q),
                "preview": c.text[:300] + "..." if len(c.text) > 300 else c.text,
            }
            for c in chunks
        ],
    }


# ---- Test endpoint ----

@app.get("/test-generate")
async def test_generate(prompt: str = "What are AI agents in scientific research?"):
    """Test Gemini API connectivity."""
    response: LLMResponse | None = await gemini_client.generate(
        prompt=prompt, complexity="low"
    )
    if response:
        return {
            "text": response.text,
            "model_used": response.model_used,
            "prompt_tokens": response.prompt_tokens,
            "response_tokens": response.response_tokens,
        }
    return {"error": "No response — check API key and quota."}
