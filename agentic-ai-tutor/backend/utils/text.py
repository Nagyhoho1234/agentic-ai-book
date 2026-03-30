"""Text processing utilities."""

import re


def clean_markdown(text: str) -> str:
    """Remove markdown formatting for plain-text operations."""
    text = re.sub(r"#{1,6}\s+", "", text)  # headings
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # bold
    text = re.sub(r"\*(.+?)\*", r"\1", text)  # italic
    text = re.sub(r"`(.+?)`", r"\1", text)  # inline code
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)  # code blocks
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)  # links
    text = re.sub(r"!\[.*?\]\(.+?\)", "", text)  # images
    return text.strip()


def truncate(text: str, max_chars: int = 500) -> str:
    """Truncate text at a word boundary."""
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars]
    last_space = truncated.rfind(" ")
    if last_space > max_chars * 0.8:
        truncated = truncated[:last_space]
    return truncated + "..."
