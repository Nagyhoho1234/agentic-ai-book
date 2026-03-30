"""Ingest Markdown chapters into ChromaDB with embeddings.

CLI usage: python -m scripts.ingest_book
"""

import json
from pathlib import Path
from typing import Optional

import chromadb
from rich.console import Console
from rich.progress import track
from sentence_transformers import SentenceTransformer

from backend.config import settings
from backend.rag.chunker import Chunk, parse_all_chapters

console = Console()

COLLECTION_NAME = "precagri_book"
COLLECTION_NAME_HU = "precagri_book_hu"


def get_chroma_client(persist_dir: Optional[Path] = None) -> chromadb.ClientAPI:
    """Get a persistent ChromaDB client."""
    if persist_dir is None:
        persist_dir = settings.resolve_path(settings.chroma_db_path)
    persist_dir.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(persist_dir))


def ingest_chapters(
    chapters_dir: Optional[Path] = None,
    chroma_dir: Optional[Path] = None,
) -> dict:
    """Parse all chapters, embed, and store in ChromaDB.

    Returns stats dict.
    """
    console.print("[bold blue]PrecAgri-Tutor Book Ingestion[/bold blue]")
    console.print()

    if chapters_dir is None:
        chapters_dir = Path(r"C:\precagri\chapters_en")

    # Parse chapters
    console.print(f"[yellow]Parsing chapters from {chapters_dir}...[/yellow]")
    chunks = parse_all_chapters(chapters_dir)
    console.print(f"  Total chunks: {len(chunks)}")

    if not chunks:
        console.print("[red]No chunks found! Check chapters_path in config.[/red]")
        return {"total_chunks": 0}

    # Load embedding model
    console.print(f"[yellow]Loading embedding model: {settings.embedding_model}[/yellow]")
    model = SentenceTransformer(settings.embedding_model)

    # Compute embeddings
    console.print("[yellow]Computing embeddings...[/yellow]")
    texts = [c.text for c in chunks]
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=32,
        normalize_embeddings=True,
    )

    # Store in ChromaDB
    console.print("[yellow]Storing in ChromaDB...[/yellow]")
    client = get_chroma_client(chroma_dir)

    # Delete existing collection if present
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Add in batches (ChromaDB has limits)
    batch_size = 500
    for i in track(range(0, len(chunks), batch_size), description="Inserting..."):
        batch = chunks[i : i + batch_size]
        batch_embeddings = embeddings[i : i + batch_size].tolist()

        collection.add(
            ids=[c.chunk_id for c in batch],
            embeddings=batch_embeddings,
            documents=[c.text for c in batch],
            metadatas=[c.metadata for c in batch],
        )

    # Save chunks as JSON backup
    chunks_dir_out = settings.resolve_path(Path("./data/chunks"))
    chunks_dir_out.mkdir(parents=True, exist_ok=True)
    chunks_json = [
        {
            "chunk_id": c.chunk_id,
            "text": c.text[:200] + "..." if len(c.text) > 200 else c.text,
            "chapter": c.chapter,
            "section": c.section,
            "subsection": c.subsection,
            "chunk_type": c.chunk_type,
            "token_count": c.token_count,
        }
        for c in chunks
    ]
    (chunks_dir_out / "chunks_index.json").write_text(
        json.dumps(chunks_json, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Compute stats
    stats = {
        "total_chunks": len(chunks),
        "chapters_processed": len(set(c.chapter for c in chunks)),
        "avg_tokens": round(sum(c.token_count for c in chunks) / len(chunks), 1),
        "max_tokens": max(c.token_count for c in chunks),
        "min_tokens": min(c.token_count for c in chunks),
        "by_type": {},
        "by_chapter": {},
    }

    for c in chunks:
        stats["by_type"][c.chunk_type] = stats["by_type"].get(c.chunk_type, 0) + 1
        stats["by_chapter"][c.chapter] = stats["by_chapter"].get(c.chapter, 0) + 1

    console.print()
    console.print("[bold green]Ingestion complete![/bold green]")
    console.print(f"  Chunks: {stats['total_chunks']}")
    console.print(f"  Chapters: {stats['chapters_processed']}")
    console.print(f"  Avg tokens/chunk: {stats['avg_tokens']}")
    console.print(f"  By type: {stats['by_type']}")
    console.print()

    return stats


def ingest_hungarian(
    chapters_dir: Optional[Path] = None,
    chroma_dir: Optional[Path] = None,
) -> dict:
    """Parse Hungarian chapters, embed, and store in a separate ChromaDB collection.

    Mirrors ingest_chapters() but uses the 'precagri_book_hu' collection
    and reads from chapters_hu/ by default.
    """
    console.print("[bold blue]PrecAgri-Tutor Hungarian Book Ingestion[/bold blue]")
    console.print()

    if chapters_dir is None:
        chapters_dir = Path(r"C:\precagri\chapters_hu")

    # Parse chapters
    console.print(f"[yellow]Parsing Hungarian chapters from {chapters_dir}...[/yellow]")
    chunks = parse_all_chapters(chapters_dir)
    console.print(f"  Total chunks: {len(chunks)}")

    if not chunks:
        console.print("[red]No chunks found! Check chapters_hu directory.[/red]")
        return {"total_chunks": 0}

    # Load embedding model
    console.print(f"[yellow]Loading embedding model: {settings.embedding_model}[/yellow]")
    model = SentenceTransformer(settings.embedding_model)

    # Compute embeddings
    console.print("[yellow]Computing embeddings...[/yellow]")
    texts = [c.text for c in chunks]
    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        batch_size=32,
        normalize_embeddings=True,
    )

    # Store in ChromaDB
    console.print("[yellow]Storing in ChromaDB (collection: precagri_book_hu)...[/yellow]")
    client = get_chroma_client(chroma_dir)

    # Delete existing HU collection if present
    try:
        client.delete_collection(COLLECTION_NAME_HU)
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME_HU,
        metadata={"hnsw:space": "cosine"},
    )

    # Add in batches
    batch_size = 500
    for i in track(range(0, len(chunks), batch_size), description="Inserting HU..."):
        batch = chunks[i : i + batch_size]
        batch_embeddings = embeddings[i : i + batch_size].tolist()

        collection.add(
            ids=[f"hu_{c.chunk_id}" for c in batch],
            embeddings=batch_embeddings,
            documents=[c.text for c in batch],
            metadatas=[c.metadata for c in batch],
        )

    # Save chunks as JSON backup
    chunks_dir_out = settings.resolve_path(Path("./data/chunks"))
    chunks_dir_out.mkdir(parents=True, exist_ok=True)
    chunks_json = [
        {
            "chunk_id": f"hu_{c.chunk_id}",
            "text": c.text[:200] + "..." if len(c.text) > 200 else c.text,
            "chapter": c.chapter,
            "section": c.section,
            "subsection": c.subsection,
            "chunk_type": c.chunk_type,
            "token_count": c.token_count,
        }
        for c in chunks
    ]
    (chunks_dir_out / "chunks_index_hu.json").write_text(
        json.dumps(chunks_json, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Compute stats
    stats = {
        "total_chunks": len(chunks),
        "chapters_processed": len(set(c.chapter for c in chunks)),
        "avg_tokens": round(sum(c.token_count for c in chunks) / len(chunks), 1),
        "max_tokens": max(c.token_count for c in chunks),
        "min_tokens": min(c.token_count for c in chunks),
        "by_type": {},
        "by_chapter": {},
    }

    for c in chunks:
        stats["by_type"][c.chunk_type] = stats["by_type"].get(c.chunk_type, 0) + 1
        stats["by_chapter"][c.chapter] = stats["by_chapter"].get(c.chapter, 0) + 1

    console.print()
    console.print("[bold green]Hungarian ingestion complete![/bold green]")
    console.print(f"  Chunks: {stats['total_chunks']}")
    console.print(f"  Chapters: {stats['chapters_processed']}")
    console.print(f"  Avg tokens/chunk: {stats['avg_tokens']}")
    console.print(f"  By type: {stats['by_type']}")
    console.print()

    return stats
