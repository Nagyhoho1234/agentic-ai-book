# Chapter 9: Design of Experimental Studies

## Summary

This chapter evaluates one of the most productive potential uses of ChatGPT: designing experiments for research projects. The authors asked GPT-4 to design a study on microplastics in bottled water, then iteratively refined the design through follow-up questions. They also tested the model's ability to provide reference studies for a "reality check."

## Subsections

### 9.1 Designing Experiments and Refining Methods

**Initial design** (Table 24): Given a simple prompt ("Design an experiment for studying microplastics in bottled water"), GPT-4 provided:
- Step-by-step procedures with chemical reagents, consumables, and instruments
- Sample collection and preparation protocols
- Extraction and identification procedures
- Data analysis steps
- Quality assurance considerations

**Commendable aspects**: Selection of representative commercial products, QA/QC steps (replicates, method blanks), rational data recording procedures.

**Gaps identified by the authors** (as domain experts):
1. Infrared/Raman spectroscopy cannot identify plastic types for particles < 100 micrometers without specialized micro-FTIR or micro-Raman instruments.
2. Polymeric microfiltration membranes would interfere with Raman signals -- need inorganic membranes (aluminum oxide, glass microfiber) or metal coating.
3. Filter membrane surface smoothness is critical for micrometer-scale analysis.
4. Need for replicates and method blanks for quality control.

**Refinement** (Tables 25-26): Through follow-up questions, GPT-4 elaborated on:
- Micro-FTIR and micro-Raman spectroscopy for small particles
- Separating particle signals from membrane background
- Filter membrane material choices (PVDF, PTFE recommended)
- Atomic Layer Deposition (ALD) coating technique as a cost-effective alternative to expensive specialty membranes

### 9.2 Reality Check

The authors asked GPT-4 for reference studies to validate the experimental design (Table 27). The model provided 7 relevant studies with DOIs, methods, and key findings. Six of the first 6 references had been previously read by one of the authors, confirming their relevance.

**Limitation**: When asked for 30+ publications, the model provided only 7, acknowledging its knowledge cutoff. For extensive literature needs, the model suggests using Web of Science, Scopus, or Google Scholar.

### 9.3 Cautionary Note

Critical safety and ethical warnings:
- Always ask for reference studies after the experimental design to do a "reality check"
- Users must validate methods against published literature
- Follow lab safety protocols (MSDS, PPE) -- AI cannot take accountability
- Do NOT use AI to design experiments for illegal or harmful purposes (illicit drugs, toxic substances, explosives, biohazards)

## Workflow for AI-Assisted Experimental Design

1. Give a simple prompt for a general task list with step-by-step procedures
2. Request more details or clarifications on specific tasks
3. Request relevant reference studies for reality-checking
4. Optionally: ask for procurement lists of reagents, instruments, PPE, and QA/QC steps

## Practical Takeaways

- ChatGPT can provide a solid starting point for experimental design, especially for newcomers to a field.
- Always refine the initial design through iterative follow-up questions.
- The initial response may hide gaps under polished writing -- domain expertise is needed to spot them.
- Use the model's reference studies to cross-validate methods, but verify all bibliographic details.
- This approach is particularly useful for students and early-career researchers entering a new research area.

## Notable References

- Boiko et al. (2023) on emergent autonomous scientific research capabilities of LLMs
- Mason et al. (2018) "Synthetic polymer contamination in bottled water" -- Frontiers in Chemistry
- Schymanski et al. (2018) on microplastics in mineral water by micro-Raman spectroscopy
