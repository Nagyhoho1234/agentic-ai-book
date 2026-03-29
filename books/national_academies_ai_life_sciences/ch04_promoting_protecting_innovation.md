# Chapter 4: Promoting and Protecting AI-Enabled Innovation for Biosecurity

## Comprehensive Summary

This chapter highlights the beneficial applications of AI-enabled biological tools for enhancing biosecurity and mitigating biological threats through improved prediction, detection, prevention, and response. It is framed by Executive Order 14110 and the National Security Memorandum on AI, which articulate two guiding principles: (1) AI must be safe and secure, and (2) promoting responsible innovation and collaboration will allow the United States to lead in AI and solve society's most difficult challenges.

The chapter covers four major topics: AI-enabled infectious disease biosurveillance, AI-enabled biodesign for countermeasure development and emergency response, AI and biodesign security (nucleic acid synthesis screening), and balancing AI-enabled responses to biological threats and potential risks.

## AI-Enabled Infectious Disease Biosurveillance

AI-enabled biological tools have long contributed to multiple aspects of infectious disease surveillance:

- **Epidemiological tracking and forecasting:** Real-time monitoring of genomic data to detect emerging threats, amplified with predicted protein structure data
- **Early-warning systems:** Natural language processing to analyze global communication sources (e.g., HealthMap identified early SARS-CoV-2 cases as "cluster of pneumonia cases of unknown etiology")
- **Pathogen classification:** Deep learning models to rapidly identify known pathogens from genomic data
- **Hotspot detection:** Neural computing to correlate various data sources with disease spikes
- **Source identification:** Automated data mining of electronic medical records to uncover hidden transmission routes
- **Risk assessment:** Reinforcement learning and machine learning for targeted testing and risk prediction

**Key capability:** AI models can integrate genomic data with epidemiological information to predict outbreak patterns and inform public health responses in near real time. AI models can also guide treatment decisions and serve as early-warning systems for both potential biological agents and risks for outbreaks and epidemics.

## AI-Enabled Biodesign for Countermeasure Development and Emergency Response

The past decade has seen a significant shift in vaccine R&D from empirical development to "structure-based" vaccine design:

### Pre-AI Advances
- Stabilizing proline residues discovered by Jason McLellan and Barney Graham for MERS-CoV spike protein -- these were ported into SARS-CoV-2 vaccine candidates (Moderna, Pfizer/BioNTech)
- SKYCovione, the first computationally designed protein vaccine to complete Phase III trial, was approved for emergency use during COVID-19

### AI-Era Transformations
- **Protein structure prediction:** AlphaFold can now predict structures of millions of proteins. Structure of a new viral glycoprotein can be predicted accurately in hours (vs. weeks/months previously)
- **Vaccine design acceleration:** Instead of relying on known proline stabilization, generative AI can rapidly explore stabilizing strategies such as cavity filling, scaffolds, and particulate display
- **Monoclonal antibody development:** Future biodesign tools will enable in silico generation of monoclonal antibodies or other protein biologics that bind to predicted or actual viral structures, circumventing the need to isolate antibodies from convalescent patients
- **Global outbreak response:** Much of the work can be performed in silico, enabling response to be initiated anywhere in the world based on viral sequence alone

### Important Distinction
Going from an AI-designed sequence to a therapeutic antibody (a single protein) faces much less of a bottleneck than going from an AI-designed sequence to a potential pathogen (a complex system such as a virus).

## AI and Biodesign Security

### Nucleic Acid Synthesis Screening
Nucleic acid synthesis is a critical chokepoint between the digital and physical worlds:

- **International Gene Synthesis Consortium (IGSC):** Industry-led group formed in 2009 that sets voluntary standards for screening nucleic acid synthesis orders based on U.S. and international biosecurity standards
- **Executive Order 14110 directives:** The Framework for Nucleic Acid Synthesis Screening (April 2024) requires all federal agencies funding life sciences research to mandate screening
- **Six requirements for synthesis providers:** (1) implement screening, (2) screen for sequences of concern (SOCs), (3) screen customers, (4) report illegitimate orders, (5) retain records, (6) ensure cybersecurity

### Challenges to Screening
- AI-enabled tools can redesign toxins using different amino acid building blocks, potentially bypassing homology-based DNA screening
- SOC definition has been expanded to include sequences "known to contribute to pathogenicity or toxicity" even when not derived from regulated biological agents
- Future benchtop synthesis devices could bypass commercial screening entirely
- Screening for intent via "know your design" approaches may be impractical and produce false positives
- AlphaFold3 API initially blocked legitimate vaccine researchers (monkeypox vaccine design), illustrating unintended consequences of access restrictions

### Screening Approaches
- Screening can occur prior to training (excluding harmful data from training sets), but this may impact performance for beneficial applications like vaccine design
- Agent-based models can be instructed to avoid designing harmful sequences
- Template-based design models can be prohibited from using certain structures/sequences

**Key conclusion:** More research in new methodologies for nucleic acid synthesis screening, including how to leverage AI-enabled biological tools for screening, is needed.

## Balancing AI-Enabled Responses to Biological Threats and Potential Risks

### Institutional Landscape
Multiple U.S. government entities support infectious disease research and biosecurity:

- **HHS:** CDC (National Center for Emerging and Zoonotic Infectious Diseases), NIH (NIAID, Integrated Research Facility at Fort Detrick)
- **USDA:** Animal Health Inspection Services, National Institute of Food and Agriculture, National Bio and Agro-Defense Facility
- **DoD:** U.S. Army Medical Research Institute of Infectious Diseases (USAMRIID), Chemical and Biological Defense
- **DHS:** National Biodefense Analysis and Countermeasures Center
- **DOE:** Biological research programs at national laboratories, Joint Genome Institute
- **NSF:** Program on Ecology and Evolution of Infectious Diseases

### Key Funding Entities for AI-Enabled MCM Development
- **BARDA:** Committed to investing in technologies for MCMs "faster, safer, and more accessible"
- **ARPA-H:** CATALYST program developing predictive drug safety and efficacy models
- **DARPA:** AIxBio initiative pushing bioinnovation boundaries
- **DOE:** Frontiers in Artificial Intelligence for Science, Security and Technology initiative

### The Committee's "If-Then" Strategy
The committee recommends an "if-then" approach to account for the dynamic pace of AI development:

- Monitor data availability as a leading indicator of emerging AI capabilities
- Use principles-based framework for periodic reassessment
- Incorporate all four factors from the 2018 framework: usability of technology, usability as a weapon, requirements of actors, potential for mitigation
- Establish benchmarks and thresholds that trigger risk assessment and mitigation

**Example triggers:**
- If clear associations between viral sequences and virulence parameters become known, then evaluate AI models' capability to predict/design pathogenicity
- If robust viral phylogenomic sequence datasets linked to epidemiological data become available, then assess for new AI transmissibility models
- If AI models are developed that infer mechanisms of pathogenicity and transmissibility, then watch for attempts to modify existing pathogens
- If AI models could predictably generate a novel replication-competent virus, then assess risk for bioweapon development

## Key Findings and Recommendations

**Recommendation 1-1:** U.S. agencies (DoD, HHS/CDC, USDA, DOE, DHS) should continue to invest in vigorous research programs to understand the biology of infectious agents and implement biosurveillance networks through CDC and USDA in cooperation with public health agencies globally.

**Recommendation 1-2:** Entities within HHS (NIH, BARDA, ARPA-H) and DoD (DARPA, Chemical and Biological Defense) should fund approaches using AI-enabled design tools for medical countermeasure development, especially for epidemics, pandemics, or other biological threats.

**Recommendation 1-3:** As part of a national preparedness strategy, BARDA, DOE, and DoD should establish a public-private partnership, analogous to Operation Warp Speed and the COVID-19 High-Performance Computing Consortium, that can leverage and provide continuous access to AI-enabled tools and computational resources and be activated rapidly in an emergency response.

**Recommendation 2:** DoD and the U.S. AI Safety Institute should develop an "if-then" strategy to evaluate continuously both the availability and quality of data and emerging AI-enabled capabilities to anticipate changes in the risk landscape. Evaluation of AI-enabled biological tool capabilities may be conducted in a sandbox environment.

## Practical Takeaways for Scientists

- AI-enabled tools can dramatically accelerate vaccine and therapeutic antibody development -- structure prediction in hours rather than months
- Biosurveillance is a major beneficial application where AI can integrate genomic, epidemiological, and clinical data in near real time
- Scientists should engage with nucleic acid synthesis screening discussions, as restrictions designed for security may inadvertently impede legitimate research (as seen with AlphaFold3 API access)
- Public-private partnerships are essential for both MCM development and for maintaining commercial-sector innovation pipelines
- The distinction between capability and intent is critical when considering biosecurity risks -- avoid unnecessarily restricting beneficial R&D
- Physical production of biological agents remains the key bottleneck that cannot be overcome by AI alone

## Notable References

- Brownstein, J. S., B. Rader, C. M. Astley, and H. Tian. 2023. "Advances in artificial intelligence for infectious-disease surveillance." *NEJM* 388(17):1597-1607.
- Corbett, K. S., et al. 2020. "SARS-CoV-2 mRNA vaccine design enabled by prototype pathogen preparedness." *Nature* 586(7830):567-571.
- Wong, F., C. de la Fuente-Nunez, and J. J. Collins. 2023. "Leveraging artificial intelligence in the fight against infectious diseases." *Science* 381(6654):164-170.
- Wong, F., et al. 2024. "Discovery of a structural class of antibiotics with explainable deep learning." *Nature* 626(7997):177-185.
- NASEM. 2018. *Biodefense in the Age of Synthetic Biology.* https://doi.org/10.17226/24890.
- Fast Track Action Committee. 2024. *Framework for Nucleic Acid Synthesis Screening.* Office of Science and Technology Policy.
