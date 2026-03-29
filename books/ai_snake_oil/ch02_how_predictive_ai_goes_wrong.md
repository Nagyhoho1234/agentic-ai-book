# Chapter 2: How Predictive AI Goes Wrong

## Summary

This chapter is the core indictment of predictive AI -- the use of machine learning to forecast future events or classify people. The authors argue that many predictive AI applications are fundamentally flawed, not because of technical bugs that can be fixed, but because the underlying task is impossible or because the systems encode and amplify existing biases.

### The Spectrum of Predictive AI

The authors present a crucial spectrum: at one end are tasks where prediction genuinely works well (e.g., weather forecasting, product recommendations, spam detection), and at the other are tasks where prediction is essentially impossible (e.g., predicting which individual will commit a crime, which job applicant will perform best, or which student will succeed). The key factor is whether the patterns in historical data are stable, measurable, and genuinely predictive of the outcome of interest.

### Criminal Justice: COMPAS and Recidivism Prediction

The chapter examines COMPAS (Correctional Offender Management Profiling for Alternative Sanctions), a widely used algorithm for predicting recidivism. A 2016 ProPublica investigation found the tool was biased against Black defendants -- they were nearly twice as likely to be falsely flagged as future criminals compared to White defendants. The tool's maker, Northpointe, disputed the finding, but the authors explain that both sides were correct: there is a mathematical impossibility of satisfying multiple fairness criteria simultaneously when base rates differ between groups. This is not a fixable bug but a fundamental limitation.

### Hiring: HireVue and Automated Assessment

The chapter details HireVue, a company that claimed to assess job candidates through AI analysis of video interviews, scoring facial expressions, word choice, and tone of voice. The authors demonstrate this is essentially modern phrenology -- there is no scientific basis for predicting job performance from facial movements. Under pressure, HireVue quietly dropped facial analysis in 2021 but continued other dubious assessment methods.

### Healthcare: Algorithmic Denial of Care

Medicare Advantage plans use algorithms to predict how long patients need post-acute care, then deny coverage when the algorithm says the patient should have recovered. One insurer's algorithm denied coverage to a patient recovering from a broken leg after predicting 17.5 days of rehabilitation, even though the patient could not stand. An investigation found the algorithm had a 90% error rate for some conditions but was overriding doctor judgment.

### Insurance: Allstate's Pricing Algorithm

Allstate used an algorithm that identified customers unlikely to comparison-shop and charged them higher premiums -- the algorithm optimized not for risk (the stated purpose of insurance pricing) but for extracting maximum revenue from each customer.

### Key Insight: The Accuracy Trap

The authors make a critical point about accuracy metrics: a model that predicts "no crime" for everyone would be 99% accurate in most jurisdictions (since 99% of people do not commit crimes in any given year), but it would be completely useless. Similarly, predictive AI tools routinely report impressive-sounding accuracy numbers that are meaningless in context.

## Key Definitions

- **COMPAS:** Correctional Offender Management Profiling for Alternative Sanctions -- a recidivism prediction tool widely used in U.S. courts.
- **Fairness Impossibility Theorem:** The mathematical proof that certain fairness criteria cannot be simultaneously satisfied when base rates differ between groups.
- **Base Rate:** The underlying frequency of an outcome in a population. Many predictive AI failures stem from ignoring base rates.
- **False Positive Rate:** The proportion of negative cases incorrectly classified as positive. In criminal justice, this means innocent people flagged as future criminals.
- **Automation Bias:** The tendency for humans to defer to automated recommendations even when their own judgment would be better.

## Practical Takeaways for Scientists

- When evaluating any predictive AI tool, always ask: what is the base rate of the outcome being predicted? High accuracy can be meaningless if the base rate is very high or very low.
- The fairness impossibility theorem means that no amount of technical tinkering can make a prediction tool simultaneously fair by all reasonable definitions. This is a mathematical constraint, not an engineering problem.
- Be wary of AI tools that claim to predict complex human outcomes (health trajectories, student performance, research impact). The track record is poor.
- If adopting predictive AI for resource allocation in your institution, demand peer-reviewed validation on a population similar to yours, not just vendor benchmarks.
- Facial recognition and analysis tools have well-documented racial and gender biases. Use extreme caution if these appear in research workflows.

## Notable References

- Angwin, J. et al. "Machine Bias." ProPublica, 2016. (COMPAS investigation)
- Buolamwini, J. and Gebru, T. "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." *FAccT 2018.*
- Robinson, D.G. *Voices in the Code: A Story about People, Their Values, and the Algorithm They Made.* Russell Sage Foundation, 2022.
- Ross, C. and Herman, B. "Denied by AI: How Medicare Advantage Plans Use Algorithms to Cut Off Care for Seniors in Need." STAT, 2023.
