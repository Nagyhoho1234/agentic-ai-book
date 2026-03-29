# Governance, Risk and Compliance (Pillar 5)

## Summary

This pillar addresses building and integrating risk management plans with the AI solution and improving business resilience, especially to AI-related cyber risks. While AI can deliver incredible benefits, the consequences of its errors can be equally significant. Every industry faces distinct risks based on target data collection points, regions, data safety, and legal compliance.

### Key risk areas:

- **Data sourcing** -- Vast data volumes come with data privacy, geopolitical, and cybersecurity risks. Data breaches can destroy reputation, lead to legal action, and cause huge revenue loss (average cost of a US data breach nearly doubled from $5.4M in 2013 to $9.4M in 2022)
- **Bias in algorithms** -- The AI model learns from its training dataset; bias in the dataset leads to undesirable outputs
- **Cyberattacks** -- Hackers can impact AI model integrity, take control of solutions, deliver manipulated inputs, or cause **poisoning of the AI algorithm**
- **Operational, financial, regulatory, and reputational hazards** -- AI used incorrectly or negligently can expose the organization to all of these

### AI Governance defined:

AI governance is the process of setting policies and establishing accountability to drive responsible development and deployment of AI systems. It encompasses risk management, regularity compliance, contractual agreements, and ethics. When done properly, AI governance fosters agility and trust.

### Assessment tools:

Capturing and managing metadata on AI models creates transparency into how AI systems are built and deployed. Many calibrated assessment tools are available in the market (developed with academia and governments) that help assess impact on risk and performance, encouraging transparency in model reporting.

## Key Procurement Guidelines (Table 8)

### 5.1 What is the target demographic for data collection?
- Is data being collected from vulnerable demographic groups?
- Is personal data collected in compliance with GDPR, HIPAA, regional laws?
- Does the supplier have informed consent of individuals whose data has been collected?
- Can individuals withdraw consent? Will collected data be withdrawn from the model?
- What are the relevant PII categories for the data collection process?
- Is content moderated (e.g., for sexuality/violence)?

### 5.2 How has the supplier accounted for managing cybersecurity risks?
- What proactive measures has the supplier taken to detect and tackle cyberattacks?
- How does the supplier minimize the effect of an attack?
- Does the supplier actively perform vulnerability management?

### 5.3 Has the supplier reviewed potential geopolitical risks?
- Has the supplier accounted for risks of collecting data from disputed territories?
- Have risks of storing or processing data in unstable regions been considered?
- Will AI pose any risk if used in such territories (e.g., heighten instability, affect peace)?
- Are data collectors at any physical risk during collection?

### 5.4 Have the risks related to the project been defined clearly?
- Is the scope clearly defined in terms of deliverables/outcomes?
- How does the supplier manage unsupported content types?
- How does the supplier define hard performance metrics with AI?
- To what extent is the AI solution reproducible?
- Will the AI model be covered by intellectual property policy? Who has legal ownership of source data, models, and resell rights?

### 5.5 Is the supplier compliant with rules and regulations?
- Has the supplier proactively prepared to ensure compliance?
- Does the supplier provide an explainability statement?
- Does the supplier comply with GDPR, CCPA, HIPAA, COPPA?
- Is the model compatible with emerging algorithmic compliance regulations (e.g., EU AI Act, NYC Law on Automated Employment Decision Tools)?

### 5.6 How does the supplier prepare for audits and compliance requirements?
- Does the supplier conduct mandatory conformity assessments? At what frequency?
- Has the supplier defined systems for internal audits? What artifacts can be shared?
- How does the supplier ensure compliance on both buyer and supplier sides after implementation?
- If access to legal support is limited (smaller buyer), how can the supplier assist?
- Has the AI model been assessed with algorithm assessment tools, model cards, etc.?

### 5.7 Is the supplier implementing international standards and certifications?
- Does the supplier follow AI governance standards from ISO, IEEE, and others?
- Will the AI system be accredited by a recognized institute providing conformity assessment?

### 5.8 What organizational practices does the supplier recommend?
- Is the risk-based approach developed by the supplier based on the specific AI model and industry?
- Has the supplier conducted an AI impact assessment of the buyer organization early in the process?

### 5.9 Do contractual agreements include all compliance-related factors?
- Can the supplier develop capacity for new contract requirements?
- Is there a supplier compliance statement (e.g., RAII certification) for master service agreements?
- Are there contractual agreements on restricted use or prohibited forms of use?
- Has the buyer developed KPIs and compliance metrics for the AI life cycle?
- Does the supplier offer support beyond contractual agreements for governance, maintenance, and change management?

## Practical Takeaways for University Leaders

- **FERPA, HIPAA, and state privacy laws** must be front and centre in any AI procurement by a university -- ensure the vendor demonstrates compliance with education-specific regulations, not just GDPR
- **Demand an explainability statement** from vendors, especially for AI tools used in student-affecting decisions (admissions, financial aid, academic advising)
- **Intellectual property ownership must be contractually clear** -- If a vendor trains a model on your institution's student data, who owns the resulting model? Can it be used for other clients?
- **Cybersecurity risk assessment is critical** -- AI systems processing student or research data are high-value targets. Require vendors to demonstrate proactive vulnerability management
- **Plan for audits from the start** -- Regulatory scrutiny of AI in education is increasing. Ensure the vendor can provide audit artifacts, conformity assessments, and compliance documentation
- **Monitor emerging regulations** -- The EU AI Act classifies some education AI as "high risk." The NYC automated employment decision tools law may have parallels for university hiring tools. Stay ahead of regulatory changes
- **Include compliance KPIs in contracts** that can be tracked throughout the AI system's life cycle

## Notable Frameworks

- **Table 8: Managing governance, risk and compliance -- questions to ask** -- The most extensive questionnaire in the report, covering 9 specification areas with dozens of detailed questions
- **EU AI Act** -- Referenced as an emerging horizontal framework for AI regulation using a risk-based approach
- **NYC Law on Automated Employment Decision Tools** (effective July 5, 2023) -- Requires bias audits by independent auditors for automated hiring systems
- **RAII (Responsible Artificial Intelligence Institute)** -- A non-profit offering certification programmes aligned with AI laws, regulations, principles, and research
- **AI explainability statement** -- A public document outlining how AI algorithms work, intended use, technology infrastructure, model accuracy, bias detection, risk management, ethical principles, and data sources
