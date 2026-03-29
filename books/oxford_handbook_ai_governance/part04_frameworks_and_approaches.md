# Section IV: Frameworks and Approaches for AI Governance

## Chapters in This Section

19. **Chapter 19** -- "The Challenge of AI Governance for Public Organizations" by Justin B. Bullock, Hsini Huang, Kyoung-Cheol Kim, and Matthew M. Young
20. **Chapter 20** -- "An Ecosystem Framework of AI Governance" by Bernd W. Wirtz, Paul F. Langer, and Jan C. Weyerer
21. **Chapter 21** -- "Governing AI Systems for Public Values" by Yu-Che Chen and Michael Ahn
22. **Chapter 22** -- "System Safety and Artificial Intelligence" by Roel I. J. Dobbe

---

## Comprehensive Summary

This section provides the most directly applicable theoretical and practical frameworks for organizations -- including universities -- that must integrate AI into their operations. The four chapters collectively answer the call for broad-based, integrated, and systems-oriented approaches to AI governance.

### AI Governance for Public Organizations -- Weber and Simon (Ch. 19)

Bullock, Huang, Kim, and Young provide one of the most university-relevant chapters in the entire handbook. They apply Max Weber's theory of bureaucracy and Herbert Simon's theory of administrative behavior to analyze how AI transforms public organizations.

**Weber's framework** identifies three threats from AI integration into bureaucracies:
1. **Decreased scope of tasks for human bureaucrats:** As AI takes over routine, protocol-defined tasks, human workers shift to cross-checks, coordination, and cross-boundary problems. This challenges Weber's division of labor.
2. **Loss of human managerial control:** AI introduces probabilistic, predictive discretion that competes with Weber's emphasis on formalized, rule-based control. Hierarchy, specialization, and formalization are all disrupted.
3. **Evolving bureaucracy:** Traditional roles shift from "street-level" to "screen-level" bureaucrats, with AI systems exercising what scholars call "artificial discretion."

**Simon's framework** highlights three complementary challenges:
1. **Reshaping bounded rationality:** AI agents have vastly different cognitive profiles than humans (superior memory and processing, but lacking contextual judgment and human norms). Hybrid human-AI teams present "different landscapes of boundedness."
2. **Value misalignment:** AI decisions inherently follow value systems unlikely to match those of the organization or its human agents. Cognitive biases and automation bias compound this problem.
3. **Changing formal/informal communication:** AI tools may improve information flow but can also disrupt trust and informal authority networks within organizations.

**Critical warning: Dehumanization and loss of control.** The authors warn that left unchecked, AI integration into public organizations could lead to unprecedented dehumanization and loss of human control. They recommend:
- Developing AI as bounded, controlled "Beamte" (professional agents) with explicit and tacit rules
- Using Weber's concepts of hierarchy, communication, and specialization to structure AI working tasks
- Applying Simon's careful identification of facts and values at every AI decision point
- Restricting AI to decisions that do not benefit from human judgment

### An Ecosystem Framework (Ch. 20)

Wirtz, Langer, and Weyerer develop an integrative, multi-level framework treating AI governance as an ecosystem with multiple interacting layers:
- **AI systems layer:** Technical capabilities (sensing, comprehension/learning, action) each requiring different governance approaches
- **AI governance challenges layer:** Issues emerging from AI deployment
- **Multi-stakeholder governance process:** Engaging government, industry, academia, and civil society in framing, assessment, evaluation, and management
- **AI governance mechanisms:** Specific tools and instruments
- **AI governance policy:** Overarching policy direction

The framework emphasizes that governance approaches must account for the **development stage** of AI capability -- not all AI requires the same governance, and simpler applications may need lighter touch. The more autonomous the AI, the more unspecific its scope and the greater the governance need.

**Three areas of AI governance concerns:**
- AI Sensing: access to data, non-biased data sources, privacy
- AI Comprehension/Learning: traceability, reproducibility, transparency of "black box," reliability
- AI Action: legality, responsibility, human control

### Governing AI for Public Values (Ch. 21)

Chen and Ahn provide a principle-based, process-oriented design framework for AI governance. Their principles are:
- **Human-centered:** AI serves human needs
- **Stakeholder-focused:** All affected parties have voice
- **Lifecycle-scoped:** Governance applies throughout the AI lifecycle

The governance process includes four phases:
1. **Goal setting** with clear public values
2. **Iterative development decisions** on data, models, and results
3. **Decisions on public service** application
4. **Assessment of impacts**

Three governance principles (transparency, accountability, fairness) are applied at each phase. This process-oriented approach makes recommendations actionable for individual AI systems rather than remaining abstract.

### System Safety and AI (Ch. 22)

Dobbe applies seven lessons from Nancy Leveson's system safety framework to AI governance, producing one of the most practically actionable chapters:

| Leveson Lesson | AI Safety Implication | Strategy |
|---|---|---|
| Component reliability is insufficient for safety | Identify hazards at system level | System hazard-informed design and safety control structure |
| Causal event models cannot capture system complexity | Understand safety through sociotechnical constraints | System-theoretic accident models |
| Probabilistic methods do not provide safety guarantees | Capture safety conditions in a system-theoretic way | Process model: goals, actions, observations |
| Operator error is a product of the environment | Align mental models across design, operation, and stakeholders | Redundancy, incremental control, error tolerance |
| Reliable software is not necessarily safe | Include AI software and organizational dependencies in hazard analysis | System-theoretic process analysis (STPA) |
| Systems migrate toward higher risk | Ensure operational safety through feedback | Audits, investigations, reporting systems |
| Blame is the enemy of safety | Build organizational culture open to understanding and learning | Just Culture |

The Dutch childcare benefits scandal (SyRI) serves as a cautionary case: an AI risk profiling system wrongly accused 26,000+ families of fraud, violating the European Convention on Human Rights. The system failed all four conditions of a proper process model (goal, action, observability, model conditions).

**Key insight:** "Highly reliable software is not necessarily safe." The curse of software flexibility means AI systems can be expanded without physical constraints, creating requirements gaps. LLMs exemplify this -- their complexity and flexibility make safety requirements extremely difficult to impose.

---

## Key Policy Frameworks

- **Weber-Simon dual lens for organizational AI:** Use Weber's structural analysis (hierarchy, specialization, formalization) alongside Simon's behavioral analysis (bounded rationality, values, communication) to evaluate AI integration
- **Ecosystem governance model:** Multi-layered, multi-stakeholder approach treating AI governance as interconnected systems
- **Process-oriented governance:** Apply transparency, accountability, and fairness at each phase of the AI lifecycle (goal setting, development, deployment, assessment)
- **System safety framework (Leveson-Dobbe):** Seven lessons translated into concrete strategies for safe AI deployment, with emphasis on process models, mental model alignment, and just culture

---

## Practical Takeaways for University Governance

1. **Apply the Weber-Simon framework** directly to university AI adoption. Universities are quintessential bureaucracies. Ask: how does each AI system affect the scope of human tasks, managerial control, and organizational structure? How does it reshape bounded rationality, value alignment, and communication flows?

2. **Guard against dehumanization.** AI-driven student interactions (chatbot advising, automated grading, algorithmic course placement) risk dehumanizing the educational experience. Restrict AI to tasks that do not benefit from human judgment and relationship.

3. **Adopt a process model** for every high-stakes AI deployment. Define: (a) the goal and safety constraints, (b) what actions the system can take, (c) how operators can observe the system's state, and (d) whether operators have an adequate mental model of the system.

4. **Build a "just culture"** around AI incidents. When an AI system produces harmful outcomes (biased grading, wrongful academic integrity flags, discriminatory recommendations), focus on systemic understanding rather than blame. Create safe reporting channels.

5. **Map the university AI ecosystem.** Use the Wirtz-Langer-Weyerer framework to identify all AI systems in use, their governance challenges, the stakeholders involved, and the governance mechanisms in place. Many universities have no comprehensive inventory.

6. **Design for lifecycle governance.** Following Chen and Ahn, governance should not be a one-time procurement review. Establish ongoing goal-setting, development oversight, deployment monitoring, and impact assessment for each AI system.

7. **Align mental models** across all stakeholders. Ensure that AI system designers, administrators who deploy the systems, faculty and staff who operate them, and students who are affected by them all share adequate understanding of what the system does, its limitations, and its potential harms.
