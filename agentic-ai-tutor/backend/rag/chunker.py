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

# Book part assignments (20 chapters)
CHAPTER_PARTS: dict[int, str] = {
    1: "Part I: Foundations",
    2: "Part I: Foundations",
    3: "Part I: Foundations",
    4: "Part II: Remote Sensing",
    5: "Part II: Remote Sensing",
    6: "Part II: Remote Sensing",
    7: "Part III: Field-Level Sensing and Positioning",
    8: "Part III: Field-Level Sensing and Positioning",
    9: "Part IV: Soil, Water, and Nutrients",
    10: "Part IV: Soil, Water, and Nutrients",
    11: "Part V: Implementation",
    12: "Part V: Implementation",
    13: "Part V: Implementation",
    14: "Part VI: Data, AI, and Decision Support",
    15: "Part VI: Data, AI, and Decision Support",
    16: "Part VI: Data, AI, and Decision Support",
    17: "Part VII: Economics, Livestock, and the Future",
    18: "Part VII: Economics, Livestock, and the Future",
    19: "Part VII: Economics, Livestock, and the Future",
    20: "Part VII: Economics, Livestock, and the Future",
}

# Chapter titles
CHAPTER_TITLES: dict[int, str] = {
    1: "Why Precision Agriculture?",
    2: "The Agricultural Landscape",
    3: "The Data Revolution in Farming",
    4: "Satellite and Aerial Remote Sensing",
    5: "Hyperspectral and Multispectral Imaging",
    6: "Proximal and In-Field Sensors",
    7: "Positioning and Navigation",
    8: "Understanding Soil Variability",
    9: "Water Management and Irrigation",
    10: "Nutrient Management",
    11: "Variable Rate Technology",
    12: "Crop Health Monitoring and Protection",
    13: "Yield Monitoring and Mapping",
    14: "Data Pipelines and Management",
    15: "Artificial Intelligence and Machine Learning in Agriculture",
    16: "Decision Support Systems",
    17: "Economics of Precision Agriculture",
    18: "Precision Livestock and Beyond",
    19: "The Future of Precision Agriculture",
    20: "Precision Agriculture in Hungary",
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

    chapter_title = CHAPTER_TITLES.get(chapter_num, f"Chapter {chapter_num}")
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
    """Parse all 20 chapters and return all chunks."""
    if chapters_dir is None:
        chapters_dir = settings.resolve_path(settings.chapters_path)

    all_chunks: list[Chunk] = []

    for ch_num in range(1, 21):
        filepath = chapters_dir / f"ch{ch_num:02d}.md"
        if filepath.exists():
            chapter_chunks = parse_chapter(filepath, ch_num)
            all_chunks.extend(chapter_chunks)

    return all_chunks
