# Agentic AI for Scientists
## A Practical Guide to AI-Powered Research

**Target audience:** Scientists, researchers, and faculty members who are NOT programmers but want to leverage AI tools effectively in their research workflows.

**Positioning:** No book currently exists that covers the full journey from basic AI chat through agentic coding tools to automated scientific pipelines and digital twins — specifically for scientists. This fills a genuine market gap.

**Context:** Supports the AI transition at the University of Debrecen, aligned with Hungary's National AI Strategy 2025-2030.

---

## PART I: FOUNDATIONS — Understanding and Using AI as a Scientist
*"From curious to competent"*

### Chapter 1: The AI Revolution in Science
- Why AI matters for every scientist, not just computer scientists
- The spectrum: from assistant to autonomous agent
- How AI is already transforming research (examples from physics, biology, earth science, engineering)
- Case studies: Berkeley Lab's A-Lab, Google Co-Scientist, Sakana AI's AI Scientist
- The University of Debrecen context and Hungary's AI strategy
- What this book will (and won't) teach you

### Chapter 2: Conversational AI — Your First Research Partner
- Understanding LLMs: what they are, what they can and cannot do
- Choosing your platform: ChatGPT, Claude, Gemini, Copilot — strengths and trade-offs
- The art of prompting for scientific work
  - Structuring complex scientific questions
  - Few-shot prompting with domain examples
  - Chain-of-thought for multi-step reasoning
  - System prompts and persona setting
- Practical workflows:
  - Literature review and synthesis
  - Brainstorming hypotheses
  - Explaining unfamiliar concepts across disciplines
  - Writing and editing manuscripts, abstracts, grant proposals
  - Responding to peer reviewers
- Ethics, hallucinations, and verification strategies
- Hands-on exercises for each workflow

### Chapter 3: AI for Data Work — No Coding Required
- Uploading and analyzing datasets through chat interfaces
  - CSV, Excel, images, PDFs
- AI-powered data visualization and exploration
- Statistical analysis through conversation
- Using ChatGPT Advanced Data Analysis (Code Interpreter)
- Claude's Artifacts for interactive outputs
- When chat-based analysis reaches its limits

---

## PART II: THE COMMAND LINE — Unlocking AI's Full Power
*"From clicking to commanding"*

### Chapter 4: Why the Terminal Matters for Scientists
- The gap between web interfaces and real research workflows
- Setting up your environment (Python, package managers, virtual environments)
- Terminal basics for the non-programmer
- The paradigm shift: describing what you want vs. clicking through menus

### Chapter 5: AI Coding Assistants — Writing Code Without Being a Programmer
- The landscape: Claude Code, GitHub Copilot, Cursor, Windsurf, OpenAI Codex
- How AI coding assistants work: context, generation, iteration
- Setting up Claude Code / Cursor for scientific work
- Your first AI-assisted Python script
  - Reading and cleaning a dataset
  - Creating publication-quality figures
  - Running a statistical test
  - Fitting a model to data
- The feedback loop: describe → generate → test → refine
- Version control with git (AI-assisted)
- Practical exercises: 5 common research tasks solved with AI coding assistants

### Chapter 6: Python as a Scientific Language — AI as Your Translator
- Why Python dominates scientific computing
- Key libraries: NumPy, SciPy, Pandas, Matplotlib, scikit-learn
- Using AI to learn Python by doing, not by studying syntax
- Pattern: "I have this data and I want this result" → working code
- Managing environments and dependencies with AI help
- Jupyter notebooks as the scientist's lab notebook
- Connecting to databases and APIs

---

## PART III: AUTOMATION — From Manual Work to Intelligent Pipelines
*"From doing it yourself to having it done"*

### Chapter 7: Automating Repetitive Research Tasks
- Identifying automation opportunities in your workflow
- File processing: batch operations on data, images, documents
- Scheduled tasks and monitoring
- Web scraping for research data (ethical considerations)
- Email and notification automation
- Practical examples:
  - Automatically processing new sensor data as it arrives
  - Batch-converting file formats
  - Monitoring a website for new publications in your field

### Chapter 8: Data Pipelines — From Raw Data to Analysis-Ready
- What is a data pipeline and why you need one
- Data ingestion from multiple sources
- Cleaning, validation, and quality assessment
  - Handling missing values, outliers, format inconsistencies
  - Automated quality reports
- Feature engineering with AI assistance
- Reproducibility: ensuring others can run your pipeline
- Tools: Dagster, Nextflow, simple Python scripts
- Case study: building a complete data pipeline for a research project

### Chapter 9: Automatic Model Configuration and Calibration
- The model configuration challenge in science
- Hyperparameter optimization: grid search, Bayesian optimization, evolutionary methods
- AI-assisted parameter tuning
  - Using LLMs to suggest parameter ranges based on literature
  - Automated sensitivity analysis
- Tools: Optuna, Ray Tune, scikit-optimize
- Surrogate models for expensive simulations
- Case study: calibrating an environmental model with AI assistance

---

## PART IV: MATHEMATICAL MODELING WITH AI
*"From equations to running models"*

### Chapter 10: AI-Assisted Mathematical Modeling
- From research question to mathematical formulation
- Using AI to derive, verify, and simplify equations
- Translating equations into code with AI assistance
  - ODEs, PDEs, algebraic systems
  - Symbolic computation (SymPy) with AI guidance
- Dimensional analysis and unit checking with AI
- Equation discovery from data: symbolic regression with PySR
  - How it works: evolutionary search for mathematical expressions
  - Practical guide: from dataset to discovered equation
  - Validating discovered equations against domain knowledge
- Physics-Informed Neural Networks (PINNs): embedding physics into ML
- Case study: discovering governing equations from experimental data

### Chapter 11: Building Simulation Models with AI
- Designing simulation architectures with AI guidance
- Agent-based models for complex systems
- Monte Carlo simulations
- Stochastic and deterministic approaches
- Connecting models to real data for validation
- Performance optimization: when your model is too slow
- AI-assisted debugging of scientific code
- Case study: building a complete simulation from scratch using AI

### Chapter 12: Digital Twins — Virtual Replicas of Real Systems
- What are digital twins and why scientists need them
- Architecture: data sources → model → visualization → feedback loop
- Platforms: NVIDIA Omniverse, Ansys TwinAI, open-source alternatives
- The interTwin project: digital twins for science (EU initiative)
- Building a simple digital twin with AI assistance
  - Connecting sensor data to a model
  - Real-time visualization
  - Predictive capabilities
- Examples from different fields:
  - Environmental monitoring
  - Industrial processes
  - Biological systems
  - Infrastructure
- Case study: creating a digital twin for a laboratory experiment

---

## PART V: GRAPHICAL AND VISUAL PROGRAMMING
*"From text to visual workflows"*

### Chapter 13: Visual Programming for Scientists
- Why visual programming appeals to scientists
- Node-based workflow editors: the concept
- n8n: visual automation without code
  - Setting up workflows
  - Connecting data sources
  - Integrating AI reasoning (via Flowise)
- Langflow: visual LLM pipeline design
- Node-RED: IoT and sensor data workflows
- KNIME and Orange: visual data science
- When to use visual vs. text-based approaches
- Case study: building a complete research workflow visually

---

## PART VI: AGENTIC AI — THE FRONTIER
*"From tools to teammates"*

### Chapter 14: Understanding AI Agents
- What makes AI "agentic": autonomy, planning, tool use, memory
- The agent architecture: perception → reasoning → action → feedback
- Single agents vs. multi-agent systems
- The role of context: MCP (Model Context Protocol) and tool connectivity
- Safety, guardrails, and human-in-the-loop patterns
- When agents help and when they hinder

### Chapter 15: Building Your First AI Agent
- Agent frameworks for scientists: CrewAI, LangGraph, AutoGen
  - CrewAI: define agent teams with roles (easiest for non-programmers)
  - LangGraph: graph-based workflows (most flexible)
  - AutoGen: conversational agents (best for collaborative reasoning)
  - Claude Agent SDK: the professional-grade toolkit
- Setting up your first multi-agent system
- Connecting agents to your data and tools via MCP
- Practical examples:
  - Literature review agent team (searcher, reader, synthesizer)
  - Data processing agent pipeline
  - Experiment monitoring agent

### Chapter 16: Agentic Research Workflows
- Designing end-to-end agentic workflows for research
- The autonomous research pipeline:
  - Hypothesis generation
  - Experimental design
  - Data collection and monitoring
  - Analysis and interpretation
  - Report generation
- Multi-agent collaboration patterns for science
- Integrating human judgment at critical decision points
- Monitoring and debugging agent systems
- Case study: an agentic system that runs a complete research sub-task

### Chapter 17: Creating Your Own Programs and Tools with AI
- From scripts to applications: when your research needs custom software
- AI-assisted program design and architecture
- Building CLIs, GUIs, and web interfaces with AI coding assistants
- Packaging and sharing your tools with colleagues
- Creating MCP servers: making your data and tools accessible to AI agents
- Open-source best practices for scientific software
- Case study: building and publishing a domain-specific research tool

---

## PART VII: PUTTING IT ALL TOGETHER
*"From learning to leading"*

### Chapter 18: The AI-Augmented Research Lab
- Designing your personal AI-augmented workflow
- Combining tools: a practical scientific stack for 2026+
  - Claude Code / Cursor for interactive work
  - CrewAI / LangGraph for custom agents
  - n8n / Flowise for visual automation
  - PySR for equation discovery
  - Dagster / Nextflow for data pipelines
  - MCP for connecting everything
- Cost management: free tiers, subscriptions, API budgets
- Data security and privacy considerations
- Collaboration: sharing AI workflows with your team

### Chapter 19: Ethics, Reproducibility, and the Future
- AI ethics in scientific research
  - Attribution and authorship
  - Bias in AI-generated analysis
  - The EU AI Act and what it means for researchers
- Reproducibility in the age of AI
  - Documenting AI-assisted workflows
  - Version pinning and prompt logging
  - The "AI methods" section in your papers
- Where this is all heading: fully autonomous scientific discovery
- Your role as a scientist in the AI era

### Appendix A: Setting Up Your AI Research Environment
- Step-by-step installation guides (Windows, Mac, Linux)
- Python, git, Claude Code, Cursor, VS Code
- API keys and account setup
- Recommended hardware and cloud options

### Appendix B: Prompt Library for Scientists
- 50+ tested prompts organized by research task
- Templates for common scientific workflows

### Appendix C: Resources and Further Reading
- Key books, papers, and online courses
- University programs and certifications
- Communities and forums

---

## KEY REFERENCE BOOKS

### Directly Relevant (should read/reference)
1. **"ChatGPT in Scientific Research and Writing"** — Han & Qiu (Springer, 2024). Closest existing book; covers chat-based AI for researchers. Your book extends far beyond this.
2. **"Co-Intelligence: Living and Working with AI"** — Ethan Mollick (2024). NYT bestseller, the philosophical framework for human-AI collaboration.
3. **"Learn AI-Assisted Python Programming"** — Porter & Zingaro (Manning, 2025). AI-assisted coding for beginners. Relevant but targets general audience.
4. **"Agentic AI: Theories and Practices"** — Ken Huang (Springer, 2025). The agentic AI reference, but from a business perspective.
5. **"Python for Scientific Computing and AI"** — Stephen Lynch (CRC, 2024). Python + AI + science intersection.
6. **"Digital Twins: Core Principles and AI Integration"** — Tekinerdogan & Verdouw (Elsevier, 2024). Digital twin reference.

### Key Papers
7. **"Agentic AI for Scientific Discovery: A Survey"** (ICLR 2025) — arxiv.org/html/2503.08979v1
8. **"Ten Simple Rules for AI-Assisted Coding in Science"** — Poldrack Lab (Stanford)
9. **"Towards End-to-End Automation of AI Research"** (Nature, 2026)
10. **"The (R)evolution of Scientific Workflows in the Agentic AI Era"** (SC'25, Oak Ridge)

### Free/Open Resources
11. **Elements of AI** (University of Helsinki) — elementsofai.com
12. **NASA LLM Cookbook for Open Science** — github.com/NASA-IMPACT/LLM-cookbook-for-open-science
13. **Springer Nature AI eBook Collection** — 70+ open-access AI books

---

## UNIVERSITY CONTEXT

### University of Debrecen — Existing AI Initiatives
- "Modern Artificial Intelligence" elective course (launched Feb 2025, 13 weeks, open to all faculties)
- AI Expert Postgraduate Diploma (1 year, Faculty of Informatics, English-language)
- Cross-border collaboration with University of Oradea on AI in finance/business
- Industry partnerships: Bosch, EPAM, GE, Microsoft, NI, NVIDIA

### Model Programs to Study
- **University of Florida**: "AI Across the Curriculum" — $70M NVIDIA partnership, 230 AI-integrated courses
- **University of Helsinki**: Elements of AI — 2M+ enrollments, free MOOC
- **Northeastern University**: Anthropic/Claude campus partnership — 50,000 users
- **Johns Hopkins**: Agentic AI Certificate Program — 16 weeks, most relevant curriculum
- **Stanford HAI**: Human-Centered AI Institute

### Hungarian National Context
- Hungary AI Strategy 2025-2030 (AI4Business, AI4Society, AI4Technology)
- AI Coalition: 400+ members since 2018
- HUN-REN SZTAKI: applied AI research leadership

---

## PRODUCTION NOTES

- **Estimated length:** ~400-500 pages
- **Format:** Each chapter should include:
  - A real-world scientific scenario as opener
  - Conceptual explanation (minimal theory, maximum intuition)
  - Step-by-step hands-on walkthrough
  - "Try it yourself" exercises
  - "What can go wrong" troubleshooting section
  - Key takeaways
- **Code/prompts:** All examples available in a companion GitHub repository
- **Language:** English (primary), with potential Hungarian translation
- **Publisher targets:** Springer Nature (strongest in academic/scientific publishing), CRC Press, or self-published with university support
