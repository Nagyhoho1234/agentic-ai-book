# Chapter 4: AI and Medical Competence

**Author:** Isaac "Zak" Kohane

## Summary

Kohane, a physician and biomedical informatics researcher, provides a rigorous assessment of GPT-4's medical competence. He approaches the AI as he would a medical trainee, systematically probing its knowledge, reasoning, and clinical judgment across multiple domains.

The chapter introduces two evaluation frameworks: the "Trial" and the "Trainee." The Trial framework treats AI evaluation like a clinical trial -- testing performance on specific, well-defined tasks with measurable outcomes. The Trainee framework evaluates the AI as one would a medical student or resident, assessing its ability to reason, handle ambiguity, and know the limits of its knowledge.

Kohane presents detailed case studies where GPT-4 handles complex diagnostic puzzles. The AI demonstrates impressive performance on cases involving rare diseases, multi-system presentations, and cases requiring integration of laboratory results, imaging findings, and clinical history. He is particularly struck by GPT-4's ability to consider diagnoses that even experienced specialists might overlook.

However, Kohane also identifies critical weaknesses. GPT-4 sometimes makes errors in medical reasoning that a competent physician would not make. More concerning, it occasionally fabricates clinical details or references that do not exist. Kohane emphasizes that these hallucinations are particularly dangerous in medicine because they are difficult to detect without independent verification.

The chapter discusses the regulatory implications. The current FDA framework for Software as a Medical Device (SaMD) was designed for narrow AI tools with specific, testable claims. GPT-4's broad, general-purpose nature does not fit neatly into this framework. Kohane argues that human-like certification (similar to medical licensing exams) is also insufficient because GPT-4's failure modes are fundamentally different from human failure modes.

## Key Medical AI Applications

- **Rare disease diagnosis:** GPT-4 identifying uncommon conditions from complex symptom presentations
- **Multi-system clinical reasoning:** Integrating findings across organ systems
- **Medical knowledge assessment:** Systematic testing comparable to board examinations
- **Diagnostic reasoning under uncertainty:** Handling ambiguous presentations where multiple diagnoses are possible
- **Clinical decision support:** Providing evidence-based recommendations for treatment

## Practical Takeaways for Scientists

- The distinction between Trial (task-based) and Trainee (competence-based) evaluation is useful for any scientist assessing AI capabilities in their domain
- Hallucinations in medical AI are not just an academic concern; they can directly endanger patients if plausible-sounding but false information influences clinical decisions
- Existing regulatory frameworks (FDA SaMD) are inadequate for general-purpose LLMs; new evaluation paradigms are needed
- Scientists should evaluate AI systems not just on what they get right, but on how they fail -- the pattern and predictability of errors matters as much as the error rate
- GPT-4's broad competence across medical specialties is unprecedented but also makes it harder to evaluate, since no single human expert spans all the domains the AI covers

## Notable References

- FDA framework for Software as a Medical Device (SaMD)
- International regulatory approaches to medical AI (Europe, China, Australia)
- Medical licensing examination structures and their applicability to AI evaluation
