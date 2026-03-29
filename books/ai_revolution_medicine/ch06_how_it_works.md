# Chapter 6: How It Works (and Doesn't)

**Author:** Peter Lee

## Summary

This is the book's most technical chapter, explaining how large language models like GPT-4 work and, crucially, why they fail. Lee provides an accessible but substantive overview of the Transformer architecture, training methodology, and the mechanisms that produce both GPT-4's impressive capabilities and its alarming failures.

Lee explains that GPT-4 is fundamentally a next-word prediction engine. Despite this seemingly simple objective, the scale of training (on vast internet text data) produces emergent capabilities that were not explicitly programmed, including medical reasoning. He describes the training process in three stages: pre-training on large text corpora, supervised fine-tuning with human-generated examples, and reinforcement learning from human feedback (RLHF).

The chapter devotes significant attention to hallucinations -- cases where GPT-4 generates plausible-sounding but factually incorrect information. Lee explains that hallucinations are not bugs that can be easily fixed but are inherent to the way language models generate text. The AI does not "know" things in the way humans do; it produces text that is statistically likely to follow the prompt. This means it can confidently generate fabricated medical studies, nonexistent drug names, or incorrect dosage information.

Lee also discusses the "temperature" parameter, which controls the randomness of GPT-4's outputs. Higher temperature settings produce more creative but less reliable responses. For medical applications, lower temperature settings are generally preferred, but even at low temperature, errors occur.

The chapter covers the concept of "grounding" -- connecting GPT-4 to external knowledge sources (databases, medical records, verified reference materials) to reduce hallucinations. Lee describes this as one of the most promising directions for making GPT-4 safer for medical use.

## Key Medical AI Applications

- **Understanding AI limitations:** Why GPT-4 hallucinates and what this means for medical applications
- **Grounding strategies:** Connecting LLMs to verified medical databases to improve accuracy
- **Temperature tuning:** Configuring AI parameters for safety-critical medical applications
- **Prompt engineering:** How the way questions are framed affects the quality and safety of medical AI output
- **Multi-modal capabilities:** Future potential for GPT-4 to process medical images, lab data, and genomic information

## Practical Takeaways for Scientists

- Understanding that GPT-4 is a statistical model (not a knowledge base) is essential for using it safely in any scientific context; it generates probable text, not verified facts
- Hallucinations cannot be eliminated through training alone; external verification and grounding are necessary for safety-critical applications
- The three-stage training pipeline (pre-training, supervised fine-tuning, RLHF) creates specific patterns of capability and failure that scientists should understand
- Temperature settings provide a simple but important lever for controlling the trade-off between creativity and reliability
- Prompt engineering is a skill that significantly affects output quality; small changes in how questions are phrased can produce dramatically different responses
- The Transformer architecture (attention mechanisms, self-attention) enables GPT-4 to maintain context across long conversations, which is crucial for complex medical discussions

## Notable References

- Vaswani, A. et al. "Attention Is All You Need" -- the original Transformer paper
- Bubeck, S. et al. (2023). *Sparks of Artificial General Intelligence: Experiments with an early version of GPT-4*
- Research on RLHF and its effects on model behavior
- Studies on hallucination rates in medical AI applications
