# Chapter 13: Management Challenges Introducing AI

## Summary

This chapter presents a provocative argument that AI coding tools fundamentally break the Agile methodology that dominates modern software development. Wienholt systematically examines each of the 14 Agile Manifesto principles and demonstrates how roughly half are incompatible with AI-generated code.

The author argues that Agile has been poorly implemented in practice -- organizations "adapt" Agile by dropping the hard parts, product managers are often unavailable for the required ceremonies, and the methodology has failed to provide meaningful metrics for tracking software quality and productivity. AI tools exacerbate these problems by enabling faster code generation without corresponding improvements in specification quality, testing coverage, or architectural coherence.

Key Agile principles broken by AI coding: Principle 2 (welcoming change) is complicated by non-deterministic LLM outputs; Principles 4 and 7 (daily business/developer collaboration and face-to-face communication) are disrupted when business stakeholders can interact directly with AI; Principle 5 (motivated individuals) is threatened when engineers face automation of their core skills; and Principle 14 (team reflection) is difficult when large code sections are AI-generated with limited team understanding.

The chapter examines measuring AI cost savings, noting the fundamental difficulty of measuring software productivity. Story points, lines of code, and other traditional metrics become even less meaningful when AI is involved. The author recommends tracking code churn (via tools like Code Maat), defect rates, and post-deployment metrics rather than trying to measure "AI productivity" directly.

The section on improving specification quality is particularly forward-looking, arguing that with AI handling more code generation, specifications must become more precise and prescriptive -- essentially reversing the Agile trend toward vague, conversational requirements. LLMs can help review and improve specifications by adding nonfunctional requirements, suggesting test cases, and identifying gaps.

## Key AI Coding Techniques

- **Specification review with LLMs**: Feed specifications into ChatGPT/Claude to check quality, add nonfunctional requirements, and suggest test cases
- **Code churn analysis**: Use Code Maat (github.com/adamtornhill/code-maat) to track if AI adoption increases code instability
- **Nonfunctional requirement generation**: Prompt LLMs to add security, performance, scalability, and accessibility requirements to specifications
- **UI mockup from wireframe**: LLMs can generate UI code from hand-drawn wireframes, but quality is basic
- **Specification decomposition**: Use LLMs to break specifications into AI-implementable work items

## Practical Takeaways for Scientists

- If your team uses Agile/Scrum, be aware that AI tools will disrupt your existing processes
- **Invest more in specifications and documentation** -- AI tools work best with precise, detailed instructions
- Track code churn as an early indicator of problems with AI adoption -- increasing churn suggests poor specifications or low-quality AI output
- Measuring AI productivity is nearly impossible with current agile metrics; focus on end-to-end quality metrics instead
- Use LLMs to review your research software specifications for missing requirements (error handling, edge cases, performance constraints)
- The six dimensions of team performance (Value, Consistency, Quality, Quantity, Speed, Resilience) provide a better framework than velocity alone
- For research teams, the specification quality issue is critical: vague descriptions of analysis requirements lead to AI generating incorrect implementations
- Post-deployment metrics (customer satisfaction, incident frequency, fix time) are more meaningful than development-phase metrics

## Notable References

- Agile Manifesto Principles (agilemanifesto.org/principles.html)
- Code Maat tool for code churn analysis (github.com/adamtornhill/code-maat)
- "Six Dimensions of Performance" by Troy Magennis (circle.flightlevels.io)
- 17th State of Agile Report (71% of organizations use Agile in SDLC)
- World Economic Forum: 74.9% of organizations likely to adopt AI by 2027
- Atlassian advice on story point estimation
- Peter Senge, "The Fifth Discipline Fieldbook" (epigraph)
