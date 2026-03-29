# Chapter 7: Advanced Language Editing

## Summary

This chapter evaluates ChatGPT's capabilities as a language editor for scientific manuscripts -- one of the most beneficial uses found throughout the study. The authors tested the model on correcting rough English translations, rewriting entire texts, translating between languages, and compared GPT-3.5 vs GPT-4 performance on these tasks.

## Subsections

### 7.1 Correcting Issues in Writing
The authors provided ChatGPT with a rough English translation of a Chinese paragraph about cold chain logistics and coronavirus transmission. The model:
- Listed over a dozen corrections with detailed explanations
- Identified grammatical errors, odd phrases, and awkward sentences
- Suggested corrections and explained the reasoning behind each one
- The revised draft was much improved in clarity and coherence

**Key insight**: ChatGPT not only corrects but *explains* corrections, making it a teaching tool for improving writing skills. This is unlike grammar checkers (e.g., Grammarly, Word) or paraphrasing tools that simply change text without explanation.

**Recommended prompt**: "Read the text below. Identify any mistakes, inconsistencies, grammatical errors, odd phrases, awkward sentences, and other issues in the text. Suggest corrections and explain each correction in detail."

### 7.2 Rewriting Entire Text
Rather than correcting individual issues, the model can rewrite entire paragraphs. The rewritten version was more polished, contained no mistakes (verified against the original Chinese), and reads like native English. However, the authors recommend using the "correct and explain" approach over "rewrite" because authors learn more from understanding their mistakes.

### 7.3 Removing Language Barriers
ChatGPT was tested translating a Chinese government white paper on climate change policy into English (Table 22). Results:
- The translation was grammatically correct and coherent.
- One inaccuracy: "increased non-fossil fuel energy capacity" should have been "adding a new target, that is, the total installed capacity of non-fossil fuels" -- a case where ambiguous Chinese text led to misinterpretation.
- GPT-4 outperformed mainstream translators (Google Translate, Microsoft Translator, DeepL, CNKI Academic Translator) in consistency with the original text and accuracy of specialized terminology.
- Users can write prompts in their native language -- the model produces similar quality responses regardless of prompt language.

### 7.4 GPT-3.5 versus GPT-4 Model
- For language editing tasks, GPT-3.5 sometimes generated better responses than GPT-4, with more precise and natural-sounding phrasing.
- This aligns with GPT-3.5 maintaining an edge on GRE writing tests.
- For more complex tasks (adapting writing styles, designing experiments), GPT-4 is clearly superior.
- **Recommendation**: Run both models and compare outputs for language editing tasks.

## Practical Takeaways

- ChatGPT provides "universal access to advanced-level language editing" -- comparable to professional human language editors.
- Especially valuable for non-native English speakers writing scientific papers.
- Use the "correct and explain" approach to learn from mistakes rather than just getting a rewrite.
- The model can help with transitions between sentences and overall text coherence.
- For translation tasks, GPT-4 outperforms mainstream translation tools for specialized scientific terminology.
- Run both GPT-3.5 and GPT-4 for language editing and compare results.

## Notable References

- Plaxco (2010) "The art of writing science" -- Protein Science
- Brown et al. (2020) "Language models are few-shot learners" -- foundational GPT paper
