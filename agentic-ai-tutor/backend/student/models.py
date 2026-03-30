"""Pydantic models for API request/response shapes."""

from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    """Incoming chat message from the student."""
    message: str
    student_id: str = "default"
    session_id: Optional[str] = None  # alias for student_id
    chapter_filter: Optional[int] = None
    lang: str = "en"
    conversation_history: Optional[list[dict]] = None

    def model_post_init(self, __context) -> None:
        """If session_id is provided but student_id is default, use session_id."""
        if self.session_id and self.student_id == "default":
            self.student_id = self.session_id


class ChatResponse(BaseModel):
    """Response sent back to the student."""
    answer: str
    agent: str = "rag"
    sources: list[dict] = Field(default_factory=list)
    model_used: str = ""
    cached: bool = False


class QuizRequest(BaseModel):
    """Request for quiz generation."""
    topic: str
    num_questions: int = 3
    difficulty: str = "medium"
    chapter_filter: Optional[int] = None


class QuizAnswerRequest(BaseModel):
    """Student's quiz answer submission."""
    student_id: str = "default"
    concept: str
    correct: bool


class QuotaStatus(BaseModel):
    """API quota status."""
    models: dict


class CacheStats(BaseModel):
    """Response cache statistics."""
    entries: int
    total_hits: int
    max_entries: int
