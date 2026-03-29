# Agentic AI for Scientists
## A Practical Guide to AI-Powered Research -- v3

**Target audience:** Scientists, researchers, and faculty members who are NOT programmers but want to leverage AI tools effectively in their research workflows.

**Positioning:** The only book that takes scientists on the complete journey from first AI conversation through agentic coding tools to autonomous research pipelines -- with hands-on examples at every step.

**Context:** Supports the AI transition at the University of Debrecen (14 faculties, 30,000+ students, Komondor supercomputer), aligned with Hungary's National AI Strategy 2025-2030.

---

## Changes from v2 and Rationale

### Structural changes driven by Codex review (accepted recommendations):

1. **Part names updated** to be more reader-friendly (Codex Rec 7).
2. **Pathway map added after Ch 4** -- a 1-page "Reading Pathways" section guiding different scientist profiles through the book (Codex Rec 3).
3. **Ch 6 restructured with core/advanced split** -- core sections accessible to all scientists; advanced material (PINNs, symbolic regression with physics priors, surrogate models) in clearly marked optional boxes (Codex Rec 1).
4. **Ethics consolidated into Ch 16** -- brief forward-reference boxes in Ch 3 and Ch 14; full treatment only in Ch 16, which now includes research integrity (Codex Rec 2 & 4).
5. **Ch 13 slimmed** -- removed developer-focused material (API design, open-source best practices); moved Docker/pip packaging to Appendix A; kept Streamlit/Gradio and MCP server creation (Codex Rec 5).
6. **Ch 15 expanded** with major teaching section and change management content; retitled "AI in the University: Teaching, Learning, and Institutional Transformation" (Codex Rec 4).
7. **Evidence quality assessment added to Ch 2** -- expanded section 2.5 on verifying AI outputs and assessing methodological quality (Codex Rec 4).
8. **Procurement guidance folded into Ch 14** -- platform selection criteria, EU MCC-AI clauses, EDUCAUSE checklist (Codex Rec 4).

### New content driven by reference book analysis:

9. **Three new reference books integrated** -- EUA report (institutional adoption), National Academies (life sciences/biosecurity), OECD AI in Science (policy, 29 essays). These fill gaps in policy, governance, and discipline-specific coverage.
10. **Missing topics from RECOMMENDED_BOOKS_MISSING_TOPICS.md** now mapped to specific chapters with source material identified.
11. **NASA Cookbook analysis** fully integrated into chapter-level source mapping.

---

## Reference Book Key (used in source mapping below)

| Code | Book | Focus |
|------|------|-------|
| **HQ** | Han & Qiu -- ChatGPT in Scientific Research and Writing (Springer, 2024) | Scientific writing, prompts, pitfalls |
| **EM** | Mollick -- Co-Intelligence (Portfolio/Penguin, 2024) | Human-AI collaboration, creativity, education, future scenarios |
| **KH** | Huang (ed.) -- Agentic AI: Theories and Practices (Springer, 2025) | Agent architecture, multi-agent systems, security, domains |
| **SL** | Lynch -- Python for Scientific Computing and AI (CRC Press, 2023) | Python, numerical methods, ML, neural networks |
| **SK** | Khan -- Brave New Words (Viking, 2024) | AI in education, tutoring, equity, assessment |
| **EUA** | EUA -- Adopting AI for Universities (EUA, 2026) | Institutional strategy, ethics, training, regulation, sustainability |
| **NAS** | National Academies -- Age of AI in Life Sciences (NAP, 2025) | AI in biology, biosecurity, data strategy, policy |
| **OECD** | OECD -- AI in Science (OECD Publishing, 2023) | AI across scientific disciplines, policy, reproducibility, infrastructure |
| **NASA** | NASA LLM Cookbook for Open Science (2024) | Prompt patterns, RAG, agents, fine-tuning (not a book but key reference) |

---

## PART I: Getting Started with AI in Research
*"From curiosity to first results"*

### Chapter 1: The AI Revolution in Scientific Research
*Why every scientist needs this book*

**Content:**
- The 80/20 problem: 80% of research time is data wrangling
- The spectrum of AI: from autocomplete to autonomous discovery
- Landmark examples: A-Lab, AI Scientist, Google Co-Scientist, AlphaFold 3, CRISPR-GPT
- Is science getting harder? Declining disruptiveness, larger teams, longer timescales
- Mollick's Four Rules for Co-Intelligence as guiding framework
- The Debrecen context: 14 faculties, Komondor, Hungary's AI Strategy
- How to use this book: progressive chapters, pick your entry point

**Reference sources:**
- **EM** Ch 1-3: History of AI, alignment, four rules framework
- **KH** Ch 1: Genesis and evolution of AI agents, 10 characteristics, taxonomy
- **OECD** Ch 1-5: Science getting harder (Bloom), declining disruptiveness (Park), AI for scientific discovery (Kitano)
- **NAS** Ch 1: AI in life sciences context, beneficial potential
- **HQ** Ch 1: ChatGPT introduction and scope
- **SK** Ch 0: Introduction to AI in education context

---

### Chapter 2: Conversational AI -- Your First Research Partner
*Getting real value from AI chat in under an hour*

**Content:**
- Understanding LLMs: tokens, context windows, hallucinations
- Choosing your platform (2026): Claude, ChatGPT, Gemini, Copilot
- The 9 NASA prompt patterns adapted for general science
- Combining patterns for complex tasks
- Working with parameters: temperature, top-p, system prompts
- **[NEW v3] Section 2.5 expanded: Evidence Quality and Verification**
  - How to tell when an AI answer is methodologically weak
  - Cross-checking against authoritative sources
  - The opacity problem: fluent outputs hiding omissions and overconfidence
  - Critical thinking skills for the AI age
  - The co-pilot philosophy: never let AI fly unattended

**Reference sources:**
- **NASA** 9 prompt patterns (primary source for prompting)
- **HQ** Ch 1: LLM basics, capabilities overview
- **EM** Ch 3: Four rules, treating AI as capable colleague
- **OECD** Ch 21: Interpretability and understanding ML reasoning
- **OECD** Ch 26: Lessons from shortcomings in ML for medical imaging (evidence quality)
- *Additional:* AI Snake Oil (Narayanan & Kapoor) for evidence quality framework

---

### Chapter 3: AI for Scientific Writing and Communication
*From manuscript drafts to public engagement*

**Content:**
- Literature review assistance: summarizing, extracting findings, identifying gaps
- Writing and editing manuscripts: grammar, clarity, titles, journal adaptation
- Responding to peer reviewers: strategies and templates
- Spotting errors in your own and others' work
- Writing research proposals and grant applications
- Science communication: popular articles, social media, press releases
- Designing experimental studies and survey instruments with AI
- The hallucination problem in citations: detection and prevention
- **[Ethics: brief forward-reference box to Ch 16 for full treatment]**

**Reference sources:**
- **HQ** Ch 2-12: PRIMARY source (entire book covers scientific writing with AI)
  - Ch 2: Extracting key points
  - Ch 3: Interpreting figures
  - Ch 4: Evaluating papers
  - Ch 5: Spotting errors
  - Ch 6: Responding to reviewers
  - Ch 7: Language editing
  - Ch 8: Crafting titles
  - Ch 9: Experimental design
  - Ch 10: Survey design
  - Ch 11: Research proposals
  - Ch 12: Science communication
  - Ch 13-14: Pitfalls and recommendations
- **EM** Ch 5: AI as creative, hallucination as feature/bug
- **OECD** Ch 6-7: Semantic analysis for finding research, AI connections between papers
- **OECD** Ch 8: AI-assisted peer review

---

### Chapter 4: AI for Data Analysis -- No Coding Required
*Upload your data and get answers through conversation*

**Content:**
- Uploading and analyzing datasets through chat interfaces
- AI-powered exploratory data analysis
- Statistical analysis through conversation
- Data visualization: quick plots to publication-quality figures
- Platform-specific capabilities: Code Interpreter, Artifacts, Gemini+Sheets
- When no-code reaches its limits -- transition to Chapter 5

**[NEW v3] Reading Pathways (end of chapter):**
- **Social scientist:** Ch 1-4 -> Ch 8 -> Ch 9 -> Ch 15-16
- **Wet lab biologist:** Ch 1-5 -> Ch 7 -> Ch 9 -> Ch 12 -> Ch 15-16
- **Computational/physical scientist:** Ch 1-6 -> Ch 7 -> Ch 9 -> Ch 10 -> Ch 11-12 -> Ch 15-16
- **Lab/group leader:** Ch 1-4 -> Ch 14 -> Ch 15 -> Ch 16
- **Teaching-focused faculty:** Ch 1-4 -> Ch 15 -> Ch 16
- **Full journey:** All chapters in order

**Reference sources:**
- **HQ** Ch 9-10: Experimental and survey design (data context)
- **SL** Ch 4-5: Statistics, hypothesis testing, probability
- **SL** Ch 8: scikit-learn basics, k-means, decision trees
- **SL** Ch 15: Linear regression, Markov chains, Monte Carlo
- **OECD** Ch 9: Current AI applications overview (context)

---

## PART II: Everyday Scientific Work with AI
*"From clicking to commanding"*

### Chapter 5: AI Coding Assistants -- Writing Code Without Being a Programmer
*The terminal is not scary when AI writes the code for you*

**Content:**
- The paradigm shift: describing what you want vs. learning syntax
- Setting up your environment with AI help
- The 2026 landscape: Claude Code, GitHub Copilot, Cursor, Windsurf, Codex
- First AI-assisted Python scripts: cleaning data, figures, model fitting, batch processing
- The feedback loop: describe -> generate -> test -> refine -> iterate
- Version control with git (AI-managed)
- Jupyter notebooks as the scientist's lab notebook
- Key Python libraries: NumPy, SciPy, Pandas, Matplotlib, scikit-learn

**Reference sources:**
- **SL** Section I entire: Python foundations (Ch 1-5)
  - Ch 1: Python basics, data types, functions
  - Ch 2: NumPy, Matplotlib, Jupyter
  - Ch 3: SymPy symbolic math
  - Ch 4: Data structures, statistics
  - Ch 5: Applied mathematics
- **NASA** Code architecture (agent.py, chains.py as patterns)
- **KH** Ch 5: Workflow transformation, automation dimensions
- *Gap:* AI coding assistants themselves (Claude Code, Cursor, Copilot comparison) -- requires original research and testing

---

### Chapter 6: AI-Assisted Mathematical Modeling and Simulation
*From equations on paper to running models on screen*

**[v3 RESTRUCTURED: Core/Advanced split per Codex Rec 1]**

**Core sections (accessible to all scientists):**
- From research question to mathematical formulation with AI guidance
- Translating equations into code: ODEs, PDEs, optimization
- AI as translator: equations to Python in one prompt
- Symbolic computation with SymPy
- Building simulation models: agent-based, Monte Carlo, stochastic
- Automatic model calibration: Optuna, Bayesian methods, sensitivity analysis

**Advanced sections (boxed/optional, for computational scientists):**
- Equation discovery: symbolic regression with PySR
- LLM-guided symbolic regression with physics priors
- Physics-Informed Neural Networks (PINNs)
- Surrogate models for expensive simulations

**Reference sources:**
- **SL** Section II entire: PRIMARY source for numerical methods
  - Ch 6: Dynamical systems, bifurcation, chaos
  - Ch 7: Chemical kinetics, SIR models
  - Ch 10: Chaos, fractals, nonlinear dynamics
  - Ch 12: Numerical methods for ODEs (Euler, Runge-Kutta)
  - Ch 13: Numerical methods for PDEs, signal processing
  - Ch 14: Nonlinear dynamics, hysteresis
  - Ch 15: Statistics, Monte Carlo
- **SL** Ch 3: SymPy for symbolic computation
- **OECD** Ch 12: AI for mathematics (Williamson)
- **OECD** Ch 19: AI in scientific discovery challenges
- *Gap:* PySR symbolic regression, PINNs -- requires MIT SciML textbook (Rackauckas) and original examples

---

### Chapter 7: Data Pipelines and Automation
*Stop doing manually what a script can do in seconds*

**Content:**
- The data pipeline concept: ingestion -> cleaning -> transformation -> analysis -> output
- Identifying automation opportunities in your workflow
- Data ingestion from files, databases, APIs, sensors
- Cleaning, validation, quality assessment
- Batch processing at scale
- Scheduled tasks and monitoring
- Pipeline tools: simple scripts -> Dagster -> Nextflow
- Reproducibility: containerization, environment management, documentation

**Reference sources:**
- **NASA** CMR connector, data pipelines (primary technical reference)
- **KH** Ch 5: Workflow transformation, RPA to GenAI agents
- **OECD** Ch 17: Federated learning and data privacy (data handling)
- **OECD** Ch 18: Robotic labs and autonomous experimentation
- **NAS** Ch 5: Importance of data, data provenance, AI-compatible datasets
- **SL** Ch 7: Chemical kinetics with Pandas DataFrames (data processing)

---

## PART III: From No-Code to Domain-Specific AI
*"From generic AI to your AI"*

### Chapter 8: Visual Programming and Workflow Design
*Build AI workflows by dragging and dropping -- no syntax required*

**Content:**
- Why visual programming appeals to scientists
- n8n: general-purpose visual automation
- LangFlow: visual LLM pipeline design
- Node-RED: IoT and sensor data workflows
- KNIME and Orange: visual data science
- Combining visual and code-based approaches

**Reference sources:**
- **NASA** LangFlow/Promptlab section (visual RAG prototyping)
- *Weak coverage:* No reference book covers visual programming for science specifically
- *Gap:* n8n, Node-RED, KNIME/Orange for research -- requires original tutorials and testing

---

### Chapter 9: RAG -- Teaching AI Your Own Data
*Make AI an expert in YOUR research domain*

**Content:**
- The limitation of general AI: it doesn't know your data
- RAG architecture: loading, chunking, embedding, vector stores, retrieval, generation
- Building a chatbot for your research documents
- Semantic search over controlled vocabularies
- Evaluating RAG quality: BERTScore, ROUGE, 3-tier framework
- Fine-tuning when RAG isn't enough (small datasets can work)

**Reference sources:**
- **NASA** OSDR evaluation notebook, EJ notebooks, gpt_embedder (PRIMARY technical source)
- **KH** Ch 2: RAG vs. Agentic RAG distinction
- **OECD** Ch 6: Semantic analysis for finding research
- **OECD** Ch 20: Machine reading challenges
- **OECD** Ch 23: Elicit -- language models as research tools
- **OECD** Ch 28: Knowledge bases for AI in science

---

### Chapter 10: Digital Twins -- Virtual Replicas of Real Systems
*Merge your models with real-time data*

**Content:**
- What are digital twins and why scientists need them
- Architecture: data -> model -> visualization -> feedback
- Platforms: NVIDIA Omniverse, Ansys TwinAI, interTwin (EU), open-source
- Building a simple digital twin with AI assistance
- Domain examples: environmental, industrial, biological, infrastructure
- The Debrecen connection: Automotive & AI Institute, BMW factory

**Reference sources:**
- **KH** Ch 11: Robotics, simulation (NVIDIA Isaac Sim, spatial intelligence)
- **OECD** Ch 15: AI for earth and environmental sciences
- **OECD** Ch 18: Robotic labs and autonomous experimentation
- *Weak coverage:* No reference book covers scientific digital twins specifically
- *Gap:* interTwin platform, NVIDIA Omniverse for science -- requires original research

---

## PART IV: Agentic AI -- From Tools to Teammates
*"From using AI to collaborating with AI"*

### Chapter 11: Understanding AI Agents
*What makes AI "agentic" -- and why it matters for science*

**Content:**
- From tools to agents: the autonomy spectrum
- Huang's 10 characteristics and 7-layer architecture
- Mollick's Centaur vs. Cyborg modes
- The ReACT pattern: Thought -> Action -> Observation -> repeat
- Tool use and MCP (Model Context Protocol)
- Multi-agent systems: coordination, communication, conflict resolution
- Safety, guardrails, and human-in-the-loop
- The AI agent economy: costs, access, fairness

**Reference sources:**
- **KH** Ch 1-4: PRIMARY source for agent theory
  - Ch 1: 10 characteristics, taxonomy, history
  - Ch 2: 7-layer architecture, frameworks, RAG
  - Ch 3: Multi-agent coordination, protocols, conflict resolution
  - Ch 4: AI agent economy, blockchain, tokens
- **EM** Ch 6: Centaur vs. Cyborg work modes, Jagged Frontier
- **NASA** ReACT agent notebooks (astro + CMR agents)
- **KH** Ch 12: Safety, OWASP Top 10, alignment drift

---

### Chapter 12: Building AI Agents for Research
*Your first agent that actually does useful work*

**Content:**
- Agent frameworks: CrewAI, LangGraph, AutoGen, Claude Agent SDK
- Building research agents: literature review team, data pipeline, experiment monitor
- Connecting agents to data and tools via MCP
- End-to-end agentic research workflows
- Monitoring and debugging agent systems

**Reference sources:**
- **KH** Ch 2: Frameworks comparison (AutoGen, LangGraph, LlamaIndex, AutoGPT)
- **KH** Ch 3: Multi-agent systems design and coordination
- **KH** Ch 5: Business workflow agents (adapted for research)
- **NASA** agent.py, chains.py architecture (primary code reference)
- **OECD** Ch 22: Combining collective and machine intelligence
- **OECD** Ch 5: AI for scientific discovery (autonomous experimentation)

---

### Chapter 13: Creating Your Own Programs and Tools
*From scripts to applications your colleagues can use*

**[v3 SLIMMED per Codex Rec 5]**

**Content (kept):**
- When your research needs custom software
- Building interfaces: Streamlit and Gradio (web apps in minutes)
- Creating MCP servers: making your data/tools AI-accessible
- Publishing to GitHub with documentation

**Removed (covered elsewhere or too developer-focused):**
- ~~AI-assisted program design~~ (covered in Ch 5)
- ~~Docker/pip packaging~~ (moved to Appendix A)
- ~~Open-source best practices~~ (too developer-focused)
- ~~API design for agents~~ (too developer-focused)

**Reference sources:**
- **KH** Ch 5: Workflow to software, deployment
- **NASA** Code modules (architectural patterns)
- *Weak coverage:* Streamlit/Gradio for science not covered in any reference
- *Gap:* MCP server creation tutorials -- requires original content

---

## PART V: Leading Responsible AI Adoption
*"From personal adoption to institutional transformation"*

### Chapter 14: The AI-Augmented Research Lab
*Designing your complete AI-powered workflow*

**Content:**
- The 2026 scientific AI stack: what goes where
- Cost management: free tiers -> subscriptions -> API budgets -> HPC
- Computing resources: laptop -> cloud -> Komondor supercomputer
- Data security and privacy: cloud vs. local, GDPR, EU AI Act
- **[NEW v3] AI procurement guidance:**
  - Platform selection criteria for research institutions
  - EU Model Contractual Clauses for AI (MCC-AI)
  - EDUCAUSE procurement checklist adapted for European universities
  - Total cost of ownership analysis
- Team collaboration: sharing workflows, training colleagues
- Measuring AI impact: time saved, quality improved, new capabilities

**Reference sources:**
- **EUA** Ch 2: Institutional strategies for AI adoption
- **EUA** Ch 4: Regulation and compliance (EU AI Act, procurement)
- **KH** Ch 5: Business workflow transformation (adapted for lab)
- **KH** Ch 4: AI agent economy (costs, access)
- **OECD** Ch 27: AI for science as priority for public R&D
- **OECD** Ch 29: HPC leadership for AI
- **OECD** Ch 17: Federated learning and data privacy
- **NAS** Ch 4: Promoting and protecting AI-enabled innovation
- *Additional:* EDUCAUSE/ACE procurement report, EU MCC-AI clauses

---

### Chapter 15: AI in the University -- Teaching, Learning, and Institutional Transformation
*What works, what doesn't, and what to do next*

**[v3 EXPANDED with teaching section and change management per Codex Rec 4]**

**Content:**

**15.1 University case studies (reframed as transferable models):**
- University of Florida: AI Across the Curriculum -- embed AI in every discipline
- University of Helsinki: Elements of AI -- accessibility drives mass adoption
- Northeastern: Campus-wide Claude -- deploy one platform, measure impact
- Johns Hopkins: Agentic AI Certificate -- structured progressive learning

**15.2 [NEW] AI in Teaching and Supervision:**
- Course preparation with AI: syllabi, readings, lecture materials
- Assessment design: avoiding the "homework apocalypse"
- The SARPS framework for assessment redesign
- AI-assisted thesis and dissertation supervision
- Student AI policies: what to allow, what to require, what to prohibit
- AI as Socratic tutor: Bloom's 2-sigma problem at scale
- Practical examples from Khanmigo and Claude for Education

**15.3 [NEW] Change Management for AI Adoption:**
- Faculty resistance: understanding and addressing concerns
- Uneven digital skills across disciplines
- Rogers' Diffusion of Innovations applied to universities (Polish study data)
- Incentive structures: how to reward AI integration
- Training models: workshops, communities of practice, peer mentoring
- The EUA participative approach: whole-community engagement

**15.4 A Roadmap for the University of Debrecen:**
- What Debrecen has: assets and strengths
- What Debrecen needs: gaps and priorities
- A three-phase AI transition plan
- How this book fits into the curriculum

**Reference sources:**
- **SK** entire book: PRIMARY source for teaching with AI
  - Ch 1-3: AI tutoring, Khanmigo development, global deployment
  - Ch 7-8: STEM with AI, math accessibility
  - Ch 14-16: Teaching in AI age, AI teaching assistants, cheating/assessment
  - Ch 17-18: Global equity, economics of AI in education
  - Ch 19-20: Future of assessments, college admissions
- **EM** Ch 7: AI as tutor, Bloom's 2-sigma, homework apocalypse
- **EM** Ch 8: AI as coach, expertise development, skill gaps
- **EUA** Ch 1: Ethics, principles, values for universities
- **EUA** Ch 2: Institutional strategies (PRIMARY for change management)
- **EUA** Ch 3: Training (faculty and staff)
- **EUA** Ch 5: Sustainability and societal impact
- **OECD** Ch 24: Democratising AI to accelerate discovery
- **OECD** Ch 25: Narrowing of AI research (diversity concerns)
- **OECD** Ch 31: AI and scientific productivity policy
- *Additional:* Teaching with AI (Bowen, JHU Press), Generative AI in Higher Education (Chan & Colloton, free), Polish academics adoption study

---

### Chapter 16: Ethics, Reproducibility, and the Future of AI in Science
*Responsible AI use and where this is all heading*

**[v3 EXPANDED: consolidated ethics treatment + research integrity per Codex Rec 2 & 4]**

**Content:**

**16.1 [EXPANDED] Research Integrity in the AI Age:**
- Fabricated citations and hallucinated references
- AI-generated image manipulation and detection
- Synthetic data misuse: when generated data passes as real
- Detection tools: AI-generated text detectors, image forensics
- The "postplagiarism" concept: hybrid human-AI writing as the new norm
- Statistics: ~13.5% of PubMed papers in 2024 showed LLM signatures
- Biosecurity considerations: AI-enabled biological design risks

**16.2 AI Ethics in Scientific Research (consolidated from Ch 3, 14):**
- Attribution and authorship: who wrote this paper?
- Bias in AI-generated analysis
- The EU AI Act: classification, obligations, compliance for researchers
- Journal policies on AI use (2026 landscape)
- COPE guidelines for AI in publishing

**16.3 Reproducibility in the Age of AI:**
- The reproducibility challenge: non-deterministic outputs
- Documenting AI-assisted workflows: what to record
- Version pinning, prompt logging, seed fixing
- Writing the "AI Methods" section in your papers
- Sharing prompts, configs, and agent definitions

**16.4 Principles for Responsible AI in Science:**
- NASA's 5 principles: Transparency, Trust, Teamwork, Training, Techniques
- Mollick's four rules revisited as ethical guardrails
- EUA values-based approach to AI adoption
- Building a personal AI ethics framework

**16.5 Where This Is All Heading:**
- Four scenarios: Stagnation, Slow Growth, Exponential Growth, AGI
- Fully autonomous scientific discovery: promise and peril
- The scientist's evolving role: from doing to directing to collaborating
- Your first steps after finishing this book

**Reference sources:**
- **EM** Ch 2: Alignment problem, bias, RLHF, safety
- **EM** Ch 9: Four future scenarios, disinformation, AGI
- **HQ** Ch 13: Pitfalls -- hallucination, randomness, bibliographic errors
- **HQ** Ch 14: Recommendations for researchers and developers
- **KH** Ch 12: Agent safety, OWASP Top 10, governance framework
- **KH** Ch 6-7: Offensive/defensive security (misuse context)
- **EUA** Ch 1: Ethics, principles, values
- **EUA** Ch 4: Regulation and compliance
- **EUA** Ch 5: Sustainability and societal impact
- **NAS** Ch 3: AI-enabled biological design and biosecurity risks
- **NAS** Ch 4: Promoting and protecting innovation
- **OECD** Ch 30: Improving reproducibility of AI research (PRIMARY for reproducibility)
- **OECD** Ch 31: AI policy and governance for science
- **OECD** Ch 26: Lessons from ML shortcomings in medical imaging
- *Additional:* AI Snake Oil (Narayanan & Kapoor), Science Fictions (Ritchie), Second Handbook of Academic Integrity (Eaton)

---

## APPENDICES

### Appendix A: Setting Up Your AI Research Environment
- Python, git, VS Code, Claude Code, Cursor installation
- API keys and account setup
- Komondor supercomputer access (Debrecen users)
- **[NEW v3] Docker and pip packaging** (moved from Ch 13)
- Recommended hardware and cloud options
- Troubleshooting common issues

### Appendix B: Prompt Library for Scientists (50+ Prompts)
- Literature review and synthesis (10)
- Writing and editing (10)
- Data analysis and visualization (10)
- Experimental design (5)
- Code generation and debugging (10)
- Agent instructions and system prompts (5)
- Based on NASA's 9 patterns + extensions

### Appendix C: Resources and Further Reading
- Key books (annotated, with what to read from each)
- Key papers
- Online courses and certifications
- Communities and forums
- Hungarian-language resources (PULI GPT, HuSpaCy, AI Coalition)
- **[NEW v3] Discipline-specific book recommendations** (from RECOMMENDED_BOOKS_MISSING_TOPICS.md)

---

## COMPLETE CROSS-REFERENCE: What Comes From Where

### Primary Reference Mapping

| Our Chapter | HQ (ChatGPT) | EM (Co-Intelligence) | KH (Agentic AI) | SL (Python/SciComp) | SK (Brave New Words) | EUA (Universities) | NAS (Life Sciences) | OECD (AI in Science) | NASA Cookbook |
|---|---|---|---|---|---|---|---|---|---|
| 1. AI Revolution | Ch 1 (basics) | Ch 1-3 (framework) | Ch 1 (spectrum) | -- | -- | -- | Ch 1 (context) | Ch 1-5 (science harder) | Motivation |
| 2. Conversational AI | Ch 1 (LLMs) | Ch 3 (four rules) | -- | -- | -- | -- | -- | Ch 21, 26 (evidence) | 9 patterns |
| 3. Scientific Writing | **Ch 2-12 (PRIMARY)** | Ch 5 (creativity) | -- | -- | -- | -- | -- | Ch 6-8 (search, review) | -- |
| 4. Data Analysis | Ch 9-10 (design) | -- | -- | Ch 4-5, 8, 15 (stats) | -- | -- | -- | Ch 9 (overview) | -- |
| 5. Coding Assistants | -- | -- | Ch 5 (workflows) | **Sec I (PRIMARY)** | -- | -- | -- | -- | Code arch |
| 6. Math Modeling | -- | -- | -- | **Sec II (PRIMARY)** | -- | -- | -- | Ch 12, 19 (math, discovery) | -- |
| 7. Data Pipelines | -- | -- | Ch 5 (workflows) | Ch 7 (Pandas) | -- | -- | Ch 5 (data) | Ch 17-18 (privacy, labs) | CMR connector |
| 8. Visual Programming | -- | -- | -- | -- | -- | -- | -- | -- | LangFlow |
| 9. RAG | -- | -- | Ch 2 (RAG) | -- | -- | -- | -- | Ch 6, 20, 23, 28 (search) | **OSDR+EJ (PRIMARY)** |
| 10. Digital Twins | -- | -- | Ch 11 (robotics) | -- | -- | -- | -- | Ch 15, 18 (earth, labs) | -- |
| 11. Understanding Agents | -- | Ch 6 (Centaur) | **Ch 1-4 (PRIMARY)** | -- | -- | -- | -- | Ch 22 (collective) | ReACT agents |
| 12. Building Agents | -- | -- | **Ch 2-3 (PRIMARY)** | -- | -- | -- | -- | Ch 5, 22 (discovery) | agent.py |
| 13. Creating Tools | -- | -- | Ch 5 (deploy) | -- | -- | -- | -- | -- | Code modules |
| 14. AI-Augmented Lab | -- | Ch 8 (coaching) | Ch 4-5 (economy) | -- | -- | **Ch 2, 4 (strategy)** | Ch 4 (innovation) | Ch 17, 27, 29 (HPC) | Best practices |
| 15. University/Teaching | -- | Ch 7-8 (tutor/coach) | -- | -- | **Entire (PRIMARY)** | **Ch 1-3, 5 (PRIMARY)** | -- | Ch 24-25, 31 (policy) | -- |
| 16. Ethics & Future | Ch 13-14 (pitfalls) | Ch 2, 9 (align, future) | Ch 12 (safety) | -- | Ch 13 (guardrails) | **Ch 1, 4-5 (PRIMARY)** | Ch 3-4 (biosecurity) | **Ch 26, 30-31 (PRIMARY)** | Ethics |

---

## MISSING TOPICS INTEGRATION SUMMARY

| Missing Topic (from Codex) | Where Added | Source Material |
|---|---|---|
| **Research integrity** | Ch 16.1 (expanded) | AI Snake Oil, Science Fictions, OECD Ch 30, NAS Ch 3, Sharon Kabel tracker |
| **Discipline pathways** | Ch 4 end (pathway map) + "In your field" boxes throughout | OECD domain chapters, NAS, discipline-specific books in Appendix C |
| **Evidence quality** | Ch 2.5 (expanded verification) | AI Snake Oil, OECD Ch 21/26, Microsoft Research critical thinking study |
| **Procurement** | Ch 14 (new section) | EUA Ch 2/4, EDUCAUSE/ACE report, EU MCC-AI clauses |
| **Teaching** | Ch 15.2 (major new section) | SK (entire), EM Ch 7-8, EUA Ch 3, Teaching with AI (Bowen), SARPS framework |
| **Change management** | Ch 15.3 (new section) | EUA Ch 2-3, Polish academics study, OECD Ch 31, BCG 70% statistic |

---

## GAP ANALYSIS TABLE

| Ch # | Chapter Title | Reference Sources Available | Coverage | What's Missing / Needs Original Research | Priority |
|---|---|---|---|---|---|
| 1 | The AI Revolution in Scientific Research | EM, KH, OECD, NAS, HQ, SK | **Strong** | Debrecen-specific context (original research). AI breakthroughs updated to 2026. | Low |
| 2 | Conversational AI -- Your First Research Partner | NASA, HQ, EM, OECD | **Strong** | 2026 platform comparison (Claude, ChatGPT, Gemini landscape evolves fast). Evidence quality assessment framework needs original synthesis from AI Snake Oil + Microsoft Research study. | Medium |
| 3 | AI for Scientific Writing and Communication | **HQ (entire book)**, EM, OECD | **Strong** | Journal AI policies (2026 update needed). Citation hallucination detection tools (rapidly evolving). | Low |
| 4 | AI for Data Analysis -- No Coding Required | HQ, SL | **Adequate** | Chat-based data analysis tutorials with real datasets (no book covers this workflow specifically). Platform-specific capabilities change rapidly. | Medium |
| 5 | AI Coding Assistants | SL, NASA, KH | **Weak** | No reference book covers AI coding assistants for scientists (Claude Code, Cursor, Copilot). This is entirely original content requiring hands-on testing and comparison. The Python fundamentals come from Lynch but the AI-assisted workflow is new. | **High** |
| 6 | Math Modeling and Simulation | **SL (entire Section II)**, OECD | **Adequate** (core) / **Weak** (advanced) | Core sections well-covered by Lynch. Advanced sections (PySR, PINNs, surrogate models) need MIT SciML textbook + original examples. LLM-guided symbolic regression is cutting-edge with limited published material. | Medium |
| 7 | Data Pipelines and Automation | NASA, KH, OECD, NAS, SL | **Adequate** | Pipeline tool tutorials (Dagster, Nextflow) need original content. Sensor/IoT data ingestion for science not well covered. | Medium |
| 8 | Visual Programming and Workflow Design | NASA (LangFlow only) | **Weak** | No reference book covers n8n, Node-RED, KNIME, or Orange for scientific research. NASA covers LangFlow briefly. Entire chapter needs original tutorials, screenshots, and worked examples. | **High** |
| 9 | RAG -- Teaching AI Your Own Data | **NASA (PRIMARY)**, KH, OECD | **Strong** | NASA provides complete technical foundation. Needs adaptation from NASA-specific to domain-general science. Vector store landscape evolves rapidly. | Low |
| 10 | Digital Twins | KH (partial), OECD (partial) | **Weak** | No reference book covers scientific digital twins comprehensively. KH covers robotics/simulation tangentially. interTwin platform documentation, NVIDIA Omniverse for science, and domain examples all need original research. Debrecen BMW case needs local reporting. | **High** |
| 11 | Understanding AI Agents | **KH (PRIMARY)**, EM, NASA | **Strong** | MCP ecosystem documentation (rapidly evolving, 2025-2026). A2A protocol (Google, very new). Otherwise excellent coverage from Huang. | Low |
| 12 | Building AI Agents for Research | **KH (PRIMARY)**, NASA, OECD | **Adequate** | Framework comparison needs hands-on testing (CrewAI, LangGraph, AutoGen, Claude Agent SDK -- landscape shifts quarterly). Research-specific agent examples need original development. | Medium |
| 13 | Creating Your Own Programs and Tools | KH, NASA | **Weak** | Streamlit/Gradio for science not covered anywhere. MCP server creation tutorials are original content. Slimmed chapter reduces the gap somewhat. | Medium |
| 14 | The AI-Augmented Research Lab | EUA, KH, OECD, NAS | **Adequate** | 2026 AI stack specifics (costs, platform features) need original benchmarking. Procurement guidance needs synthesis from EDUCAUSE + EU MCC-AI + EUA. Komondor access guide is Debrecen-specific. | Medium |
| 15 | AI in the University: Teaching, Learning, and Institutional Transformation | **SK (PRIMARY)**, **EUA (PRIMARY)**, EM, OECD | **Strong** | University case studies need original reporting (UF, Helsinki, Northeastern, JHU). Teaching section well-sourced from SK + EM but needs adaptation for research university context. Change management needs synthesis from EUA + Polish study + BCG data. Debrecen roadmap entirely original. | Medium |
| 16 | Ethics, Reproducibility, and the Future | **OECD (PRIMARY)**, **EUA (PRIMARY)**, EM, HQ, KH, NAS | **Strong** | Research integrity section is new and needs synthesis from AI Snake Oil + Science Fictions + recent papers. "Postplagiarism" concept needs Eaton's Handbook. Biosecurity from NAS. Reproducibility well-covered by OECD Ch 30. Future scenarios from Mollick. | Low |
| App A | Setting Up Environment | SL | **Adequate** | Installation guides need original writing for 2026 tools. Docker/pip packaging (moved from Ch 13) needs original content. | Low |
| App B | Prompt Library | NASA, HQ | **Strong** | 9 NASA patterns + HQ examples provide foundation. Domain-general adaptation needed. | Low |
| App C | Resources | All books | **Strong** | Discipline-specific recommendations from RECOMMENDED_BOOKS_MISSING_TOPICS.md ready to integrate. Hungarian resources need original curation. | Low |

---

## GAP PRIORITY SUMMARY

### High Priority Gaps (need significant original content):
1. **Ch 5: AI Coding Assistants** -- No reference covers this workflow. Requires hands-on comparison of Claude Code, Cursor, Copilot, Windsurf, Codex for scientific tasks.
2. **Ch 8: Visual Programming** -- Almost no reference material. Requires building and documenting original n8n, KNIME, Orange workflows for research.
3. **Ch 10: Digital Twins** -- No comprehensive scientific digital twin reference. Requires original research on interTwin, Omniverse, and domain-specific examples.

### Medium Priority Gaps (need moderate original content):
4. **Ch 2: Evidence quality** -- Framework needs synthesis from multiple non-book sources.
5. **Ch 4: Chat-based data analysis** -- Workflow tutorials need original development.
6. **Ch 6 Advanced: PySR, PINNs** -- Cutting-edge material with limited published guides.
7. **Ch 7: Pipeline tools** -- Dagster/Nextflow tutorials for science need original writing.
8. **Ch 12: Research agent examples** -- Framework landscape shifts rapidly; needs current testing.
9. **Ch 13: Streamlit/Gradio, MCP servers** -- Practical tutorials need original development.
10. **Ch 14: Procurement** -- Synthesis from multiple policy sources needed.
11. **Ch 15: Case studies, Debrecen roadmap** -- Original reporting and synthesis required.

### Low Priority Gaps (well-sourced, need only adaptation/updating):
12. **Ch 1, 3, 9, 11, 16, Appendices** -- Strong reference coverage; mainly need 2026 updating and domain-general adaptation.

---

## PRODUCTION NOTES

- **Estimated length:** ~350-400 pages
- **Chapters:** 16 (unchanged from v2)
- **Format per chapter:**
  - Real-world scientific scenario as opener
  - Conceptual explanation (minimal theory, maximum intuition)
  - Step-by-step hands-on walkthrough
  - "In your field" boxes (discipline-specific adaptations) -- NEW in v3
  - "Try it yourself" exercises
  - "What can go wrong" troubleshooting
  - Key takeaways (3-5 bullets)
  - "Going deeper" references to source books
- **Companion repository:** GitHub with all code, notebooks, prompt templates
- **Language:** English (primary), potential Hungarian translation
- **Publisher targets:** Springer Nature (academic credibility) or CRC Press (practical focus)

---

## VERSION HISTORY

| Version | Date | Key Changes |
|---------|------|-------------|
| v1 | 2026-03-25 | Initial 19-chapter structure |
| v2 | 2026-03-27 | Reduced to 16 chapters; added RAG, scientific writing, lit review; integrated Mollick/Huang/Lynch; strengthened Debrecen thread |
| v3 | 2026-03-29 | Incorporated Codex review (pathway map, core/advanced split, ethics consolidation, slimmed Ch 13, teaching section, part names); mapped all 8 reference books; added 6 missing topics; full gap analysis with 3 reference books newly integrated (EUA, NAS, OECD) |
