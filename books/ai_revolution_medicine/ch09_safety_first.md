# Chapter 9: Safety First

**Author:** Isaac "Zak" Kohane, Carey Goldberg, and Peter Lee

## Summary

This chapter tackles the critical question of how to regulate and safeguard AI in medicine. All three authors collaborate on this chapter, reflecting the complexity and importance of the topic. They acknowledge that regulation historically lags behind technology -- the Internet was only regulated in the 1990s, seat belt laws came decades after cars, and HIPAA did not anticipate social media -- and that we are at the very beginning of this lag period for medical AI.

The chapter uses a creative device: asking GPT-4 to respond to regulatory questions from the perspective of two fictional characters -- Barry (a doctor who is also a healthcare system lobbyist) and Darlene (a patient advocacy group founder who is also a civil rights lawyer). This approach surfaces the tension between innovation and patient protection.

**Key regulatory questions explored:**

1. **How should AI in healthcare be regulated?** Barry advocates for regulation that supports innovation while maintaining safety. Darlene emphasizes equity, bias prevention, and patient consent for data use.

2. **Do industry interests clash with patient interests?** Barry argues they can align if companies are transparent. Darlene insists on regulation that protects patient rights and promotes equity, with accountability for AI systems being fair, accountable, and transparent.

3. **Individual vs. societal outcomes:** Should medical AI maximize outcomes for individual patients or society? Barry advocates for both. Darlene argues AI must be designed with equity in mind, improving outcomes across all populations.

4. **Cost considerations:** Should AI factor in cost when making medical suggestions? Barry sees value in cost-effective recommendations. Darlene argues AI should always suggest the best option regardless of ability to pay, to avoid exacerbating healthcare disparities.

5. **Transparency vs. intellectual property:** Should regulators be able to inspect LLM inner workings? Barry sees a balance needed. Darlene argues for full regulatory access because patient safety demands it.

6. **Data currency:** Should regulation ensure AI is trained on accurate, up-to-date data? Both agree this is essential, noting that context-dependent medical decisions (e.g., malaria vs. non-malaria zones) require contextually appropriate AI.

7. **Bias monitoring:** Should there be ongoing monitoring for bias? Both agree, with Darlene emphasizing it as "absolutely crucial."

**The chapter examines existing regulatory frameworks:**

- The **FDA** has approved hundreds of narrow AI-augmented tools and developed a SaMD (Software as a Medical Device) framework, but GPT-4's general-purpose nature makes this framework a poor fit.
- **John Halamka** (Mayo Clinic Platform president) divides AI uses into low-risk (writing insurance letters) and high-risk (affecting patient care directly). High-risk applications should have "mandated human review" with liability on the reviewing human.
- The **UK "Medregs" blog** distinguishes between general-purpose LLMs (unlikely to qualify as medical devices) and LLMs specifically adapted for medical use (likely regulated as medical devices).
- The **EU** requires companies to demonstrate training on representative patient populations and considers geographic, behavioral, and functional context.
- **NIST** published a voluntary AI risk framework accepted by major companies (Amazon, etc.), calling for AI to be valid, reliable, safe, transparent, and privacy-enhanced.
- The **Coalition for Health AI** proposed a blueprint for trustworthy medical AI covering fairness, transparency, and reliability.

**Peter Lee's three regulatory arguments:**
1. The current FDA SaMD framework should NOT automatically apply to general-purpose LLMs like GPT-4, as this would immediately brake development
2. Human-like certification (medical licensing) does not work for LLMs because their failure modes differ fundamentally from human failure modes
3. The medical community must get up to speed quickly and drive the research and development of regulatory approaches

**Data Safety Monitoring Boards** are proposed as a model for AI oversight -- continuous monitoring panels with power to halt deployment if safety concerns emerge. Jim Weinstein (Microsoft) suggests AI should incorporate individual patient values in decision-making through prompts.

## Key Medical AI Applications

- **Regulatory framework design:** How to evaluate and certify AI systems for medical use
- **Bias detection and monitoring:** Systematic checking of AI output across demographic subgroups
- **Trustworthiness assurance:** Frameworks for ensuring fairness, transparency, accountability
- **Context-sensitive deployment:** AI that adapts recommendations to geographic and demographic context
- **Patient consent for AI use:** Mechanisms for patients to understand and agree to AI involvement in their care

## Practical Takeaways for Scientists

- Existing regulatory frameworks (FDA SaMD) are inadequate for general-purpose LLMs; scientists involved in medical AI should actively engage in developing new frameworks
- The distinction between general-purpose LLMs and medically-adapted LLMs is regulatory significant -- general tools may escape device regulation while adapted versions will likely be regulated
- Bias monitoring must be continuous, not one-time, because models are updated and contexts change
- Data Safety Monitoring Boards from clinical trials provide a useful model for ongoing AI safety surveillance
- The tension between innovation and regulation is real but not irreconcilable; risk-stratified approaches (low-risk vs. high-risk uses) offer a pragmatic path forward
- Scientists should consider both individual patient outcomes and population-level equity when evaluating medical AI systems
- Transparency about training data, model limitations, and potential conflicts of interest should be standard practice for any medical AI deployment

## Notable References

- Coalition for Health AI blueprint for trustworthy AI: coalitionforhealthai.org
- UK Medregs blog post on LLMs and medical devices (March 2023)
- Lieu, T. (2023). *AI Needs To Be Regulated Now*. NYT Opinion.
- Lawrence, L. (2023). *The FDA plans to regulate far more AI tools as devices*. STAT.
- Volpicelli, G. (2023). *ChatGPT broke the EU plan to regulate AI*. POLITICO.
- NIST AI Risk Management Framework
- EU AI Act requirements for representative training data
