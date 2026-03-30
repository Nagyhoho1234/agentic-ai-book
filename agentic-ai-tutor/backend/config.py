"""Application configuration loaded from environment variables."""

from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """All settings for the PrecAgri-Tutor backend."""

    # Gemini API
    gemini_api_key: str = ""

    # Embedding model
    embedding_model: str = "all-MiniLM-L6-v2"

    # Paths (relative to project root)
    project_root: Path = Path(__file__).resolve().parent.parent
    chroma_db_path: Path = Path("./data/chroma_db")
    sqlite_db_path: Path = Path("./data/precagri_tutor.db")
    chapters_path: Path = Path("../chapters_en")
    chapters_path_hu: Path = Path("../chapters_hu")

    # Gemini model routing
    model_flash_lite: str = "gemini-2.5-flash-lite"
    model_flash: str = "gemini-2.5-flash"
    model_pro: str = "gemini-2.5-pro"

    # Rate limits (requests per day)
    rpd_flash_lite: int = 1000
    rpd_flash: int = 250
    rpd_pro: int = 100

    # Rate limits (requests per minute)
    rpm_flash_lite: int = 15
    rpm_flash: int = 10
    rpm_pro: int = 5

    # Cache settings
    cache_similarity_threshold: float = 0.92
    cache_ttl_days: int = 7
    cache_max_entries: int = 10000

    # RAG settings
    rag_top_k: int = 5
    chunk_max_tokens: int = 1500
    chunk_overlap_tokens: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def resolve_path(self, p: Path) -> Path:
        """Resolve a path relative to project root."""
        if p.is_absolute():
            return p
        return (self.project_root / p).resolve()


settings = Settings()
