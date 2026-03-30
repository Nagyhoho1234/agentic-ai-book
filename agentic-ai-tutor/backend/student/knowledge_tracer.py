"""Bayesian Knowledge Tracing (BKT) per concept.

Parameters:
- P(L0) = 0.1  (initial probability of mastery)
- P(T)  = 0.3  (probability of learning on each attempt)
- P(G)  = 0.2  (probability of guessing correctly)
- P(S)  = 0.1  (probability of slipping -- making an error despite mastery)
"""

from backend.db.database import get_db


# BKT parameters
P_L0 = 0.1   # Initial mastery probability
P_T = 0.3    # Learning/transition probability
P_G = 0.2    # Guess probability
P_S = 0.1    # Slip probability


def bkt_update(p_mastery: float, correct: bool) -> float:
    """Update mastery probability given an observation.

    Uses standard BKT update equations.
    """
    if correct:
        # P(L|correct) = P(L) * (1 - P(S)) / [P(L)*(1-P(S)) + (1-P(L))*P(G)]
        numerator = p_mastery * (1 - P_S)
        denominator = p_mastery * (1 - P_S) + (1 - p_mastery) * P_G
    else:
        # P(L|incorrect) = P(L) * P(S) / [P(L)*P(S) + (1-P(L))*(1-P(G))]
        numerator = p_mastery * P_S
        denominator = p_mastery * P_S + (1 - p_mastery) * (1 - P_G)

    p_mastery_given_obs = numerator / denominator if denominator > 0 else p_mastery

    # Apply learning transition
    p_mastery_new = p_mastery_given_obs + (1 - p_mastery_given_obs) * P_T

    return min(max(p_mastery_new, 0.0), 1.0)


async def update_knowledge(student_id: str, concept: str, correct: bool) -> float:
    """Update a student's mastery of a concept and return new mastery probability."""
    db = await get_db()
    try:
        # Ensure student exists
        await db.execute(
            "INSERT OR IGNORE INTO students (id) VALUES (?)", (student_id,)
        )

        # Get current state
        cursor = await db.execute(
            "SELECT p_mastery, attempts, correct FROM knowledge_states WHERE student_id = ? AND concept = ?",
            (student_id, concept),
        )
        row = await cursor.fetchone()

        if row:
            current_mastery = row[0]
            attempts = row[1]
            correct_count = row[2]
        else:
            current_mastery = P_L0
            attempts = 0
            correct_count = 0

        # BKT update
        new_mastery = bkt_update(current_mastery, correct)

        # Store
        await db.execute(
            """INSERT INTO knowledge_states (student_id, concept, p_mastery, attempts, correct, last_updated)
               VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
               ON CONFLICT(student_id, concept) DO UPDATE SET
                   p_mastery = ?,
                   attempts = attempts + 1,
                   correct = correct + ?,
                   last_updated = CURRENT_TIMESTAMP""",
            (student_id, concept, new_mastery, attempts + 1, correct_count + (1 if correct else 0),
             new_mastery, 1 if correct else 0),
        )
        await db.commit()
        return new_mastery
    finally:
        await db.close()


async def get_mastery_summary(student_id: str) -> dict:
    """Get mastery levels for all concepts a student has interacted with."""
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT concept, p_mastery, attempts, correct FROM knowledge_states WHERE student_id = ?",
            (student_id,),
        )
        rows = await cursor.fetchall()
        return {
            row[0]: {
                "mastery": round(row[1], 3),
                "attempts": row[2],
                "correct": row[3],
                "status": "mastered" if row[1] >= 0.8 else ("learning" if row[1] >= 0.4 else "novice"),
            }
            for row in rows
        }
    finally:
        await db.close()


async def get_weak_topics(student_id: str, threshold: float = 0.5) -> list[str]:
    """Get concepts where the student's mastery is below threshold."""
    db = await get_db()
    try:
        cursor = await db.execute(
            "SELECT concept FROM knowledge_states WHERE student_id = ? AND p_mastery < ? ORDER BY p_mastery ASC",
            (student_id, threshold),
        )
        rows = await cursor.fetchall()
        return [row[0] for row in rows]
    finally:
        await db.close()
