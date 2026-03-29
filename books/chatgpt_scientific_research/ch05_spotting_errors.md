# Chapter 5: Spotting Errors

## Summary

This chapter explores ChatGPT's ability to identify errors in scientific publications -- a significant issue given that reproducibility is recognized as one of the biggest challenges facing science today. The authors tested the AI on two types of errors: scientific/mathematical errors and misquotations.

## Key Concepts

- **Scientific errors in publications**: Errors are common in scientific literature, and journals like Nature, Science, and Environmental Science & Technology provide mechanisms for corrections.
- **Reproducibility crisis**: Baker (2016) reported that 1,500 scientists acknowledged difficulties in reproducing results, highlighting the systemic nature of errors in science.

## Subsections

### 5.1 Scientific Errors
The authors used a critical review paper from Water Research (Tran et al. 2017) that cataloged common errors in adsorption studies as their test reference.

**Example 1 -- Terminology/Chemistry errors** (Table 13): The model was asked to identify errors in a passage about PFOSA (perfluorooctanesulfonamide). New Bing correctly spotted two out of several errors:
- PFOSA has a sulfonamide group, not an "amino group"
- When pH > pKa, PFOSA exists as a negatively charged anion, not a neutral molecule

However, the model failed to identify other errors and provided unreliable references (Wikipedia, PubChem, Burns 2008) that contained no supporting data.

**Example 2 -- Mathematical equation errors** (Table 14): The model was asked to spot errors in adsorption kinetics equations from Zafar et al. (2007). The model provided correct equations for all four models but failed to spot an error in the linearized pseudo-second-order equation. Additionally, one of the model's own corrections (pseudo-first-order Lagergren equation) contained an error -- using a logarithm instead of a natural log.

### 5.2 Misquotation
The model was tested on identifying misquotations in a review paper (He et al. 2021a) -- subtle errors where quoted statements don't accurately reflect the findings of the cited study. The AI did a good job by refining statements with more accurate wording and highlighting corrections in bold font.

## Key Findings

- ChatGPT can identify some errors (misconceptions, incorrect terminology, equation errors, misquotations) but corrections are often incomplete.
- The model's corrections are mixed with its own errors -- requiring careful validation.
- Despite limitations, LLMs show promise as an augmented tool for error-spotting, though they cannot replace human expert review.
- Virtually all existing publications could be scrutinized for errors by AI, potentially reducing erroneous information in science.

## Practical Takeaways

- Use ChatGPT as a supplementary error-checking tool, not a replacement for expert review.
- Always validate the model's corrections -- it may introduce new errors while correcting old ones.
- The model is better at identifying conceptual errors than mathematical errors in equations.
- Misquotation detection is a strength -- the model can compare statements against referenced sources when it has access to the full text.
- Image manipulation, plagiarism, falsified data, and studies with poor QA/QC may be subject to AI scrutiny in the future.

## Notable References

- Tran et al. (2017) "Mistakes and inconsistencies regarding adsorption of contaminants from aqueous solutions: A critical review" -- Water Research
- Baker (2016) "1,500 scientists lift the lid on reproducibility" -- Nature
- Pulverer (2015) "When things go wrong: correcting the scientific record" -- EMBO Journal
