# Chapter 2: How LLMs Work

## Summary

This chapter provides a concise technical overview of how Large Language Models function, aimed at giving developers enough understanding to use them effectively without requiring a deep ML background. Wienholt covers the evolution from early AI (expert systems, OCR) through machine learning fundamentals (least squares regression, neural networks) to modern transformer-based architectures.

The chapter explains key concepts including neural network basics, the transformer architecture, GPT models, and the training process. It addresses the critical distinction between training data (static, historical) and the model's outputs (probabilistic, potentially hallucinated). The author compares major LLM providers -- OpenAI (GPT-4o, o3-mini), Anthropic (Claude 3.7 Sonnet), and Google (Gemini) -- and discusses benchmarks like MMLU for evaluating model capabilities.

A particularly valuable section covers LLM hallucination, explaining why models can generate plausible-sounding but incorrect outputs, and the practical implications for code generation. The chapter also discusses paraphrasing concerns -- that LLMs may reproduce training data closely enough to raise intellectual property issues.

## Key AI Coding Techniques

- **Understanding probabilistic output**: LLM code suggestions are probabilistic, not deterministic -- the same prompt can yield different results
- **Model selection matters**: Different models (GPT-4o, Claude 3.7 Sonnet, o3-mini) have different strengths; Copilot allows switching between them
- **Hallucination awareness**: Models can confidently generate code that references non-existent APIs or libraries
- **Temperature and creativity**: Higher temperature settings produce more varied but potentially less accurate outputs
- **Context window**: The amount of code/context the model can "see" affects output quality

## Practical Takeaways for Scientists

- LLMs are sophisticated pattern-matching systems trained on vast code repositories -- they do not "understand" code the way humans do
- Always verify AI-generated code, especially for domain-specific scientific computations where training data may be sparse
- The "computer decision" concept: LLMs make the same kind of statistical decision as a least-squares regression, just at vastly greater scale
- Benchmarks like MMLU can help compare models, but real-world performance on your specific tasks is what matters
- Be aware that LLM outputs may closely paraphrase existing code, with potential IP implications

## Notable References

- Neural network fundamentals and the transformer architecture
- OpenAI GPT models, Anthropic Claude models, Google Gemini models
- MMLU (Multitask Language Understanding) benchmark
- Hallucination as a fundamental LLM limitation
- North Vietnamese Army example of AI hallucination (fabricating historical "facts")
