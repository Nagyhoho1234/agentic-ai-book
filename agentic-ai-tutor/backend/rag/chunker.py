"""Section-aware chunker for Markdown chapter files.

Splits .md chapters by heading structure, preserving metadata
(chapter number, part, section, subsection, topics).
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import tiktoken

from backend.config import settings

# Book part assignments (19 chapters)
CHAPTER_PARTS: dict[int, str] = {
    1: "I. rész: Ismerkedés az AI-val",
    2: "I. rész: Ismerkedés az AI-val",
    3: "I. rész: Ismerkedés az AI-val",
    4: "I. rész: Ismerkedés az AI-val",
    5: "II. rész: Mindennapi tudományos munka",
    6: "II. rész: Mindennapi tudományos munka",
    7: "II. rész: Mindennapi tudományos munka",
    8: "III. rész: Domain-specifikus AI",
    9: "III. rész: Domain-specifikus AI",
    10: "III. rész: Domain-specifikus AI",
    11: "IV. rész: Ágentikus AI",
    12: "IV. rész: Ágentikus AI",
    13: "IV. rész: Ágentikus AI",
    14: "V. rész: Felelős AI-adoptáció",
    15: "V. rész: Felelős AI-adoptáció",
    16: "V. rész: Felelős AI-adoptáció",
    17: "VI. rész: Szakterületi alkalmazások",
    18: "VI. rész: Szakterületi alkalmazások",
    19: "VI. rész: Szakterületi alkalmazások",
}

# Chapter titles
CHAPTER_TITLES: dict[int, str] = {
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


@dataclass
class Chunk:
    """A chunk of book text with full metadata."""
    text: str
    chapter: int
    chapter_title: str
    part: str
    section: str = ""
    subsection: str = ""
    chunk_type: str = "theory"  # theory, definition, example, exercise, figure_caption, code
    token_count: int = 0
    chunk_id: str = ""
    metadata: dict = field(default_factory=dict)


def count_tokens(text: str) -> int:
    """Count tokens using tiktoken (cl100k_base)."""
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def classify_chunk_type(text: str) -> str:
    """Heuristic classification of chunk content type."""
    lower = text.lower()

    if re.search(r"```python|```r|```sql|```bash", text):
        return "code"
    if re.search(r"\*\*figure \d+", lower):
        return "figure_caption"
    if "exercise" in lower or "problem" in lower and ("calculate" in lower or "compute" in lower):
        return "exercise"
    if re.search(r"\*\*definition\*\*|is defined as|we define", lower):
        return "definition"
    if re.search(r"for example|consider the case|a practical illustration", lower):
        return "example"
    return "theory"


def split_large_chunk(text: str, max_tokens: int, overlap_tokens: int) -> list[str]:
    """Split a text block that exceeds max_tokens at paragraph boundaries."""
    paragraphs = re.split(r"\n\n+", text)
    chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = count_tokens(para)
        if current_tokens + para_tokens > max_tokens and current:
            chunks.append("\n\n".join(current))
            # Keep last paragraph(s) as overlap
            overlap: list[str] = []
            overlap_count = 0
            for p in reversed(current):
                t = count_tokens(p)
                if overlap_count + t > overlap_tokens:
                    break
                overlap.insert(0, p)
                overlap_count += t
            current = overlap
            current_tokens = overlap_count

        current.append(para)
        current_tokens += para_tokens

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def parse_chapter(filepath: Path, chapter_num: int) -> list[Chunk]:
    """Parse a Markdown chapter file into chunks.

    Strategy:
    - Split at ## (section) and ### (subsection) headings
    - If a section exceeds max_tokens, split at paragraph boundaries
    - Each chunk carries full metadata
    """
    text = filepath.read_text(encoding="utf-8")

    # Remove \newpage directives
    text = text.replace("\\newpage", "").strip()

    # Remove HTML comments (figure prompts)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    chapter_title = CHAPTER_TITLES.get(chapter_num, f"{chapter_num}. fejezet")
    part = CHAPTER_PARTS.get(chapter_num, "Unknown")

    max_tokens = settings.chunk_max_tokens
    overlap_tokens = settings.chunk_overlap_tokens

    # Split by headings (## and ###)
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)

    sections: list[tuple[str, str, str]] = []  # (heading_level, heading_text, body)
    matches = list(heading_pattern.finditer(text))

    for i, match in enumerate(matches):
        level = match.group(1)
        heading = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()

        if body:  # Skip empty sections
            sections.append((level, heading, body))

    # If no headings found, treat entire text as one section
    if not sections:
        sections = [("#", chapter_title, text)]

    chunks: list[Chunk] = []
    current_section = ""
    current_subsection = ""
    chunk_counter = 0

    for level, heading, body in sections:
        # Track section hierarchy
        if level == "#":
            # Chapter-level heading, skip (title)
            continue
        elif level == "##":
            current_section = heading
            current_subsection = ""
        elif level == "###":
            current_subsection = heading

        # Check if body needs splitting
        tokens = count_tokens(body)
        if tokens > max_tokens:
            sub_texts = split_large_chunk(body, max_tokens, overlap_tokens)
        else:
            sub_texts = [body]

        for sub_text in sub_texts:
            chunk_counter += 1
            chunk = Chunk(
                text=sub_text,
                chapter=chapter_num,
                chapter_title=chapter_title,
                part=part,
                section=current_section,
                subsection=current_subsection,
                chunk_type=classify_chunk_type(sub_text),
                token_count=count_tokens(sub_text),
                chunk_id=f"ch{chapter_num:02d}_{chunk_counter:03d}",
                metadata={
                    "chapter": chapter_num,
                    "chapter_title": chapter_title,
                    "part": part,
                    "section": current_section,
                    "subsection": current_subsection,
                    "chunk_type": classify_chunk_type(sub_text),
                },
            )
            chunks.append(chunk)

    return chunks


def parse_all_chapters(chapters_dir: Optional[Path] = None) -> list[Chunk]:
    """Parse all 19 chapters and return all chunks."""
    if chapters_dir is None:
        chapters_dir = settings.resolve_path(settings.chapters_path)

    all_chunks: list[Chunk] = []

    import glob as _glob
    for ch_num in range(1, 20):
        # Try exact name first, then glob for ch01_*.md patterns
        filepath = chapters_dir / f"ch{ch_num:02d}.md"
        if not filepath.exists():
            pattern = str(chapters_dir / f"ch{ch_num:02d}_*.md")
            matches = sorted(_glob.glob(pattern))
            if matches:
                filepath = Path(matches[0])
        if filepath.exists():
            chapter_chunks = parse_chapter(filepath, ch_num)
            all_chunks.extend(chapter_chunks)

    return all_chunks
