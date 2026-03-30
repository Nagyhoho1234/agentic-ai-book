"""Session management for student conversations."""

from backend.db.database import get_db


async def save_message(student_id: str, role: str, content: str, agent: str = "") -> None:
    """Save a conversation message to the database."""
    db = await get_db()
    try:
        await db.execute(
            "INSERT OR IGNORE INTO students (id) VALUES (?)", (student_id,)
        )
        await db.execute(
            "INSERT INTO conversations (student_id, role, content, agent) VALUES (?, ?, ?, ?)",
            (student_id, role, content, agent),
        )
        await db.execute(
            "UPDATE students SET last_active = CURRENT_TIMESTAMP WHERE id = ?",
            (student_id,),
        )
        await db.commit()
    finally:
        await db.close()


async def get_conversation_history(student_id: str, limit: int = 10) -> list[dict]:
    """Get recent conversation history for a student."""
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT role, content, agent FROM conversations WHERE student_id = ? ORDER BY created_at DESC LIMIT ?",
            (student_id, limit),
        )
        rows = await cursor.fetchall()
        # Reverse to get chronological order
        return [{"role": row[0], "content": row[1], "agent": row[2]} for row in reversed(rows)]
    finally:
        await db.close()
