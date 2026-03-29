# Chapter 2: Design-Build-Test-Learn: Impact of AI on the Synthetic Biology Process

## Comprehensive Summary

This chapter examines the impact of AI on the Design-Build-Test-Learn (DBTL) cycle in synthetic biology, covering three key areas of development: scientific large language models (LLMs), automated laboratories, and synthetic datasets.

### The DBTL Cycle
In synthetic biology, the DBTL cycle is an iterative approach for designing, constructing, and evaluating biological systems with a built-in feedback loop:
- **Ideation/Design** (digital): AI tools provide data-driven insights, discover patterns in large datasets, generate novel ideas. In drug discovery, AI tools can generate thousands of candidate molecules in days -- a process that would take years for human researchers.
- **Build** (physical): The key point where digital outputs transition to physical implementation. This is where the digital-physical divide occurs.
- **Test** (physical): Designed agents are evaluated for expected behavior.
- **Learn** (digital/physical): Data from build and test phases refine and optimize designs for continuous improvement.

### Ideation and Design: Large Language Models and Foundation Models

**Scientific LLMs:**
- LLMs are approaching trillions of learnable parameters with significant advances in language understanding and generation
- "LLMs for science" are being developed for domain-specific knowledge acquisition and ideation
- Examples include: Med-PaLM 2 (medicine), CRISPR-GPT (gene-editing experiments), ChemCrow (chemical synthesis), BioGPT (biomedical research), MatSciBERT (materials science), AstronomyGPT, ClimateGPT
- LLMs can generate research ideas rated as more novel than those produced by 100 experts, though ideas lacked depth
- Current LLMs cannot reason well about planning problems; reasoning capabilities are improving (GPT-4o and beyond)

**Dual-use concerns:**
- Concerns exist about exploiting LLMs for harmful guidance (e.g., bioweapon creation)
- A study by Soice et al. (2023) found that student prompts to chatbots about pathogen creation were "highly guided and detailed" -- they already contained the information requested
- Rigorous analysis indicates current LLMs cannot reason well enough for complex protocol planning

**Foundation Models:**
- Models are not restricted to transformers -- include VAEs, GANs, diffusion models, and others
- Can be trained on multiple data modalities (e.g., DALL-E for text+images, Sora for text+video)
- Biological foundation models include:
  - IsoFormer (multimodal: DNA, RNA, proteins)
  - IBM Biomedical Foundation Models (diagnostic/therapeutic target discovery)
  - Medical imaging and pathology models
- Foundation models could become "one-stop shops" combining ideation and design, but current computational and data costs make this impractical

**Alternative architectures:**
- State space models (S4, S5, Mamba, Hawk) offer efficient recurrent networks with near-linear pretraining and constant-cost inference
- These could lower the computational barrier for biological foundation models

### Build and Test: Automated Laboratories

- Biofoundries automate design-build-test cycles and vary in capabilities
- Foundries are being leveraged to generate datasets for AI training ("lab in the loop")
- The concept of fully automated or "self-driving laboratories" is a future capability with significant challenges
- Currently, foundries are application-specific, resource-intensive, and require substantial human input
- The concern that fully automated foundries could be co-opted by malicious actors is real but currently unrealized

### Learn: Synthetic Data

- Training AI on synthetic data (artificial data mimicking real-world data) is increasingly appealing where real data is scarce
- Biological processes are physics-driven dynamic processes that no amount of wet-lab data will fully capture
- Synthetic data from Monte Carlo or molecular dynamics simulations may fill gaps in experimental data
- **Caution:** Model collapse (decreased performance from training on synthetic data from another ML model) is a documented phenomenon (Shumailov et al., 2024)

## Key Findings

1. AI's most significant impact on synthetic biology is in the digital phases (ideation and design), not the physical phases (build and test)
2. Scientific LLMs and foundation models are proliferating rapidly but remain limited in reasoning and planning capabilities
3. Automated laboratories could accelerate the DBTL cycle but are currently not capable of fully autonomous operation
4. Synthetic data shows promise but carries risks of model collapse
5. Future developments in LLMs, automated laboratories, and synthetic data represent areas to monitor for increases in AI-enabled biological capabilities

## Practical Takeaways for Scientists

- LLMs can serve as valuable ideation assistants for literature review, hypothesis generation, and experimental planning, but require expert oversight
- Foundation models trained on multiple biological modalities (DNA, RNA, protein, structure) represent a promising frontier
- Consider using biofoundries to generate datasets that can improve AI model performance
- Be cautious about training models on synthetic data -- validate against experimental results to avoid model collapse
- Alternative architectures (state space models, hybrid architectures) may lower computational costs for developing domain-specific biological models

## Notable References

- Birhane et al. 2023. "Science in the age of large language models." *Nature Reviews Physics* 5(5):277-280.
- Si, Yang, and Hashimoto. 2024. "Can LLMs generate novel research ideas?" arXiv:2409.04109.
- Soice et al. 2023. "Can large language models democratize access to dual-use biotechnology?" arXiv:2306.03809.
- Shumailov et al. 2024. "AI models collapse when trained on recursively generated data." *Nature* 631(8022):755-759.
- Hoffmann et al. 2022. "Training compute-optimal large language models." arXiv:2203.15556.
