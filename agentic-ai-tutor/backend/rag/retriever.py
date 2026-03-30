"""Retriever: query -> embed -> search ChromaDB -> build context."""

from dataclasses import dataclass
from typing import Optional

import chromadb
from sentence_transformers import SentenceTransformer

from backend.config import settings
from backend.rag.ingest import COLLECTION_NAME, COLLECTION_NAME_HU, get_chroma_client


@dataclass
class RetrievedChunk:
    """A chunk retrieved from the vector store."""
    chunk_id: str
    text: str
    chapter: int
    chapter_title: str
    section: str
    subsection: str
    chunk_type: str
    part: str
    score: float


class Retriever:
    """Retrieve relevant chunks from ChromaDB for a given query."""

    def __init__(self) -> None:
        self._model: Optional[SentenceTransformer] = None
        self._client: Optional[chromadb.ClientAPI] = None
        self._collections: dict[str, object] = {}

    def _get_model(self) -> SentenceTransformer:
        if self._model is None:
            self._model = SentenceTransformer(settings.embedding_model)
        return self._model

    def _get_collection(self, lang: str = "en"):
        """Get the ChromaDB collection for the given language."""
        if lang not in self._collections:
            if self._client is None:
                self._client = get_chroma_client()
            col_name = COLLECTION_NAME_HU if lang == "hu" else COLLECTION_NAME
            self._collections[lang] = self._client.get_collection(col_name)
        return self._collections[lang]

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        chapter_filter: Optional[int] = None,
        chunk_type_filter: Optional[str] = None,
        lang: str = "en",
    ) -> list[RetrievedChunk]:
        """Retrieve the most relevant chunks for a query.

        Args:
            query: The user's question.
            top_k: Number of chunks to return.
            chapter_filter: Optional chapter number to restrict search.
            chunk_type_filter: Optional chunk type to restrict search.
            lang: Language code ('en' or 'hu'). Selects the vector collection.

        Returns:
            List of RetrievedChunk sorted by relevance (best first).
        """
        model = self._get_model()
        collection = self._get_collection(lang=lang)

        # Embed the query
        query_embedding = model.encode(query, normalize_embeddings=True).tolist()

        # Build where filter
        where_filter = None
        conditions = []
        if chapter_filter is not None:
            conditions.append({"chapter": chapter_filter})
        if chunk_type_filter is not None:
            conditions.append({"chunk_type": chunk_type_filter})

        if len(conditions) == 1:
            where_filter = conditions[0]
        elif len(conditions) > 1:
            where_filter = {"$and": conditions}

        # Query ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_filter,
            include=["documents", "metadatas", "distances"],
        )

        # Parse results
        chunks: list[RetrievedChunk] = []
        if results and results["ids"] and results["ids"][0]:
            for i, chunk_id in enumerate(results["ids"][0]):
                meta = results["metadatas"][0][i] if results["metadatas"] else {}
                distance = results["distances"][0][i] if results["distances"] else 1.0
                # ChromaDB cosine distance: 0 = identical, 2 = opposite
                # Convert to similarity score: 1 - (distance / 2)
                similarity = 1.0 - (distance / 2.0)

                chunks.append(RetrievedChunk(
                    chunk_id=chunk_id,
                    text=results["documents"][0][i],
                    chapter=meta.get("chapter", 0),
                    chapter_title=meta.get("chapter_title", ""),
                    section=meta.get("section", ""),
                    subsection=meta.get("subsection", ""),
                    chunk_type=meta.get("chunk_type", ""),
                    part=meta.get("part", ""),
                    score=round(similarity, 4),
                ))

        return chunks

    def build_context(self, chunks: list[RetrievedChunk]) -> str:
        """Assemble retrieved chunks into a structured context string for the LLM."""
        if not chunks:
            return "No relevant content found in the textbook."

        parts = ["The following excerpts are from 'Precision Agriculture: From Principles to Practice' by Feher Zsolt Zoltan:\n"]

        for i, chunk in enumerate(chunks, 1):
            location = f"Chapter {chunk.chapter}: {chunk.chapter_title}"
            if chunk.section:
                location += f" > {chunk.section}"
            if chunk.subsection:
                location += f" > {chunk.subsection}"

            parts.append(f"--- Source {i} [{location}] (relevance: {chunk.score}) ---")
            parts.append(chunk.text)
            parts.append("")

        return "\n".join(parts)


# Singleton
retriever = Retriever()
