# NASA LLM Cookbook for Open Science — Analysis

## Repository Structure

```
LLM-cookbook-for-open-science/
├── README.md              # Comprehensive guide: prompt engineering, LangFlow, LangChain, fine-tuning
├── chat-examples/         # 9 prompt pattern templates with science examples
├── code/                  # 11 Python modules: agents, chains, tools, embeddings
├── data/                  # Environmental Justice datasets, GCMD keywords, policies
├── notebooks/             # 7 Jupyter notebooks (core hands-on material)
├── images/                # Setup screenshots
└── docs-presentations/    # Empty placeholder
```

---

## Content Summary

The cookbook covers **4 major topics** at increasing complexity:

| Level | Topic | Assets |
|-------|-------|--------|
| 1. Beginner | Prompt Engineering for Science | 9 chat-examples, README patterns |
| 2. Intermediate | RAG Prototyping with LangFlow | OSDR chatbot, evaluation notebook |
| 3. Intermediate-Advanced | LangChain Agents for Data Discovery | 2 ReACT agent notebooks, agent code |
| 4. Advanced | Fine-Tuning Encoder/Decoder Models | 3 EJ notebooks, training pipeline |

---

## Notebooks Analysis

### 1. Chat-with-mDGF.ipynb — Document QA with Prompt Patterns
- **Purpose:** Chat with NASA's Modern Data Governance Framework document
- **Techniques:** LangChain ConversationChain, Azure OpenAI GPT-4-turbo, combined prompt patterns (Persona + Recipe + Output Automator)
- **Complexity:** Beginner-Intermediate
- **Key lesson:** How to make an LLM "chat with" any reference document using conversation memory
- **Adaptability:** Any domain with governance frameworks, SOPs, regulatory documents

### 2. EJ_classify.ipynb — Text Classification Comparison
- **Purpose:** Classify Environmental Justice datasets into 8 climate indicator categories
- **Techniques:** HuggingFace fine-tuned DistilBERT vs. GPT-3.5 zero-shot vs. few-shot
- **Complexity:** Intermediate
- **Key lesson:** Fine-tuned DistilBERT: 96% accuracy at 69 samples/sec; GPT-3.5 zero-shot: 54% at 2 samples/sec; few-shot: 62%
- **Adaptability:** Any labeled text classification task (species ID, medical records, geological samples)

### 3. EJ_extractions.ipynb — Structured Metadata Extraction + 3-Tier Evaluation
- **Purpose:** Extract structured metadata from EJ dataset web pages; compare base vs. fine-tuned GPT-3.5
- **Techniques:** Pydantic schema validation, OpenAI function calling via `instructor`, BERTScore, three-tier evaluation (programmatic + LLM-as-judge + human)
- **Complexity:** Advanced
- **Key lesson:** How to define extraction schemas and build rigorous multi-level evaluation
- **Adaptability:** Any metadata extraction from unstructured text (clinical trials, specimen records, repository pages)

### 4. EJ_finetuning.ipynb — OpenAI Fine-Tuning Pipeline
- **Purpose:** Prepare training data and fine-tune GPT-3.5-turbo for metadata extraction
- **Techniques:** JSONL training format, OpenAI fine-tuning API, web scraping + NLP preprocessing
- **Complexity:** Intermediate
- **Key lesson:** Even ~40 training examples can produce useful fine-tuned models
- **Adaptability:** Universal pattern: define schema → gather examples → format JSONL → fine-tune → deploy

### 5. OSDR-evaluation.ipynb — RAG System Evaluation Framework
- **Purpose:** Evaluate retrieval quality AND answer quality of a RAG QA system for space biology
- **Techniques:** BERTScore, METEOR, ROUGE metrics; keyword + semantic retrieval recall; parametric sweep over top-k and thresholds
- **Complexity:** Advanced
- **Key lesson:** Systematic RAG evaluation beyond "does the answer look right" — retrieval recall vs. answer quality are independent dimensions
- **Adaptability:** Any RAG-based QA system (medical literature, legal documents, materials science)

### 6. langchain-react-astro.ipynb — Multi-Tool Astronomy Agent
- **Purpose:** ReACT agent chaining SIMBAD, SkyView, NASA ADS, Exoplanet Archive for natural-language astronomical queries
- **Techniques:** LangChain custom agent, astroquery, astropy, PandasAI, ReACT Thought/Action/Observation loop
- **Complexity:** Advanced
- **Key lesson:** How to wrap existing scientific Python libraries as LLM-callable tools and orchestrate them
- **Adaptability:** Blueprint for any domain with multiple data sources (geology: mineral DBs + geochemical APIs; biology: UniProt + PDB + PubMed)

### 7. langchain-react-cmr.ipynb — Natural Language → API Query Agent
- **Purpose:** Convert natural-language Earth science requests into valid CMR API queries with geocoding and temporal parsing
- **Techniques:** LangChain custom agent, OpenCage Geocoder, custom DatetimeChain (LLM-as-tool), CMR query construction
- **Complexity:** Intermediate-Advanced
- **Key lesson:** Using one LLM call as a "tool" within a larger agent; deploying agents as serverless APIs
- **Adaptability:** Any scientific data catalog with a search API (GBIF, Materials Project, Copernicus CDS)

---

## Prompt Patterns for Science (9 patterns)

| Pattern | Purpose | Science Example |
|---------|---------|-----------------|
| **Recipe** | Fill in missing workflow steps | "Preprocess Landsat 8 data — I know steps A,B,C — fill in the rest" |
| **Output Automator** | Generate executable scripts from descriptions | "Script to compile weekly seismic reports from USGS, earthquakes > 4.0, output CSV" |
| **Persona** | Adopt expert perspective | "Respond as an expert astrophysicist about gravitational waves" |
| **Flipped Interaction** | LLM asks questions (Socratic method) | "Ask me questions about star formation to help me learn" |
| **Question Refinement** | Sharpen vague questions | "Refine my question about lightning focusing on ice particles" |
| **Alternative Approach** | Broaden methodological awareness | "Different approaches to detecting exoplanets" |
| **Cognitive Verifier** | Decompose complex questions | "Break down 'what happens during a solar eclipse' into subquestions" |
| **Fact Check List** | Make assumptions explicit and verifiable | "List facts your answer depends on that should be fact-checked" |
| **Context Manager** | Focus/limit LLM scope | "Only discuss gravitational lensing, ignore transit method" |

---

## Code Architecture

The Python codebase implements a **complete RAG pipeline for scientific data discovery**:

```
Natural Language Query
    ↓
agent.py (ReACT agent loop)
    ↓
chains.py (DatetimeChain, QAChain, SummarizeChain)
    ↓
prompting_tools.py (BoundingBoxFinder, CMRQuery, GCMDKeywordSearch)
    ↓
gpt_embedder.py (semantic keyword matching via OpenAI embeddings)
    ↓
cmr_connector.py (orchestrator: multi-reader QA with evidence selection)
    ↓
Structured Answer + Evidence + Source Attribution
```

**Key code files:**
- `agent.py` — Custom ReACT agent with prompt template + output parser
- `chains.py` — 6 LLM chains: datetime extraction, QA, summarization, evidence selection
- `cmr_connector.py` — High-level orchestrator (facade pattern) tying everything together
- `gpt_embedder.py` — Semantic search over controlled vocabularies (GCMD keywords) using OpenAI embeddings
- `prompting_tools.py` — LangChain BaseTool wrappers for geocoding, CMR API, keyword search
- `prompts.py` — Central prompt template library (9 templates)

---

## How This Maps to Our Book

| NASA Cookbook Content | Book Chapter | How to Use |
|---------------------|--------------|------------|
| Prompt patterns (9 templates) | Ch 2: Conversational AI | Adapt all 9 patterns with domain-general science examples; add to Appendix B prompt library |
| LLM fundamentals (tokens, embeddings, parameters) | Ch 2: Conversational AI | Use as foundation, modernize with 2026 models |
| LangFlow/Promptlab RAG chatbot | Ch 13: Visual Programming | Demonstrate LangFlow as entry point to visual AI workflows |
| ReACT agents (astro + CMR) | Ch 14-15: Understanding & Building AI Agents | Adapt as the primary agent-building tutorial pattern; replace NASA APIs with generic scientific APIs |
| Fine-tuning (EJ classifier + extractor) | Ch 9: Auto Model Configuration | Show fine-tuning as an advanced model customization technique |
| RAG evaluation (OSDR) | Ch 16: Agentic Research Workflows | Use evaluation methodology as template for validating any AI-assisted pipeline |
| Embedding-based semantic search | Ch 8: Data Pipelines | Show how to build domain-specific search over controlled vocabularies |
| Multi-reader QA with evidence | Ch 16: Agentic Research Workflows | Demonstrate evidence-backed automated literature review |
| Ethics/verification approach | Ch 19: Ethics, Reproducibility | Reference NASA's "co-pilot" philosophy and fact-check patterns |

---

## Key Takeaways for Our Book

1. **Progressive complexity works.** The cookbook moves from chat prompts → RAG prototypes → agents → fine-tuning. Our book follows the same arc (chat → command line → automation → agents).

2. **9 prompt patterns are gold.** These are directly usable in Chapter 2 and Appendix B, adapted from NASA-specific to domain-general science examples.

3. **The ReACT agent pattern is the core agent architecture.** Both NASA agent notebooks use the same pattern: decompose question → select tool → execute → observe → repeat. This becomes our Chapter 15 foundation.

4. **Fine-tuning with small datasets is viable.** The EJ notebooks show ~40 examples can meaningfully improve extraction quality. This demystifies fine-tuning for scientists who think they need millions of examples.

5. **Evaluation matters.** The 3-tier evaluation framework (programmatic + LLM-as-judge + human) from EJ_extractions is a best practice we should teach in the book.

6. **The code is dated but the patterns are timeless.** The cookbook uses GPT-3.5/4 and older LangChain APIs, but the architectural patterns (chains, tools, agents, embeddings) apply regardless of the underlying model.

7. **Domain adaptation is straightforward.** Every notebook can be adapted to non-NASA domains by swapping: (a) the data source/API, (b) the controlled vocabulary, (c) the prompt examples. The architecture stays the same.

8. **The "80% data wrangling" statistic** (Gentemann et al., 2021) is a powerful motivator for our audience — it applies across all scientific domains.
