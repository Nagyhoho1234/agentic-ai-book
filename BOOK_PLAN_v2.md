# Agentic AI for Scientists
## A Practical Guide to AI-Powered Research — v2

**Target audience:** Scientists, researchers, and faculty members who are NOT programmers but want to leverage AI tools effectively in their research workflows.

**Positioning:** The only book that takes scientists on the complete journey from first AI conversation through agentic coding tools to autonomous research pipelines — with hands-on examples at every step.

**Context:** Supports the AI transition at the University of Debrecen (14 faculties, 30,000+ students, Komondor supercomputer), aligned with Hungary's National AI Strategy 2025-2030.

---

## Changes from v1 and Rationale

### What changed and why:

1. **Merged "Terminal basics" into Chapter 4 instead of a standalone chapter.** Lynch's Python book and the ChatGPT book both show that scientists learn tools *through tasks*, not through abstract setup chapters. Removed the standalone "Why the Terminal Matters" chapter — scientists will encounter the terminal organically when they need coding assistants.

2. **Added RAG (Retrieval-Augmented Generation) as its own chapter.** The NASA cookbook's most impactful notebooks (OSDR chatbot, CMR agent) all use RAG. Mollick's Co-Intelligence emphasizes that AI + your own data is the killer combination. This was buried across multiple chapters in v1; it deserves its own treatment.

3. **Moved "Visual Programming" earlier (from Part V to Part III).** Helsinki's Elements of AI success proves that visual/no-code approaches should come *before* heavy coding, not after. Scientists who aren't programmers need an on-ramp. LangFlow appears in the NASA cookbook as a prototyping tool, not an advanced technique.

4. **Combined "Building Your First AI Agent" and "Agentic Research Workflows" into a tighter structure.** The Ken Huang book's 7-layer architecture and the NASA cookbook's ReACT pattern provide a clear, non-redundant framework. Two chapters were too many for what's essentially one learning arc.

5. **Added a dedicated chapter on AI for Scientific Writing and Communication.** The Han & Qiu book devotes 12 of 15 chapters to this. It's clearly what scientists care about most. Was underrepresented in v1 (buried in Ch 2 bullet points).

6. **Added "AI-Assisted Literature Review and Knowledge Discovery" as its own chapter.** This is the #1 entry point for most scientists. Mollick, Han & Qiu, and the NASA cookbook all emphasize it. Deserves dedicated treatment with RAG, semantic search, and citation management.

7. **Strengthened the Debrecen thread throughout.** Research revealed Komondor supercomputer (5 PFLOPS), Automotive & AI Coordination Institute, GE HealthCare NLP project, BMW factory demand, NVIDIA DLI Teaching Centre. These provide concrete local anchors for every part.

8. **Reduced from 19 to 16 chapters.** Removed redundancy, merged overlapping topics. Tighter is better for a practical guide. Each chapter now has a clearer unique contribution.

9. **Added Mollick's "Four Rules" as a structural motif.** His framework (Always Invite AI, Be the Human in the Loop, Treat AI Like a Person, Assume This Is the Worst AI) provides a memorable through-line for the entire book.

10. **Elevated "Mathematical Modeling with AI" by integrating it with simulation rather than separating them.** Lynch's book structure (math → scientific computing → AI) shows these flow naturally together.

---

## PART I: FOUNDATIONS — The AI-Augmented Scientist
*"From curiosity to first results"*

### Chapter 1: The AI Revolution in Scientific Research
*Why every scientist needs this book*

- The 80/20 problem: 80% of research time is data wrangling (Gentemann et al., 2021)
- The spectrum of AI: from autocomplete to autonomous discovery
  - Chat assistants → coding tools → pipelines → agents → AI Scientists
- Landmark examples:
  - Berkeley Lab's A-Lab (autonomous materials synthesis)
  - Sakana AI's AI Scientist (idea → paper → review, published in Nature 2026)
  - Google Co-Scientist (hypothesis generation)
  - AlphaFold 3, CRISPR-GPT
- Mollick's Four Rules for Co-Intelligence as our guiding framework
- The University of Debrecen context:
  - 14 faculties, 30K students, Komondor supercomputer
  - "Modern AI" course, AI Expert diploma, NVIDIA DLI centre
  - Hungary's AI Strategy 2025-2030, AI Coalition (400+ members)
  - BMW factory and industrial demand for AI-literate graduates
- What this book covers vs. what existing books cover (positioning)
- How to use this book: progressive chapters, skip what you know

**References:** Mollick Ch 1-3 (framework), Debrecen research (local context), Huang Ch 1 (agent spectrum)

---

### Chapter 2: Conversational AI — Your First Research Partner
*Getting real value from AI chat in under an hour*

- Understanding LLMs: what they are and aren't (tokens, context windows, hallucinations)
- Choosing your platform (2026 landscape): Claude, ChatGPT, Gemini, Copilot
  - Strengths, costs, context windows, when to use which
- The 9 NASA prompt patterns adapted for general science:
  1. Recipe Pattern → experimental protocols, data processing workflows
  2. Output Automator → generating analysis scripts from descriptions
  3. Persona Pattern → adopt expert perspective in adjacent fields
  4. Flipped Interaction → Socratic learning of new topics
  5. Question Refinement → sharpening research questions
  6. Alternative Approach → broadening methodological awareness
  7. Cognitive Verifier → decomposing complex questions
  8. Fact Check List → making AI assumptions explicit and verifiable
  9. Context Manager → focusing/limiting AI scope
- Combining patterns for complex tasks (NASA's mDGF example adapted)
- Working with parameters: temperature, top-p, system prompts
- Verification strategies: the "co-pilot" philosophy (never let AI fly unattended)
- Hands-on: 5 exercises using only a browser

**References:** NASA Cookbook (9 patterns), Han & Qiu Ch 1 (LLM basics), Mollick Ch 3 (four rules)

---

### Chapter 3: AI for Scientific Writing and Communication
*From manuscript drafts to public engagement*

- Literature review assistance: summarizing papers, extracting key findings
- Writing and editing manuscripts:
  - Language editing and grammar correction
  - Crafting article titles
  - Adapting tone for different journals
- Responding to peer reviewers (strategies + templates)
- Spotting errors in your own and others' work
- Writing research proposals and grant applications
- Science communication: popular articles, social media, press releases
- Designing experimental studies and survey instruments with AI
- The hallucination problem in citations: detection and prevention
- Ethics: attribution, transparency, journal policies
- Hands-on: take one of your own papers through the full AI editing workflow

**References:** Han & Qiu Ch 2-12 (entire book is our source), Mollick Ch 5 (AI creativity)

---

### Chapter 4: AI for Data Analysis — No Coding Required
*Upload your data and get answers through conversation*

- Uploading and analyzing datasets through chat interfaces
  - CSV, Excel, images, PDFs, lab outputs
- AI-powered exploratory data analysis
- Statistical analysis through conversation
  - Descriptive statistics, hypothesis testing, regression
- Data visualization: from quick plots to publication-quality figures
- Using ChatGPT's Code Interpreter / Advanced Data Analysis
- Claude's Artifacts for interactive outputs
- Gemini's integration with Google Sheets
- When no-code reaches its limits → transition to Chapter 5
- Hands-on: analyze a real dataset entirely through chat

**References:** Han & Qiu Ch 9-10 (experiment + survey design), Lynch Ch 4-5 (statistics context)

---

## PART II: LEVELLING UP — Coding with AI Assistance
*"From clicking to commanding"*

### Chapter 5: AI Coding Assistants — Writing Code Without Being a Programmer
*The terminal is not scary when AI writes the code for you*

- The paradigm shift: describing what you want vs. learning syntax
- Setting up your environment (Python, git, virtual environments) — with AI help
- The 2026 landscape: Claude Code, GitHub Copilot, Cursor, Windsurf, Codex
  - What each does best, costs, how to choose
- Your first AI-assisted Python scripts:
  - Reading and cleaning a messy dataset
  - Creating publication-quality figures
  - Fitting a model to experimental data
  - Batch processing files
- The feedback loop: describe → generate → test → refine → iterate
- Version control with git (AI-managed)
- Jupyter notebooks as the scientist's lab notebook
- Key Python libraries: NumPy, SciPy, Pandas, Matplotlib, scikit-learn
- Hands-on: 5 common research tasks solved with Claude Code

**References:** Lynch Section I (Python foundations), NASA Cookbook code (patterns), JHU Certificate (curriculum structure)

---

### Chapter 6: AI-Assisted Mathematical Modeling and Simulation
*From equations on paper to running models on screen*

- From research question to mathematical formulation — with AI guidance
- Translating equations into code:
  - ODEs and PDEs (Euler, Runge-Kutta, finite differences)
  - Algebraic and optimization problems
  - Symbolic computation with SymPy
- Equation discovery from data: symbolic regression with PySR
  - How it works: evolutionary search for mathematical expressions
  - From dataset to discovered governing equation
  - Validating against domain knowledge
- Physics-Informed Neural Networks (PINNs): embedding known physics into ML
- Building simulation models:
  - Agent-based models, Monte Carlo methods
  - Stochastic vs. deterministic approaches
- Automatic model calibration:
  - Hyperparameter optimization (Optuna, Bayesian methods)
  - AI-suggested parameter ranges from literature
  - Sensitivity analysis
- Surrogate models: when your simulation is too slow
- Hands-on: build a complete model from equations → code → calibration → results

**References:** Lynch Section II entire (scientific computing), Lynch Ch 6 (dynamical systems), Ch 12-14 (numerical methods)

---

### Chapter 7: Data Pipelines and Automation
*Stop doing manually what a script can do in seconds*

- The data pipeline concept: from raw data to analysis-ready
- Identifying automation opportunities in your workflow
- Data ingestion from multiple sources (files, databases, APIs, sensors)
- Cleaning, validation, and quality assessment:
  - Missing values, outliers, format inconsistencies
  - Automated quality reports
- Batch processing: files, images, documents at scale
- Scheduled tasks and monitoring (cron, watchdogs)
- Web scraping for research data (ethical considerations)
- Pipeline tools: simple Python scripts → Dagster → Nextflow
- Reproducibility: ensuring others can run your pipeline
- Hands-on: build a pipeline that processes your actual research data

**References:** NASA Cookbook (CMR connector, data pipelines), Huang Ch 5 (workflow automation)

---

## PART III: INTELLIGENT TOOLS — AI That Knows Your Domain
*"From generic AI to your AI"*

### Chapter 8: Visual Programming and Workflow Design
*Build AI workflows by dragging and dropping — no syntax required*

- Why visual programming appeals to scientists (flowcharts are natural)
- Node-based workflow editors: the concept
- n8n: general-purpose visual automation
  - Connecting data sources, triggers, actions
  - Example: monitor for new papers in your field → summarize → email
- LangFlow: visual LLM pipeline design
  - Building a RAG chatbot visually (NASA Promptlab approach adapted)
  - Prototyping before coding
- Node-RED: IoT and sensor data workflows
- KNIME and Orange: visual data science for statistical analysis
- When to use visual vs. text-based approaches
- Hands-on: build an automated research workflow visually in n8n

**References:** NASA Cookbook (LangFlow/Promptlab section), UF research (AI integration approaches), Helsinki (accessible design principles)

---

### Chapter 9: RAG — Teaching AI Your Own Data
*Make AI an expert in YOUR research domain*

- The limitation of general AI: it doesn't know your data
- Retrieval-Augmented Generation (RAG): concept and architecture
  - Document loading, chunking, embedding, vector stores, retrieval, generation
- Building a chatbot for your research documents:
  - Your papers, lab notes, datasets, manuals
  - NASA OSDR chatbot as a model (adapted for general use)
- Semantic search over controlled vocabularies
  - NASA's GCMD keyword approach adapted for any domain taxonomy
- Evaluating RAG quality:
  - Retrieval recall: are we finding the right documents?
  - Answer quality: BERTScore, ROUGE, human evaluation
  - The 3-tier evaluation framework (programmatic + LLM-judge + human)
- Fine-tuning for your domain (when RAG isn't enough):
  - Fine-tuning with small datasets (~40 examples can work!)
  - Encoder fine-tuning (classification) vs. decoder fine-tuning (generation)
  - Practical guide with NASA EJ example adapted
- Hands-on: build a RAG system over your own research papers

**References:** NASA Cookbook (OSDR evaluation, EJ notebooks, gpt_embedder), Huang Ch 2 (RAG vs Agentic RAG)

---

### Chapter 10: Digital Twins — Virtual Replicas of Real Systems
*Merge your models with real-time data*

- What are digital twins and why scientists need them
- Architecture: data sources → model → visualization → feedback loop
- Platforms:
  - NVIDIA Omniverse (dominant, physics-based)
  - Ansys TwinAI (engineering simulation)
  - interTwin (EU, open-source for science: physics, astronomy, climate)
  - Open-source alternatives
- Building a simple digital twin with AI assistance:
  - Connecting sensor data to a model
  - Real-time visualization
  - Predictive capabilities
- Examples from different fields:
  - Environmental monitoring and climate
  - Industrial processes (BMW Debrecen context)
  - Biological systems
  - Infrastructure (buildings, energy: 20% savings demonstrated)
- The Debrecen connection: Automotive & AI Coordination Institute, BMW factory
- Hands-on: create a digital twin for a laboratory experiment or process

**References:** Huang Ch 11 (robotics/simulation), Debrecen research (BMW, Automotive Institute), interTwin project

---

## PART IV: AGENTIC AI — From Tools to Teammates
*"From using AI to collaborating with AI"*

### Chapter 11: Understanding AI Agents
*What makes AI "agentic" — and why it matters for science*

- From tools to agents: the autonomy spectrum
  - Huang's 10 characteristics of AI agents
  - The 7-layer agent architecture (foundation → ecosystem)
  - Mollick's Centaur (human decides, AI executes) vs. Cyborg (seamless integration)
- The ReACT pattern: Thought → Action → Observation → repeat
  - NASA's CMR and Astro agents as concrete examples
- Tool use and MCP (Model Context Protocol):
  - The universal standard for connecting AI to external tools and data
  - 10,000+ servers, supported by Claude, ChatGPT, Gemini, Copilot
- Multi-agent systems: when one agent isn't enough
  - Coordination, communication, conflict resolution (Huang Ch 3)
- Safety, guardrails, and human-in-the-loop:
  - OWASP Top 10 for AI Agents
  - Alignment drift, motivation drift
  - The "co-pilot" principle revisited
- The AI agent economy: who pays, who benefits (Huang Ch 4)

**References:** Huang Ch 1-4 (theory), Mollick Ch 6 (Centaur/Cyborg), NASA Cookbook (ReACT agents), JHU Certificate (curriculum)

---

### Chapter 12: Building AI Agents for Research
*Your first agent that actually does useful work*

- Agent frameworks for scientists:
  - CrewAI: define agent teams with roles (easiest for non-programmers)
  - LangGraph: graph-based workflows (most flexible)
  - AutoGen: conversational agents (best for collaborative reasoning)
  - Claude Agent SDK: professional-grade toolkit
- Building your first research agents:
  - Literature review agent team (searcher → reader → synthesizer)
  - Data processing agent pipeline
  - Experiment monitoring agent
- Connecting agents to your data and tools via MCP:
  - File systems, databases, APIs, instruments
  - Creating custom MCP servers for your lab
- Designing end-to-end agentic research workflows:
  - Hypothesis generation → data collection → analysis → reporting
  - Human judgment at critical decision points
- Monitoring and debugging agent systems
- Hands-on: build a multi-agent system that automates a real research sub-task

**References:** Huang Ch 2-3 (frameworks, multi-agent), NASA Cookbook (agent.py, chains.py architecture), JHU Certificate (culminating project)

---

### Chapter 13: Creating Your Own Programs and Tools
*From scripts to applications that your colleagues can use*

- When your research needs custom software
- AI-assisted program design and architecture
- Building interfaces: CLI, GUI (Streamlit/Gradio), web apps
- Packaging and sharing tools:
  - pip packages, Docker containers
  - GitHub repositories with documentation
- Creating MCP servers: making your data/tools accessible to AI agents
- Publishing and maintaining scientific software
- Open-source best practices
- Hands-on: build and publish a domain-specific research tool

**References:** NASA Cookbook (code architecture as model), Huang Ch 5 (workflow to software), Northeastern (student builder program model)

---

## PART V: THE BIG PICTURE — Leading the AI Transition
*"From personal adoption to institutional transformation"*

### Chapter 14: The AI-Augmented Research Lab
*Designing your complete AI-powered workflow*

- The practical 2026 scientific AI stack:
  - Claude Code / Cursor for interactive coding
  - CrewAI / LangGraph for custom agents
  - n8n / LangFlow for visual automation
  - PySR for equation discovery
  - Dagster / Nextflow for data pipelines
  - MCP for connecting everything
- Cost management: free tiers → subscriptions → API budgets → HPC
- Computing resources: laptop → cloud → Komondor supercomputer
- Data security and privacy:
  - What to send to cloud AI vs. keep local
  - EU AI Act implications
  - GDPR and research data
- Team collaboration: sharing AI workflows, training colleagues
- Measuring AI impact: time saved, quality improved, new capabilities unlocked

**References:** All books synthesized, Debrecen research (Komondor, infrastructure)

---

### Chapter 15: Lessons from Leading Universities
*What works, what doesn't, and what Debrecen should do next*

- University of Florida: "AI Across the Curriculum"
  - 230 courses, $70M NVIDIA, HiPerGator, GatorTron
  - Lesson: embed AI in every discipline, don't silo it
- University of Helsinki: Elements of AI
  - 2M enrollments, no prerequisites, free, 22 languages
  - Lesson: accessibility and inclusion drive adoption
- Northeastern: Campus-wide Claude deployment
  - 50K users, Claude for Education, Learning Mode
  - Lesson: choose one platform, deploy it properly, measure impact
- Johns Hopkins: Agentic AI Certificate
  - 16 weeks, professional-grade curriculum
  - Lesson: agentic AI requires structured, progressive learning
- What Debrecen has and what it needs:
  - Has: Modern AI course, AI Expert diploma, Komondor, NVIDIA centre, industry partners
  - Needs: discipline-specific AI integration (the UF model), campus-wide AI tool deployment (the Northeastern model), hands-on agentic AI training (the JHU model)
- A roadmap for faculty AI transition
- How this book fits into the curriculum

**References:** All 5 university research reports

---

### Chapter 16: Ethics, Reproducibility, and the Future of AI in Science
*Responsible AI use and where this is all heading*

- AI ethics in scientific research:
  - Attribution and authorship (who wrote this paper?)
  - Bias in AI-generated analysis
  - The EU AI Act and what it means for researchers
  - Journal policies on AI use (current landscape)
- Reproducibility in the age of AI:
  - Documenting AI-assisted workflows
  - Version pinning and prompt logging
  - The "AI Methods" section in your papers
  - Sharing prompts, configs, and agent definitions
- NASA's 5 AI principles: Transparency, Trust, Teamwork, Training, Techniques
- Mollick's four rules revisited as ethical guardrails
- Where this is all heading:
  - Mollick's four scenarios (stagnation → AGI)
  - Fully autonomous scientific discovery (AI Scientist, Nature 2026)
  - The scientist's role: from doing to directing to collaborating
- Your first steps after finishing this book

**References:** Mollick Ch 9 (future scenarios), Han & Qiu Ch 13-14 (pitfalls), Huang Ch 12 (safety), NASA ethics framework

---

## APPENDICES

### Appendix A: Setting Up Your AI Research Environment
- Step-by-step installation: Python, git, VS Code, Claude Code, Cursor
- API keys and account setup (Claude, OpenAI, Gemini)
- Komondor supercomputer access (for Debrecen users)
- Recommended hardware and cloud options
- Troubleshooting common issues

### Appendix B: Prompt Library for Scientists
- 50+ tested prompts organized by research task:
  - Literature review & synthesis (10)
  - Writing & editing (10)
  - Data analysis & visualization (10)
  - Experimental design (5)
  - Code generation (10)
  - Agent instructions (5)
- Templates for common workflows
- Based on NASA's 9 patterns + our extensions

### Appendix C: Resources and Further Reading
- Key books (annotated, with what to read from each)
- Key papers (with relevance notes)
- Online courses and certifications
- Communities and forums
- Hungarian-language resources (PULI GPT, HuSpaCy)

---

## CROSS-REFERENCE: What Comes From Where

| Our Chapter | Han & Qiu (ChatGPT) | Mollick (Co-Intelligence) | Huang (Agentic AI) | Lynch (Python/SciComp) | NASA Cookbook |
|---|---|---|---|---|---|
| 1. AI Revolution | — | Ch 1-3 (framework) | Ch 1 (spectrum) | — | Motivation section |
| 2. Conversational AI | Ch 1 (basics) | Ch 3 (four rules) | — | — | 9 prompt patterns |
| 3. Scientific Writing | Ch 2-12 (primary source) | Ch 5 (creativity) | — | — | — |
| 4. Data Analysis | Ch 9-10 (design) | — | — | Ch 4-5 (statistics) | — |
| 5. Coding Assistants | — | — | — | Section I (Python) | Code architecture |
| 6. Math Modeling | — | — | — | Section II (entire) | — |
| 7. Data Pipelines | — | — | Ch 5 (workflows) | — | CMR connector |
| 8. Visual Programming | — | — | — | — | LangFlow section |
| 9. RAG | — | — | Ch 2 (RAG vs Agentic RAG) | — | OSDR + EJ notebooks |
| 10. Digital Twins | — | — | Ch 11 (robotics) | — | — |
| 11. Understanding Agents | — | Ch 6 (Centaur/Cyborg) | Ch 1-4 (theory) | — | ReACT agents |
| 12. Building Agents | — | — | Ch 2-3 (frameworks) | — | agent.py, chains.py |
| 13. Creating Tools | — | — | Ch 5 (deployment) | — | Code modules |
| 14. AI-Augmented Lab | — | Ch 8 (coaching) | Ch 5 (business) | — | Best practices |
| 15. University Lessons | — | Ch 7 (tutoring) | — | — | — |
| 16. Ethics & Future | Ch 13-14 (pitfalls) | Ch 9 (future) | Ch 12 (safety) | — | Ethics section |

### Unique contributions (NOT covered by any reference book):
- **Chapter 5**: AI coding assistants for scientists (Claude Code, Cursor, Codex comparison)
- **Chapter 6**: PySR symbolic regression + PINNs for equation discovery (cutting-edge)
- **Chapter 8**: Visual programming with n8n/LangFlow for research workflows
- **Chapter 10**: Digital twins for scientific applications (interTwin, Omniverse)
- **Chapter 12**: Building multi-agent research systems with MCP
- **Chapter 15**: University AI transition roadmap (entirely original synthesis)
- **Debrecen thread**: woven through every chapter (entirely original)

---

## PRODUCTION NOTES

- **Estimated length:** ~350-400 pages (tighter than v1's 400-500)
- **Chapters:** 16 (down from 19 in v1)
- **Format per chapter:**
  - Real-world scientific scenario as opener
  - Conceptual explanation (minimal theory, maximum intuition)
  - Step-by-step hands-on walkthrough
  - "Try it yourself" exercises
  - "What can go wrong" troubleshooting
  - Key takeaways (3-5 bullets)
  - "Going deeper" references to source books
- **Companion repository:** GitHub with all code, notebooks, prompt templates
- **Language:** English (primary), potential Hungarian translation
- **Publisher targets:** Springer Nature (academic credibility) or CRC Press (practical focus)
- **Debrecen-specific supplement:** Optional extra chapter/appendix with Hungarian resources, Komondor access guide, local industry connections
