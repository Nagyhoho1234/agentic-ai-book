# CLAUDE.md — Project Instructions for Agentic AI for Scientists

## Project Overview

This is the planning and writing workspace for **"Agentic AI for Scientists: A Practical Guide to AI-Powered Research"** — a 16-chapter book targeting non-programmer scientists at the University of Debrecen, Hungary.

- **Book plan:** `BOOK_PLAN_v3.md` (active structure, scored 9.2/10 by Codex GPT-5.4)
- **Score progression:** 7.5 → 8.3 → 9.2
- **Status:** Ready to write. Start with Chapter 2.

## Writing Rules

### Voice and Tone
- Write for scientists who are NOT programmers. They understand research methodology, statistics, and domain science — but not software engineering.
- Focus on **outcomes and results**, not code quality or implementation details.
- Lead with "what this does for your research" before "how it works technically."
- Use Mollick's Four Rules as a recurring motif: (1) Always invite AI, (2) Be the human in the loop, (3) Treat AI like a capable colleague, (4) Assume this is the worst AI you'll ever use.
- No hype. Carl Sagan's "baloney detection kit" applies. Every claim about AI capability must be grounded in evidence or cited.

### Chapter Format (mandatory for every chapter)
1. **Real-world scientific scenario** as opener (1-2 paragraphs, relatable problem)
2. **Conceptual explanation** (minimal theory, maximum intuition)
3. **Step-by-step hands-on walkthrough** (the core of each chapter)
4. **"In your field" boxes** — discipline-specific adaptations (at least 2 per chapter)
5. **"Try it yourself" exercises** (3-5 per chapter)
6. **"What can go wrong" troubleshooting** section
7. **Key takeaways** (3-5 bullets)
8. **"Going deeper" references** to source books

### Difficulty Badges (add to chapter headers)
- `[Browser Only]` — Ch 1-4, 15-16
- `[Browser + Terminal]` — Ch 5, 7, 8
- `[Terminal + Basic Python]` — Ch 6, 9, 10, 11-13
- `[Any Level]` — Ch 14, Appendices

### Content Policies
- **Ethics:** Full treatment ONLY in Chapter 16. Other chapters use brief forward-reference boxes: "See Chapter 16 for the full ethics discussion."
- **Tool comparisons:** ONE comparison table per tool category in the most relevant chapter. Other chapters just reference it. No redundancy.
- **Platform-specific details** (pricing, features, setup) go to **Appendix A** and the companion website, NOT in narrative chapters. Chapters focus on principles and workflows.
- **"2026 landscape" framing:** Use sparingly. Prefer timeless principles. Volatile details get a "Current as of [date]" marker.
- **Debrecen thread:** Every chapter should have at least one concrete Debrecen connection (Komondor supercomputer, BMW factory, faculty examples, Hungarian resources).

## Reference Library

25 books/papers converted to ~320 chapter-level MD summaries in `books/`:

### Reference Codes (used in BOOK_PLAN_v3.md source mapping)
| Code | Folder | Book |
|------|--------|------|
| HQ | `chatgpt_scientific_research/` | Han & Qiu — ChatGPT in Scientific Research (Springer, 2024) |
| EM | `co_intelligence/` | Mollick — Co-Intelligence (Penguin, 2024) |
| KH | `agentic_ai_theories/` | Huang — Agentic AI: Theories and Practices (Springer, 2025) |
| SL | `python_scientific_computing/` | Lynch — Python for Scientific Computing (CRC, 2023) |
| SK | `brave_new_words/` | Khan — Brave New Words (Viking, 2024) |
| EUA | `eua_adopting_ai/` | EUA — Adopting AI for Universities (2026) |
| NAS | `national_academies_ai_life_sciences/` | National Academies — AI in Life Sciences (2025) |
| OECD | `oecd_ai_in_science/` | OECD — AI in Science (2023) |
| NASA | `../LLM-cookbook-for-open-science/` | NASA LLM Cookbook |

### Additional References
| Folder | Book |
|--------|------|
| `ai_snake_oil/` | Narayanan & Kapoor — AI Snake Oil (Princeton, 2024) |
| `teaching_with_ai/` | Bowen & Watson — Teaching with AI (JHU Press, 2024) |
| `ai_revolution_medicine/` | Lee et al. — AI Revolution in Medicine (Pearson, 2023) |
| `deep_learning_earth_sciences/` | Camps-Valls et al. — Deep Learning for Earth Sciences (Wiley, 2021) |
| `oxford_handbook_ai_governance/` | Bullock et al. — Oxford Handbook of AI Governance (OUP, 2024) |
| `learn_ai_python/` | Porter & Zingaro — Learn AI-Assisted Python (Manning, 2023) |
| `github_copilot_practice/` | Wienholt — GitHub Copilot in Practice (Springer, 2025) |
| `github_copilot_handbook/` | Bos & Pagels — GitHub Copilot Handbook (Packt, 2025) |
| `knime_predictive_analytics/` | Acito — Predictive Analytics with KNIME (Springer, 2023) |
| `n8n_beginners/` | Natheem — n8n Book for Beginners (2026) |
| `digital_twin_fundamentals/` | Vohra — Digital Twin Fundamentals (Wiley, 2023) |
| `digital_twin_handbook/` | Thakker & Pervez — Digital Twin Handbook (2024) |
| `national_academies_digital_twins/` | NAS — Digital Twins Research Gaps (NAP, 2024) |
| `intertwin_paper/` | interTwin — Scientific Digital Twins (ScienceDirect, 2025) |
| `fusion_digital_twin/` | Bhatia et al. — Fusion DT with Omniverse (AIP, 2025) |
| `generative_ai_higher_education/` | Chan & Colloton — GenAI in Higher Ed (Routledge, 2024) |
| `wef_ai_procurement/` | WEF — AI Procurement Guidelines (2023) |

### How to Use References
- Before writing any chapter, read the source mapping in `BOOK_PLAN_v3.md` to see which books feed that chapter.
- Read the relevant chapter MDs from `books/` — they contain comprehensive summaries, key concepts, and practical takeaways.
- Cite sources in the text as (Author, Year) and list them in the "Going deeper" section.
- Do NOT copy text from reference books. Synthesize and adapt for our audience.

## Other Key Files
| File | Purpose |
|------|---------|
| `BOOK_PLAN_v3.md` | Active book structure with full source mapping and gap analysis |
| `BOOK_STRUCTURE_3level.md` | Detailed 3-level subchapter structure |
| `NASA_LLM_Cookbook_Analysis.md` | Analysis of NASA cookbook mapped to our chapters |
| `CODEX_REVIEW.md` | GPT-5.4 v2 review (7.5/10) |
| `CODEX_REVIEW_v3_RESPONSE.md` | GPT-5.4 v3 review (8.3→9.2) with accepted/rejected recommendations |
| `FINAL_SUMMARY_TABLE.md` | Master status table |
| `RECOMMENDED_BOOKS_MISSING_TOPICS.md` | Book recommendations for originally-weak topics |
| `research/` | 5 university research reports (Florida, Helsinki, Northeastern, JHU, Debrecen) |
| `examples/` | Working code examples for chapters |

## Writing Workflow

1. **Before writing a chapter:** Read `BOOK_PLAN_v3.md` source mapping for that chapter, then read relevant book summaries from `books/`.
2. **Write in:** `chapters/chXX_title.md` (create the `chapters/` directory when starting)
3. **Examples/code go in:** `examples/chXX_topic/`
4. **Git commit** after completing each chapter section (not just at the end).
5. **Cross-review with Codex:** After drafting a chapter, send it to `codex exec --model gpt-5.4` for review. Judge recommendations before applying.

## Parallelization
- This machine has AMD 9950X (32 threads) and 96GB RAM.
- Use up to 3-4 parallel agents for research tasks (NOT 9 — causes rate limits).
- The user pays for Anthropic Max plan. Respect rate limits.

## Debrecen Context (use throughout)
- 14 faculties, ~30,000 students, ~7,800 international students
- Komondor supercomputer (5 PFLOPS)
- NVIDIA DLI Teaching Centre, Microsoft AI Knowledge Centre
- Automotive & AI Coordination Institute (Sept 2025)
- BMW EUR 2B factory — industrial AI demand
- "Modern AI" elective course (Feb 2025, all faculties)
- AI Expert Postgraduate Diploma (Faculty of Informatics)
- Hungary AI Strategy 2025-2030, AI Coalition (400+ members)
- PULI GPT (Hungarian language model), HuSpaCy

## Publisher Target
Springer Nature (primary) — academic credibility, institutional reach, library distribution.
CRC Press (fallback) — practical/professional positioning.

## Glossary Terms (define in glossary, use consistently)
LLM, RAG, MCP, agent, multi-agent system, vector store, embedding, digital twin, fine-tuning, prompt engineering, hallucination, RLHF, ReACT, token, context window, API
