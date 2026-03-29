# Chapter 7: Why Do Myths About AI Persist?

## Summary

This chapter investigates the ecosystem of hype that sustains AI snake oil. The authors identify four major sources of myths -- companies, researchers, journalists, and public figures -- and show how cognitive biases make the public especially susceptible. This is perhaps the most directly useful chapter for scientists, as it provides a systematic framework for evaluating AI claims.

### The AI Hype Cycle: Epic's Sepsis Model

The chapter opens with a detailed case study of Epic Systems' sepsis prediction model, which exemplifies the full AI hype cycle:

1. **Hype launch (2017):** Epic released an AI tool claiming to predict sepsis using electronic health records. The value proposition was compelling: detect sepsis early, save lives, no extra equipment needed.
2. **Uncritical adoption:** Hundreds of hospitals adopted the tool. No peer-reviewed evidence was available. Epic called the model a "proprietary trade secret."
3. **Independent evaluation (2021):** University of Michigan researchers found the model's relative accuracy was 63% -- barely better than a coin flip (50%), far below Epic's claimed 76-83%.
4. **Resistance to accountability:** Epic responded with anecdotal evidence rather than rigorous data. It turned out Epic was paying hospitals up to $1 million in credits for using the model, making adoption rates a poor measure of quality.
5. **Quiet retreat (2022):** Epic stopped selling its one-size-fits-all model, asking hospitals to train models on their own data -- a tacit admission that the plug-and-play approach failed.

Other Epic models included features like "religion" to predict no-shows, likely leading to discrimination.

### Companies Have Few Incentives for Transparency

- Models like COMPAS (recidivism), HireVue (hiring), and Epic (healthcare) are proprietary. Companies hide behind "trade secret" claims.
- Startups game accuracy metrics to attract investors: switching from top-3 to top-5 accuracy to hit the 90% threshold that impresses funders.
- VCs have aligned incentives to hype: "The VCs wanted to hype things up, get a lot of press, make a splash, so they could raise the next round at a higher valuation."
- Benchmark performance on academic datasets grossly overestimates real-world utility. GPT-4 passing the bar exam at the 90th percentile tells us nothing about whether it can do a lawyer's actual job.

### The AI Community Has a Culture of Hype

- AI research cycles between "springs" (hype periods) and "winters" (funding droughts). The current spring risks another winter if expectations are not met.
- Almost three-quarters of AI PhDs choose industry over academia, creating conflicts of interest.
- Academic research serves as limited check on industry power because the field accepts corporate funding uncritically.
- The field prioritizes engineering breakthroughs over scientific understanding of *why* AI works.
- Ali Rahimi's 2017 NeurIPS speech compared AI research to "alchemy" -- focus on beating benchmarks rather than building genuine understanding.
- Geoffrey Hinton's 2016 prediction that radiologists would be obsolete within five years was spectacularly wrong -- in 2022 there was a worldwide shortage of radiologists.

### The Reproducibility Crisis in AI Research

- A 2018 review of 400 leading AI papers found that **none** satisfied all criteria for reproducibility.
- Most papers satisfied only 20-30% of reproducibility requirements.
- The authors' own research found widespread "leakage" errors -- where models are evaluated on data they were trained on -- in fields including medicine, psychiatry, computer security, and genomics.
- When the authors corrected leakage in civil war prediction models that claimed "astounding accuracy," the models performed no better than decades-old methods.
- OpenAI's discontinuation of its Codex model with just three days' notice made hundreds of academic papers unreproducible overnight.

### News Media Misleads the Public

- AI articles routinely use robot imagery even when the AI application has nothing to do with robots, creating the false impression that AI equals robots.
- News stories uncritically repeat company PR statements and attribute agency to AI ("the algorithm decided" rather than "the engineers programmed").
- Press releases from universities are responsible for a major chunk of AI hype in scientific research.
- Mystical language ("the magic of AI," "the gods of artificial intelligence") misrepresents what are fundamentally statistical pattern-matching systems.

### Public Figures Spread AI Hype

The authors critique Kissinger, Schmidt, and Huttenlocher's book *The Age of AI* as exemplifying public-figure hype -- incessant hyperbole, failure to distinguish different types of AI, and portrayal of AI as "unknowable" when it is actually quite well understood technically.

### Cognitive Biases That Sustain Myths

- **Illusion of explanatory depth:** People believe they understand AI more deeply than they do.
- **Halo effect:** Impressive performance in one domain (chess) leads people to assume universal capability.
- **Priming:** Science fiction has primed the public to equate AI with sentient robots.
- **Illusory truth effect:** Repeated inaccurate claims come to feel true through sheer repetition.
- **Anchoring bias:** Initial overblown claims about AI capabilities anchor beliefs even after corrections.
- **Confirmation bias:** Once people believe AI is powerful, they selectively notice evidence supporting this belief.
- **Quantification bias:** Impressive-sounding accuracy numbers (90%!) are taken at face value without asking what they mean in context.
- **Anthropomorphism:** People attribute human qualities to AI systems, leading to misplaced trust.

## Key Definitions

- **Leakage:** When training data contaminates the test set, artificially inflating model performance. A cardinal error in machine learning.
- **Relative Accuracy:** The probability that a positive case is scored higher than a negative case. 50% is equivalent to random guessing.
- **Top-N Accuracy:** Counting a prediction as correct if the right answer is among the model's top N guesses. Higher N artificially inflates accuracy.
- **Reproducibility Crisis:** The widespread failure of scientific results to replicate when independently tested.
- **Regulatory Capture:** When a regulatory agency is co-opted to serve the interests of the industry it is supposed to regulate.
- **Criti-hype:** Criticism that inadvertently reinforces hype about a technology's power.

## Practical Takeaways for Scientists

- **Always demand peer-reviewed, independently validated evidence** before adopting any AI tool in consequential settings. Vendor benchmarks are insufficient.
- **Check for leakage** in any AI-based study: was the model evaluated on data it was trained on? This is the most common methodological error in AI-based science.
- **Be skeptical of accuracy claims.** Ask: what metric was used? What is the base rate? Was the evaluation on realistic data? Could a simple baseline achieve similar results?
- **The reproducibility checklist matters.** When publishing AI-based research, release code and data. When evaluating others' work, check whether you could reproduce it.
- **Watch for cognitive biases** in your own evaluation of AI tools. The halo effect (AI beat a chess champion, so it must be good at my task) is particularly seductive.
- **Question the framing.** When you see a headline about AI achieving 90% accuracy at something, ask what that actually means for your use case. 90% accuracy in a system with a 1% base rate means the vast majority of positive predictions are wrong.
- **Independence matters.** Treat AI claims from companies with the same skepticism you would apply to pharmaceutical company claims about their own drugs.

## Notable References

- Rahimi, A. "AI is the new alchemy." NeurIPS Test of Time Award speech, 2017.
- Lipton, Z.C. and Steinhardt, J. "Troubling Trends in Machine Learning Scholarship." *ICML*, 2018.
- Gundersen, O.E. and Kjensmo, S. Study of reproducibility in AI research, Norwegian University of Science and Technology, 2018.
- Kapoor, S. and Narayanan, A. "Leakage and the Reproducibility Crisis in Machine-Learning-Based Science." *Patterns*, 2023.
- Whittaker, M. and Suchman, L. "The Myth of Artificial Intelligence." Review of *The Age of AI*.
- Mitchell, M. Various writings on AI culture and hype.
