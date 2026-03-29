# Multi-Version Book Strategy

## Branch Structure

```
master          — shared base: book plan, reference library, research, examples
├── hu-ebook    — Hungarian e-book for Debrecen AI transition
└── en-springer — English book for Springer/CRC publication
```

### master (shared)
- All reference books (books/)
- All research reports (research/)
- Book plans and structure (BOOK_PLAN_v3.md)
- Code examples (examples/)
- NASA cookbook (LLM-cookbook-for-open-science/)
- CLAUDE.md project instructions

### hu-ebook (Hungarian fork)
- Chapters written in Hungarian: `chapters/hu/`
- Target: MSc, PhD, academics, faculty leadership at University of Debrecen
- Purpose: AI transition support — education, research, management
- Format: e-book, no size limit per chapter
- All 16 chapters + appendices
- Debrecen-specific content expanded significantly
- Hungarian terminology glossary

### en-springer (English fork)
- Chapters written in English: `chapters/en/`
- Target: International scientific audience
- Purpose: Springer Nature or CRC Press publication
- Format: ~350-400 pages (publisher constraints)
- Tighter, more concise than Hungarian version

## Writing Workflow

1. Structural changes → commit to `master` (both versions inherit)
2. Hungarian chapter writing → commit to `hu-ebook`
3. English chapter writing → commit to `en-springer`
4. New reference books/research → commit to `master`
5. Periodically merge `master` into both branches to sync shared assets

## Hungarian Language Policy

### Use English terms for:
- LLM (nagy nyelvi modell — define once, then use LLM)
- RAG (visszakeresés-kiegészített generálás — define once, then use RAG)
- prompt, prompting, prompt engineering
- agent, multi-agent system
- pipeline
- digital twin (digitális iker — both forms acceptable)
- fine-tuning (finomhangolás — both forms acceptable)
- token, tokenizálás
- embedding, vektor
- API
- MCP (Model Context Protocol)
- framework
- machine learning / deep learning (gépi tanulás / mélytanulás — Hungarian OK here)
- chatbot
- workflow

### Hungarian grammar on English roots:
- "a promptot" (accusative)
- "az agentek" (plural)
- "a pipeline-ban" (inessive)
- "RAG-alapú" (adjective form)
- "LLM-mel" (instrumental)
- "fine-tuningolni" (verb form)

### Define on first use:
Every English technical term gets a parenthetical Hungarian explanation on its FIRST appearance in each chapter:
> "A RAG (Retrieval-Augmented Generation, vagyis visszakeresés-kiegészített generálás) lehetővé teszi..."

After first definition, use the English abbreviation only.

### Never force:
- Don't translate tool names (Claude Code, Cursor, KNIME, n8n)
- Don't translate company/organization names
- Don't translate established acronyms (AI, API, PDF, CSV)

## Key Differences Between Versions

| Aspect | Hungarian E-book | English Springer |
|--------|-----------------|------------------|
| Language | Hungarian + English terms | English |
| Audience | Debrecen MSc/PhD/faculty/leadership | International scientists |
| Purpose | AI transition support | Reference/practical guide |
| Length | No limit per chapter | ~350-400 pages total |
| Debrecen content | Heavily expanded | Present but not dominant |
| Teaching section (Ch 15) | Major focus (Hungarian HE context) | International case studies |
| Examples | Hungarian data, Hungarian APIs | Generic/international |
| Pricing/tools | HUF, Hungarian context | USD/EUR, international |
| Publication | Self-published e-book | Springer Nature |
| Timeline | Can start now, publish fast | Publisher review process |
