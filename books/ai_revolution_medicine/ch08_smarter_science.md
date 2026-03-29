# Chapter 8: Smarter Science

**Author:** Isaac "Zak" Kohane

## Summary

Kohane opens with a deeply personal story: as a new doctor, his first patient -- a newborn -- died from persistent pulmonary hypertension. A study on ECMO (extra-corporeal membrane oxygenation) published shortly after would have saved the baby's life. This experience has haunted Kohane for decades and drives his conviction that accelerating medical research saves lives. He asks GPT-4 whether it could help overcome the countless delays that slow the research-to-treatment pipeline.

The chapter systematically explores GPT-4's potential across three pillars of biomedical research: clinical trials, scientific publishing, and basic research.

**Clinical Trial Design:** Using the GLP-1 pathway (the science behind weight-loss drugs semaglutide/Wegovy and tirzepatide/Mounjaro) as a running example, Kohane asks GPT-4 to design a randomized controlled trial comparing a hypothetical new drug ("shrinkatide") to tirzepatide. GPT-4 produces a reasonable trial design including recruitment, randomization, measurement protocols, and statistical analysis. It also generates inclusion/exclusion criteria and an adverse event monitoring table.

**Patient Recruitment:** GPT-4 is given SOAP notes and asked to determine whether patients meet trial criteria. It correctly calculates BMI from height and weight data (5'4", 170 lbs = BMI 29), identifies inclusion and exclusion criteria matches, and cross-references eligibility against specific clinicaltrials.gov study criteria. However, it also "forgets" its own earlier BMI calculation, illustrating the hallucination problem. Kohane estimates that automated eligibility screening could save $150-$1,000 per patient and cut months to years from trial timelines, given that a one-month delay costs pharmaceutical companies $600,000-$8 million.

**Informed Consent:** GPT-4 summarizes a 1,142-word consent form from an Eli Lilly tirzepatide study (SURMOUNT-2) into accessible bullet points, then answers patient questions about visits, injections, placebo assignment, and benefits. It can adjust reading level on request (demonstrated at 6th grade level).

**Code Generation:** GPT-4 generates Python/Flask code with SQLAlchemy for a web form to capture adverse events, producing functional backend and frontend code from a single prompt.

**Research Literature:** GPT-4 summarizes a high-impact NEJM article on tirzepatide vs. semaglutide, adjusts summaries for different literacy levels, and reports on racial/ethnic representation in trial populations. Kohane envisions services that allow investigators to query the entire biomedical literature with complex, multi-criteria searches.

**Scientific Writing:** GPT-4 converts a stream-of-consciousness narrative about Google Trends data on weight loss drugs into a properly formatted medical publication abstract with Objectives, Methods, Results, and Conclusions sections -- demonstrating how non-native English speakers could overcome language barriers to publication.

**Data Analysis:** In a striking example, Kohane presents a puzzle about white blood cell counts: white males aged 50-65 with low WBC measured between 12AM-8AM had 53% mortality at 3 years, while those measured between 8AM-4PM had only 3% mortality. GPT-4 correctly identifies the key insight (blood draws at 3AM indicate hospitalization/serious illness, not just low WBC) -- an answer that 90% of data scientists get wrong.

**Basic Research:** GPT-4 identifies protein targets for neurodegeneration (BACE1 for Alzheimer's, alpha-synuclein for Parkinson's, huntingtin for Huntington's) and lists specific BACE1 inhibitor compounds with selectivity data (MK-8931, GRL-8234, JNJ-269932, LY2886721). While this information is available in published literature, GPT-4's ability to synthesize it rapidly is valuable.

**Missing Data and Bias:** Kohane raises the critical issue that GPT-4's medical knowledge depends on its training data, which is biased toward certain populations, institutions, and geographic contexts. Clinical notes from a Boston hospital differ dramatically from those in a malaria-endemic region. He advocates for patient-directed data sharing through models like the UK Biobank (500,000+ consented participants) rather than hospital-mediated data deals.

**Vision -- "Dr. OWE":** Kohane envisions a future model ("Dr. One-With-Everything") that integrates protein structure prediction (like AlphaFold2), genetic variation databases, clinical trial data, and biomedical literature into a unified research tool. He predicts this could be the central intellectual tool for biomedical research by the mid-2030s.

## Key Medical AI Applications

- **Clinical trial design:** Automated generation of trial protocols, inclusion/exclusion criteria, and adverse event monitoring plans
- **Patient eligibility screening:** Automated matching of patient records against trial criteria, with potential to save months and millions of dollars
- **Informed consent simplification:** Translating complex consent documents into accessible, interactive Q&A format
- **Literature synthesis:** Rapid summarization and comparison of research papers across journals
- **Research publication support:** Formatting narratives into publication-ready abstracts, particularly aiding non-English-speaking researchers
- **Data interpretation:** Identifying confounding variables and causal relationships in clinical data
- **Basic research acceleration:** Synthesizing knowledge about protein targets, inhibitor compounds, and drug mechanisms
- **Code prototyping:** Generating functional data collection tools (web forms, databases) for rapid field testing

## Practical Takeaways for Scientists

- The cost of trial delays is quantifiable ($600K-$8M per month) and AI-assisted patient recruitment could materially reduce this
- GPT-4's ability to calculate BMI from raw measurements and cross-reference against criteria is useful but error-prone; always verify its arithmetic
- The "data context matters more than data value" insight (3AM blood draw vs. 3PM) illustrates GPT-4's ability to reason about confounders -- but it also includes less-important explanations alongside the correct one
- GPT-4's knowledge is bounded by its training data cutoff; it lacks real-time access to databases and recent publications
- The vision of integrating LLMs with specialized biological models (AlphaFold2, genomic databases) represents a realistic and potentially transformative research direction
- Patient-directed data sharing (like UK Biobank) may produce more representative training data than hospital-mediated deals
- Non-English-speaking researchers can use LLMs to overcome publication barriers, potentially democratizing scientific communication

## Notable References

- Frias, J. P. et al. (2021). Tirzepatide versus Semaglutide Once Weekly in Patients with Type 2 Diabetes. *NEJM*, 385(6), 503-515.
- AlphaFold2 by DeepMind for protein structure prediction
- UK Biobank (500,000+ participants with consented clinical and research data)
- i2b2 project (community.i2b2.org) for healthcare as a living laboratory
- ClinicalTrials.gov trial NCT02092545
