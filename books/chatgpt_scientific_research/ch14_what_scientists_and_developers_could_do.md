# Chapter 14: What Scientists and Developers Could Do

## Summary

This chapter provides actionable recommendations for both scientific researchers and AI model developers. It is forward-looking, addressing how scientists can adapt to AI tools and what developers should improve. The authors reference OpenAI's May 2023 open letter predicting that AI will "exceed expert skill level in most domains" within ten years.

## Subsections

### 14.1 Scientists as Early Adopters of AI Large Language Models

Scientists are well-positioned as early adopters due to their inherent curiosity and need for processing vast information. The authors offer five specific recommendations:

**14.1.1 Writing Effective Prompts**
- Formulate clear questions/hypotheses before writing prompts.
- If the initial response is unsatisfactory, rephrase and try again.
- Specify the purpose of the request and describe the intended use context.
- Use role-assigning (e.g., "You are a peer reviewer...") to refine responses.
- Break complex requests into multiple prompts within one chat session rather than one massive prompt.
- Non-native English speakers can write prompts in their native language with similar quality results.

**14.1.2 Testing Different Models**
- Many pre-trained GPTs and plugins exist beyond ChatGPT and new Bing.
- OpenAI's plugin system (launched May 2023) and GPT Store (November 2023) offer customized models.
- Other AI tools like Perplexity Ask can complement ChatGPT for specific tasks.
- Researchers should explore and compare multiple models.

**14.1.3 Cautionary Note**
- Be aware of unintended consequences: data privacy risks, non-compliance with publisher policies, hallucination, and potential bias.
- On 25 March 2023, a bug in ChatGPT exposed about 1.2% of ChatGPT Plus users' chat titles to other users.
- ChatPDF and similar tools may collect user data and query information.
- Until regulatory authorities establish clear rules, users should be cautious about privacy and intellectual property.

**14.1.4 Proactive Engagement**
- Follow model updates proactively -- improvements have been rapid over the past 18 months.
- Share experiences and feedback with developers through online forums and social media.
- Scientists can help reduce model bias, customize models for specific tasks, and improve prompt strategies.

**14.1.5 Writing with AI in Mind**
- Write metadata (title, abstract, section titles, figure captions, references) in a clear, meticulous, and informative manner since LLMs can scrape this information.
- Write "stand-alone" figure captions that include main results, interpretations, key methods, and "take-home messages."
- Make metadata available for text-scraping tools when publisher options exist.
- This can increase the visibility and impact of publications as AI analysis becomes more prevalent.

### 14.2 Functionalities in Need

Recommendations for developers:
1. **File upload in free version**: Allow document upload (PDF, TXT, RTF, Word, LaTeX, images, CSV, Excel) in the free ChatGPT interface.
2. **Accurate bibliographic information**: Train models on correct metadata (titles, authors, journal names, DOIs, page numbers) to reduce hallucination in references.
3. **Supplementary material integration**: Make analysis of supplementary files the default behavior when processing research papers.
4. **Source weighting**: Prioritize information from (i) references cited in the paper being analyzed, (ii) papers by the same first/corresponding author, and (iii) high-citation papers on similar topics.

### 14.3 Scientific Data for Training Models
- Models need real, peer-reviewed, validated scientific data -- not synthetic data.
- The reproducibility crisis undermines training data quality.
- Most scientific publications are behind paywalls, limiting training data.
- Publishers could collaborate with AI developers to create specialized, subscription-based scientific AI models.

### 14.4 Prompt Example Sets
- Developers should provide standardized, effective prompt templates tailored to scientific researchers.
- Prompt engineering is not easy for scientists who are not programmers.
- Standardized prompts would reduce inconsistency in model responses.

## Key Figure

- **Figure 6**: Diagram showing ChatGPT's current capabilities organized in a research workflow cycle: Brainstorming and Problem Formulation -> Data Collection and Information Gathering -> Literature Analysis and Knowledge Integration -> Scientific Writing, Peer Review and Publication -> Science Communication and Public Engagement (and back to Brainstorming).

## Practical Takeaways

- Write clear, purpose-driven prompts and use role-assignment for better results.
- Break complex tasks into sequential prompts within one chat session.
- Test multiple models and compare outputs.
- Write your papers with AI readers in mind -- stand-alone captions, complete metadata.
- Be vigilant about data privacy when uploading unpublished work to AI tools.
- Engage proactively with AI developments and share feedback with developers.

## Notable References

- OpenAI (2023b) "Governance of superintelligence"
- OpenAI (2023e) on the ChatGPT data exposure incident
- Lichtenberger (2023) on ChatPDF reaching 300,000 chats
- Tregoning (2023) "AI writing tools could hand scientists the 'gift of time'" -- Nature
