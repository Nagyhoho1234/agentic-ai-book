# Chapter 13: Pitfalls

## Summary

This chapter consolidates the key limitations and risks of using ChatGPT and related LLMs in scientific research. It serves as a critical counterbalance to the positive demonstrations in earlier chapters.

## Key Pitfalls

### 1. Randomness of Responses
- Identical prompts in different chat sessions produce significantly different responses in content, quality, and detail.
- This is observed in both ChatGPT and new Bing, across all chat modes ("More Creative," "More Balanced," "More Precise").
- **Mitigation**: Ask the same question multiple times across sessions and analyze outputs collectively. Craft clear, unambiguous, well-defined prompts to improve consistency.
- Users must understand that LLMs, like humans, are sensitive to the wording of requests and lack the "fuzzy logic" of human brains for interpreting poorly worded prompts.

### 2. Hallucination
- The model generates false or inaccurate information, attributes facts to wrong or non-existent sources.
- Particularly prevalent in bibliographic information: incorrect journal names, author names, publication years, article numbers, and DOIs.
- Switching from "More Creative" to "More Precise" mode in new Bing does NOT meaningfully alleviate this issue.
- The polished, authoritative tone of AI responses makes hallucinated content difficult to spot without deliberate fact-checking.
- This creates a paradox: users want quick, accurate answers, but AI's polished language makes errors hard to detect.
- Hallucinated errors may serve as "fingerprints" for detecting AI-generated scientific content.

### 3. Failure to Analyze Supplementary Materials
- Both ChatGPT and new Bing consistently failed to include supplementary materials in their analyses of research papers.
- This occurred even when links to supplementary files were provided in the prompts.
- This is a significant limitation because many environmental science journals publish substantial data, methods, and results in supplementary files.
- Supplementary materials are typically freely available online, making this failure particularly puzzling.

## Key Findings (Bullet Points from the Book)

- Responses exhibit significant randomness -- multiple queries or refined prompts are needed for consistent quality.
- The model tends to "hallucinate" by providing false information or citing non-existent sources. Bibliographic citations are especially unreliable.
- Changing model settings (Creative vs. Precise) does not fix hallucination -- it is an intrinsic limitation.
- Users face risk when relying on unverified AI outputs, made worse by the model's authoritative and polished tone.
- Both ChatGPT and new Bing fail to analyze supplementary materials, despite their high relevance and public availability.

## Practical Takeaways

- NEVER trust AI-generated bibliographic information without manual verification.
- Run the same query multiple times and compare outputs.
- The more polished and authoritative the response sounds, the more carefully it should be fact-checked.
- Do not rely on any single AI response as definitive -- treat outputs as starting points for investigation.
- Be especially vigilant about numerical data, specific claims, dates, and reference citations.
- The inability to process supplementary materials means users must manually integrate this information into their analyses.

## Notable References

- OpenAI (2022) on ChatGPT limitations
- Jackson (2023) on OpenAI discontinuing its AI detection tool
- Pegoraro et al. (2023) "To ChatGPT, or not to ChatGPT: that is the question"
- Emsley (2023) "ChatGPT: these are not hallucinations -- they're fabrications and falsifications"
