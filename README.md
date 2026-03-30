# A kutatási célú ágentikus AI 2026-ban — Helyzetkép és iránymutató
# Agentic AI for Scientific Research in 2026 — Status Report and Guidelines

**Hungarian-language AI-powered interactive learning platform for researchers**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19327532.svg)](https://doi.org/10.5281/zenodo.19327532)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: Hungarian](https://img.shields.io/badge/Language-Hungarian-red.svg)](#)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org)
[![React 19](https://img.shields.io/badge/React-19-61DAFB.svg)](https://react.dev)

> **AI-Generated Content Disclosure**
>
> Both the textbook content (19 chapters, ~100,000 words) and the majority of this
> application's source code were generated with the assistance of **large language models (LLMs)**.
> The text has been through automated language review but has not been independently
> peer-reviewed. This material should be treated as an **educational technology demonstration**,
> not as an authoritative reference.

---

## Overview

An interactive learning platform built around a 19-chapter **Hungarian-language** university
e-book covering AI for scientific research — from conversational AI to autonomous research
agents. The book includes domain-specific examples from precision agriculture,
hydroinformatics, and geoinformatics.

Students and researchers can read the book, ask AI-powered questions about specific passages,
take self-assessment quizzes, explore concept dependencies, and study domain-specific examples
— all through a bilingual web interface.

### Key Numbers

| Metric | Count |
|--------|-------|
| Chapters | 19 (Hungarian) |
| Appendices | 4 (setup guide, 50+ prompt library, resources, glossary) |
| Total words | ~100,000 |
| Quiz questions | 209 (4 types: MCQ, T/F, fill-blank, essay) |
| RAG chunks | 753 |
| Concept graph | 99 concepts with prerequisite links |
| Domain examples | 42 boxes (🌾 agriculture, 💧 hydrology, 🗺️ GIS) |
| Figure placeholders | 57 with image generation prompts |
| Reference books | 25 processed sources |

---

## Features

| Feature | Description |
|---|---|
| **Book Reader** | 19-chapter textbook with markdown rendering, LaTeX equations, tables |
| **AI Chat** | RAG-powered Q&A grounded in textbook content |
| **Text Selection** | Highlight any passage and ask questions about it |
| **Quiz System** | 209 pre-generated questions, local grading, PDF export |
| **Concept Map** | Interactive SVG dependency graph across all 19 chapters |
| **Full-Text Search** | Semantic search across all chapters with highlighted excerpts |
| **Cross-References** | Clickable chapter links in text ("1. fejezet" format) |
| **3-Level TOC** | Sidebar with Part / Chapter / Section navigation (numbered: 1.1, 1.1.1) |
| **Dark Mode** | Light/dark theme toggle |
| **Mobile Layout** | Responsive design for phone/tablet |

---

## Book Structure (19 Chapters, 6 Parts)

### Part I: Getting Started with AI in Research
1. The AI Revolution in Scientific Research
2. Conversational AI — Your First Research Partner
3. AI for Scientific Writing and Communication
4. AI-Powered Data Analysis — No Coding Required

### Part II: Everyday Scientific Work with AI
5. AI Coding Assistants — Writing Code Without Being a Programmer
6. AI-Assisted Mathematical Modeling and Simulation
7. Data Pipelines and Automation

### Part III: Domain-Specific AI
8. Visual Programming and Workflow Design
9. RAG — Teaching AI Your Own Data
10. Digital Twins — Virtual Replicas of Real Systems

### Part IV: Agentic AI — From Tools to Teammates
11. Understanding AI Agents
12. Building AI Agents for Research
13. Creating Your Own Programs and Tools

### Part V: Leading Responsible AI Adoption
14. The AI-Augmented Research Lab
15. AI in the University — Teaching, Learning, and Institutional Transformation
16. Ethics, Reproducibility, and the Future of AI in Science

### Part VI: Domain Applications
17. AI in Precision Agriculture
18. AI in Hydroinformatics
19. AI in Geoinformatics

### Appendices
- A: AI Research Environment Setup Guide
- B: Prompt Library for Researchers (50+ prompts)
- C: Resources and Further Reading
- Glossary (55+ terms with Hungarian explanations)

---

## Quick Start

### Prerequisites
- Python 3.11+ (conda recommended)
- Node.js 18+
- Gemini API key ([aistudio.google.com](https://aistudio.google.com/apikey))

### Installation

```bash
# Clone
git clone https://github.com/Nagyhoho1234/agentic-ai-book.git
cd agentic-ai-book

# Create conda environment
conda create -n aitutor python=3.11 -y
conda activate aitutor

# Install backend dependencies
cd agentic-ai-tutor
pip install -r requirements.txt

# Set Gemini API key
echo "GEMINI_API_KEY=your-key-here" > .env

# Index chapters into vector database
python -m backend.rag.ingest

# Start backend
uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Start frontend (new terminal)
cd frontend
npm install
npm run dev
```

The platform will be available at `http://localhost:5173`.

---

## Project Structure

```
agentic-ai-book/
├── chapters/hu/              # 19 chapters + preface + appendices (Hungarian)
│   ├── ch00_eloszo.md
│   ├── ch01_ai_forradalom.md
│   ├── ...
│   ├── ch19_ai_terinformatika.md
│   ├── glossary.md
│   ├── appendix_a_kornyezet.md
│   ├── appendix_b_prompt_konyvtar.md
│   └── appendix_c_forrasok.md
├── agentic-ai-tutor/         # Interactive web application
│   ├── backend/              # FastAPI + Gemini + ChromaDB RAG
│   │   ├── agents/           # Socratic, quiz, RAG agents
│   │   ├── rag/              # Chunker, retriever, concept graph (99 concepts)
│   │   └── student/          # Knowledge tracking, session management
│   ├── frontend/             # React + Vite + Tailwind
│   └── data/                 # Quiz questions (209, 4 types)
├── CITATION.cff              # Zenodo citation metadata
├── LICENSE                   # MIT License
└── README.md                 # This file
```

---

## Domain Context

This book was developed to support the AI transition at the **University of Debrecen** (Hungary),
aligned with Hungary's National AI Strategy 2025-2030. Three domain applications are presented
in detail, drawing from the author's existing textbooks:

| Domain | Chapter | Source Textbook |
|---|---|---|
| 🌾 Precision Agriculture | Ch. 17 | [precagri](https://github.com/Nagyhoho1234/precagri) |
| 💧 Hydroinformatics | Ch. 18 | [maidment-hidroGIS](https://github.com/Nagyhoho1234/maidment-hidroGIS) |
| 🗺️ Geoinformatics | Ch. 19 | [gis-tutor](https://github.com/Nagyhoho1234/gis-tutor) |

---

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | React 19 + Vite + Tailwind CSS |
| Backend | FastAPI + Python 3.11 |
| LLM | Google Gemini (Flash/Pro) |
| Embeddings | all-MiniLM-L6-v2 (sentence-transformers) |
| Vector DB | ChromaDB |
| Database | SQLite (aiosqlite) |

---

## Citation

```bibtex
@software{feher2026agenticai,
  author       = {Fehér, Zsolt Zoltán},
  title        = {Agentic AI for Scientific Research in 2026 — Status Report and Guidelines},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/Nagyhoho1234/agentic-ai-book},
  version      = {1.0.0}
}
```

---

## License

MIT License — see [LICENSE](LICENSE).

---

## Author

**Fehér Zsolt Zoltán**
University of Debrecen
ORCID: [0009-0007-6659-4197](https://orcid.org/0009-0007-6659-4197)

*This book and platform were developed with the assistance of AI tools (Claude, ChatGPT, Codex) —
itself a demonstration of the thesis it advocates.*
