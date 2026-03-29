# Chapter 3: AI-Enabled Biological Design and the Risks of Synthetic Biology

## Comprehensive Summary

This chapter explores the complexities of biological design and engineering and subsequent biosecurity risk implications, focusing on current capabilities of AI-enabled biological tools combined with scientific understanding of biology. It examines three representative problems of increasing complexity and the 2018 NASEM framework for assessing biosecurity risks.

### AI-Enabled Design of Biomolecules

Current AI tools ARE capable of designing and redesigning molecules:
- **Protein design tools:** RoseTTAFold, AlphaFold, RFdiffusion can predict structures and design novel proteins
- **Redesigning toxins:** ProteinMPNN can assign amino acid building blocks to create a structurally similar molecule with limited sequence homology to the parent, potentially bypassing homology-based DNA screening
- **Limitations:** Fine-grained control, synthetic accessibility, permeation of physical barriers, interaction with specific cellular targets remain challenges
- **Intrinsically disordered proteins (IDPs):** Comprise 30-50% of proteomes and are refractive to traditional folding tools; AI-enabled prediction tools are beginning to address these
- Current AI-enabled design focuses on satisfying one or a few properties at a time, not the arbitrary number needed for a functional biological agent

### AI-Enabled Design of Self-Replicating Agents (Epidemic/Pandemic Potential)

This is far more challenging than molecule design. Key barriers:
- Generative AI models need to predict structural, virulence, AND transmissibility determinants accurately
- Currently available viral sequence data are unlikely to be sufficient for training such models
- Virulence and transmissibility are often associated with multiple molecular determinants and host interaction components
- RNA viruses operate near their mutational tolerance limit -- most changes are deleterious
- **Conclusion:** No available AI tool can currently design a virus de novo

### Modification of Existing Organisms

AI biological models can predict phenotypes from genotypic, proteomic, and molecular data, but with limitations:
- Several non-AI methods already predict pathogen characteristics (transmission rates, antibody escape)
- Unsupervised protein language models show promise in predicting viral infectivity and escape using deep mutational scanning data
- The ESM family of models can competitively model aspects of viral evolution in zero-shot or fine-tuned settings
- Long-term viral evolution prediction remains unreliable due to inherent uncertainty

### Understanding Data Limitations in Viral Design

- The lack of well-curated data is a critical limiting factor
- Protein folding models (e.g., AlphaFold) were trained on ~200,000 experimentally determined structures contributed over decades -- this data curation effort is what made the breakthrough possible
- COVID-19 drove collection of 15+ million SARS-CoV-2 sequences in GISAID, but phenotypic data has been collected for only a small fraction
- Virus genome sequences in databases are often incomplete, contain errors, or represent only consensus sequences
- There is no straightforward way to determine if an individual database sequence is fully functional
- AlphaFold3 authors acknowledge current protein design models are poor predictors of protein dynamics

### The "Butterfly Effect" in Viral Evolution

The chaotic nature of viral evolution challenges accurate prediction:
- Chaos theory and computational irreducibility concepts apply to evolutionary pathways
- The evolutionary trajectory of pathogens (and any newly created viruses) may remain unpredictable even with the best AI tools and supercomputers
- Physical production bottleneck is NOT affected by AI capabilities

### Implications for Biosecurity

Current state: AI-enabled biological tools can facilitate the design of simple biomolecules (toxins) but NOT complex self-replicating organisms. Significant capability uplifts to monitor:
1. Models able to predict transmissibility and pathogenesis with high accuracy
2. AI-enabled design of fully replicating infectious agents
3. Design models for molecules/pathogens that no longer require minimal wet-lab testing
4. Improved AI-driven automated laboratories

**Key conclusion:** *The relative lack of biological and mechanistic understanding about virulent phenotypes and the paucity of high-fidelity biological data mean that AI-enabled biological tools currently cannot be used to de novo design and subsequently build complex biological systems that can successfully replicate as transmissible biological agents with epidemic or pandemic potential.*

### The 2018 Framework for Assessing Biosecurity Risks

The NASEM 2018 framework from *Biodefense in the Age of Synthetic Biology* analyzes four main attributes:
1. **Usability of the technology:** Ease of use, rate of development, barriers to use, synergy with other technologies
2. **Usability as a weapon:** Production and delivery, scope of casualty, predictability of results
3. **Requirements of actors:** Access to expertise, access to resources, organizational footprint requirements
4. **Potential for mitigation:** Deterrence/prevention, recognition of attack, attribution, consequence management

### State-Sponsored Biological Weapons Programs

- Russia and North Korea have active offensive BW programs
- China and Iran raise compliance concerns with the Biological Weapons Convention (BWC)
- The barriers to de novo agent production are universal, even for nation states
- The U.S. maintains its biotechnological lead but must invest in scientific training and workforce development

### Future Impact of AI Agents

Box 3-4 describes how AI agents could streamline discovery-to-deployment:
- Bespoke AI agents could assist with ideation, reformulate ideas as tasks for design tools, push designs to wet labs
- Current paradigm still requires human experts to narrow hypotheses and formulate precise tasks
- Lone actors are less likely to possess resources for moving beyond ideation; organizations and nation states have more capability
- Computational resources and cost are major hurdles for lone actors

## Key Findings

1. AI can currently design simple biomolecules but NOT complex replicating organisms
2. The digital-physical divide (build and test) remains a critical bottleneck unaffected by AI capabilities
3. Data limitations are the primary constraint on developing more dangerous AI capabilities
4. The chaotic nature of viral evolution introduces fundamental unpredictability
5. The 2018 NASEM framework remains applicable for assessing AI-related biosecurity risks
6. State actors have more resources but face the same fundamental biological barriers

## Practical Takeaways for Scientists

- When using AI for protein or molecule design, remember that experimental validation remains essential -- AI provides guidance, not certainty
- Monitor the development of datasets linking viral sequences to virulence/transmissibility phenotypes as an early warning indicator
- The quality and completeness of sequences in viral databases (e.g., GISAID, GenBank) directly affects AI model capabilities -- contributing high-quality data is important
- Scientists working on gain-of-function or related research should be aware of how AI tools might amplify dual-use concerns
- The 2018 NASEM framework provides a useful lens for evaluating the risk profile of any new AI-enabled capability

## Notable References

- Urbina et al. 2022. "Dual use of artificial intelligence-powered drug discovery." *Nature Machine Intelligence* 4(3):189-191.
- Ekins et al. 2023. "Generative AI-assisted protein design must consider repurposing potential." *GEN Biotechnology* 2(4):296-300.
- Eisfeld et al. 2024. "A compendium of multi-omics data illuminating host responses to lethal human virus infections." *Scientific Data* 11(1):328.
- Abramson et al. 2024. "Accurate structure prediction of biomolecular interactions with AlphaFold 3." *Nature* 630(8016):493-500.
- NASEM. 2018. *Biodefense in the Age of Synthetic Biology.* https://doi.org/10.17226/24890.
