# A kutatási célú ágentikus AI 2026-ban — Helyzetkép és iránymutató

**Magyar nyelvű AI-alapú interaktív tanulási platform kutatóknak**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Language: HU](https://img.shields.io/badge/Nyelv-Magyar-red.svg)](#)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-green.svg)](https://python.org)
[![React 19](https://img.shields.io/badge/React-19-61DAFB.svg)](https://react.dev)

> **AI-generált tartalom nyilatkozat**
>
> A tankönyv szövege (19 fejezet, ~100 000 szó) és az alkalmazás forráskódjának
> jelentős része **nagy nyelvi modellek (LLM-ek)** segítségével készült.
> A szöveg automatizált nyelvi ellenőrzésen esett át, de független szakmai
> lektoráláson nem. Az anyag **oktatástechnológiai demonstrációnak** tekintendő,
> nem pedig lektorált szakkönyvnek.

---

## Áttekintés

Interaktív tanulási platform egy 19 fejezetes magyar nyelvű egyetemi tankönyv köré építve, amely a tudományos kutatásban alkalmazható mesterséges intelligenciát mutatja be — a társalgási AI-tól az autonóm kutatási ágensekig. A könyv a precíziós mezőgazdaság, a hidroinformatika és a térinformatika szakterületi példáival illusztrált.

A platform lehetővé teszi a könyv olvasását, AI-alapú kérdezést a szöveghez, kvíz-alapú önellenőrzést, fogalmi térkép böngészését és szakterületi példák tanulmányozását.

### Számok

| Mutató | Érték |
|--------|-------|
| Fejezetek | 19 (HU) |
| Függelékek | 4 (előszó, környezet-beállítás, prompt-könyvtár, források, szójegyzék) |
| Összes szó | ~100 000 |
| Kvíz-kérdések | 209 (4 típus: feleletválasztós, igaz/hamis, kiegészítős, esszé) |
| RAG chunk-ok | 753 |
| Fogalmi gráf | 99 fogalom előfeltétel-kapcsolatokkal |
| Szakterületi példák | 42 doboz (🌾 mezőgazdaság, 💧 hidrológia, 🗺️ térinformatika) |
| Ábrák | 57 helykitöltő ábraprompttal |
| Referencia könyvek | 25 feldolgozott forrás |

---

## Funkciók

| Funkció | Leírás |
|---|---|
| **Könyvolvasó** | 19 fejezetes tankönyv markdown renderelővel, LaTeX egyenletekkel |
| **AI Chat** | RAG-alapú kérdés-válasz a tankönyv tartalmából |
| **Szövegkijelölés** | Bármely szövegrész kijelölése és kérdezés róla |
| **Kvízrendszer** | 209 előre generált kérdés, helyi értékelés, PDF export |
| **Fogalmi térkép** | Interaktív SVG függőségi gráf 19 fejezeten át |
| **Teljes szövegű keresés** | Szemantikus keresés kiemelt részletekkel |
| **Kereszthivatkozások** | Kattintható fejezethivatkozások a szövegben |
| **3 szintű tartalomjegyzék** | Oldalsáv: Rész / Fejezet / Alfejezet navigáció |
| **Sötét mód** | Világos/sötét témaváltás |
| **Mobil nézet** | Reszponzív elrendezés telefonra/tabletre |

---

## Könyvstruktúra (19 fejezet, 6 rész)

### I. rész: Ismerkedés az AI-val a kutatásban
1. Az AI forradalom a tudományos kutatásban
2. Társalgási AI — Az első kutatási partnered
3. AI a tudományos írásban és kommunikációban
4. AI-vel végzett adatelemzés — Kódolás nélkül

### II. rész: Mindennapi tudományos munka AI-val
5. AI kódolási asszisztensek — Kód írása programozás nélkül
6. AI-támogatott matematikai modellezés és szimuláció
7. Adat-pipeline-ok és automatizálás

### III. rész: Domain-specifikus AI
8. Vizuális programozás és munkafolyamat-tervezés
9. RAG — Tanítsuk meg az AI-t a saját adatainkra
10. Digitális ikrek — Valós rendszerek virtuális másolatai

### IV. rész: Ágentikus AI — Eszközökből munkatársak
11. Az AI ágensek megértése
12. AI ágensek építése kutatáshoz
13. Saját programok és eszközök készítése

### V. rész: Felelős AI-adoptáció vezetése
14. Az AI-val felszerelt kutatólabor
15. AI az egyetemen — Oktatás, tanulás és intézményi átalakulás
16. Etika, reprodukálhatóság és az AI jövője a tudományban

### VI. rész: Szakterületi alkalmazások
17. AI a precíziós mezőgazdaságban
18. AI a hidroinformatikában
19. AI a térinformatikában

### Függelékek
- A. függelék: AI kutatási környezet beállítása
- B. függelék: Prompt-könyvtár kutatóknak (50+ prompt)
- C. függelék: Források és további olvasmányok
- Szójegyzék (Glosszárium, 55+ fogalom)

---

## Gyors indítás

### Előfeltételek
- Python 3.11+ (conda ajánlott)
- Node.js 18+
- Gemini API kulcs ([aistudio.google.com](https://aistudio.google.com/apikey))

### Telepítés

```bash
# Klónozás
git clone https://github.com/Nagyhoho1234/agentic-ai-book.git
cd agentic-ai-book

# Conda környezet létrehozása
conda create -n aitutor python=3.11 -y
conda activate aitutor

# Backend függőségek
cd agentic-ai-tutor
pip install -r requirements.txt

# Gemini API kulcs beállítása
echo "GEMINI_API_KEY=your-key-here" > .env

# Fejezetek indexelése
python -m backend.rag.ingest

# Backend indítása
uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Frontend indítása (új terminálban)
cd frontend
npm install
npm run dev
```

A platform elérhető a `http://localhost:5173` címen.

---

## Projektstruktúra

```
agentic-ai-book/
├── chapters/hu/              # 19 fejezet + előszó + függelékek (magyar)
│   ├── ch00_eloszo.md
│   ├── ch01_ai_forradalom.md
│   ├── ...
│   ├── ch19_ai_terinformatika.md
│   ├── glossary.md
│   ├── appendix_a_kornyezet.md
│   ├── appendix_b_prompt_konyvtar.md
│   └── appendix_c_forrasok.md
├── agentic-ai-tutor/         # Interaktív webalkalmazás
│   ├── backend/              # FastAPI + Gemini + ChromaDB RAG
│   │   ├── agents/           # Szókratikus, kvíz, RAG ágensek
│   │   ├── rag/              # Chunker, retriever, concept graph
│   │   └── student/          # Tudáskövetés, munkamenet-kezelés
│   ├── frontend/             # React + Vite + Tailwind
│   └── data/                 # Kvíz-kérdések (209 db, 4 típus)
├── examples/                 # Futtatható kódpéldák
├── research/                 # Egyetemi kutatási jelentések (5 db)
├── BOOK_PLAN_v3.md           # Aktív könyvterv (forrástérképpel)
├── CLAUDE.md                 # Projekt-utasítások
├── CITATION.cff              # Zenodo hivatkozás
├── LICENSE                   # MIT licenc
└── README.md                 # Ez a fájl
```

---

## Szakterületi kontextus

A könyv a Debreceni Egyetem AI-átállásának támogatására készült, és három szakterületi alkalmazást mutat be részletesen:

| Szakterület | Fejezet | Forrás tankönyv |
|---|---|---|
| 🌾 Precíziós mezőgazdaság | 17. fejezet | [precagri](https://github.com/Nagyhoho1234/precagri) |
| 💧 Hidroinformatika | 18. fejezet | [maidment-hidroGIS](https://github.com/Nagyhoho1234/maidment-hidroGIS) |
| 🗺️ Térinformatika | 19. fejezet | [gis-konyv2025](https://github.com/Nagyhoho1234/gis-konyv2025) |

---

## Technológiai stack

| Komponens | Technológia |
|---|---|
| Frontend | React 19 + Vite + Tailwind CSS |
| Backend | FastAPI + Python 3.11 |
| LLM | Google Gemini (Flash/Pro) |
| Embedding | all-MiniLM-L6-v2 (sentence-transformers) |
| Vektor DB | ChromaDB |
| Adatbázis | SQLite (aiosqlite) |

---

## Hivatkozás

```bibtex
@software{feher2026agenticai,
  author       = {Fehér, Zsolt Zoltán},
  title        = {A kutatási célú ágentikus AI 2026-ban — Helyzetkép és iránymutató},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/Nagyhoho1234/agentic-ai-book},
  version      = {1.0.0}
}
```

---

## Licenc

MIT License — lásd [LICENSE](LICENSE).

---

## Készítette

**Fehér Zsolt Zoltán**
Debreceni Egyetem
ORCID: [0009-0007-6659-4197](https://orcid.org/0009-0007-6659-4197)

*Ez a könyv és platform AI-eszközök (Claude, ChatGPT, Codex) segítségével készült —
maga is demonstrációja annak a tézisnek, amelyet képvisel.*
