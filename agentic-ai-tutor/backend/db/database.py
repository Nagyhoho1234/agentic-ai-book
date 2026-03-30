"""SQLite database setup and connection management."""

import aiosqlite
from pathlib import Path
from backend.config import settings

DB_PATH = settings.resolve_path(settings.sqlite_db_path)


async def get_db() -> aiosqlite.Connection:
    """Get an async SQLite connection."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = await aiosqlite.connect(str(DB_PATH))
    db.row_factory = aiosqlite.Row
    return db


async def init_db() -> None:
    """Create all tables if they don't exist."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(str(DB_PATH)) as db:
        # Rate limiter daily counts
        await db.execute("""
            CREATE TABLE IF NOT EXISTS rate_limits (
                model TEXT NOT NULL,
                date TEXT NOT NULL,
                request_count INTEGER DEFAULT 0,
                PRIMARY KEY (model, date)
            )
        """)

        # Response cache
        await db.execute("""
            CREATE TABLE IF NOT EXISTS response_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt_hash TEXT NOT NULL,
                prompt_text TEXT NOT NULL,
                response_text TEXT NOT NULL,
                model_used TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                access_count INTEGER DEFAULT 1
            )
        """)
        await db.execute("""
            CREATE INDEX IF NOT EXISTS idx_cache_hash ON response_cache(prompt_hash)
        """)

        # Student sessions
        await db.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id TEXT PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Knowledge tracing
        await db.execute("""
            CREATE TABLE IF NOT EXISTS knowledge_states (
                student_id TEXT NOT NULL,
                concept TEXT NOT NULL,
                p_mastery REAL DEFAULT 0.1,
                attempts INTEGER DEFAULT 0,
                correct INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (student_id, concept),
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        # Conversation history
        await db.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                agent TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        # API usage log
        await db.execute("""
            CREATE TABLE IF NOT EXISTS api_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT NOT NULL,
                prompt_tokens INTEGER,
                response_tokens INTEGER,
                cached INTEGER DEFAULT 0,
                agent TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        await db.commit()
