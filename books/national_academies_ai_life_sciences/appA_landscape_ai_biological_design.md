# Appendix A: Mapping the Landscape of AI-Enabled Biological Design

## Overview

This appendix is a commissioned review paper authored by **Brian L. Hie** (Stanford University, Department of Chemical Engineering; Stanford Data Science; Arc Institute, Palo Alto). It provides a systematic overview of AI-enabled biological models, focusing on their applications in designing biological molecules and systems. The review covers foundation models, generative models, predictive models, and design models, with emphasis on protein engineering, genomic and transcriptomic modeling, and the biological datasets that underpin these tools.

## Comprehensive Summary

### Taxonomy of AI Biological Models

The review organizes AI-enabled biological tools into three categories:

1. **Foundation Models:** Large-scale unsupervised models that learn to reconstruct underlying data distributions. When trained on sufficiently large and complex datasets, they demonstrate generalist capabilities across a broad set of downstream tasks. Performance improves as both model and data scale increase (the "scaling hypothesis").

2. **Predictive Models:** Typically supervised models that map one biological modality to another (e.g., sequence to structure). Designed for specific tasks such as protein structure prediction, fitness prediction, or epigenomic profiling.

3. **Design Models:** Combine both generative and predictive models. The generative model proposes candidate sequences, and a predictive model evaluates them via "rejection sampling." Only sequences predicted to have the desired function are selected for experimental testing.

### Key Architectures

- **Multilayer Perceptron (MLP):** Fully connected layers of artificial neurons
- **Convolutional Neural Networks (CNNs):** Process information organized by position, focusing on local interactions
- **Graph Convolutional Neural Networks (GNNs):** Operate on graph-structured data, useful for molecular representations
- **Transformer Architecture:** Based on self-attention, enabling capture of both local and long-range dependencies; dominant architecture but scales quadratically with sequence length
- **State Space Models (SSMs):** Emerging class maintaining near-linear computational scaling with sequence length
- **Hybrid Architectures:** Combine different layer types (CNN, transformer, SSM) within a single network

### Training Objectives
- **Autoregressive language modeling:** Predict next token in sequence (left-to-right)
- **Masked language modeling:** Predict masked/corrupted tokens in input
- **Discrete diffusion modeling:** Progressively remove artificially corrupted tokens
- **Continuous diffusion modeling:** Iteratively remove artificial noise from continuous data
- **Mean squared error (MSE):** Minimize difference between prediction and ground truth
- **Variational autoencoders (VAEs):** Encode inputs to latent space and decode back
- Generative models are those trained with sampling-friendly objectives

## Foundation Models of Biological Data

### General Protein Sequence Models
Major model families catalogued in Table A-1:
- **ESM family:** ESM-1b, ESM-1v, ESM-2 (masked language modeling, transformer), ESM3 (multimodal, discrete diffusion)
- **ProGen family:** ProGen, ProGen2 (autoregressive, transformer)
- Other notable models: CARP, ProteinBERT, TAPE, ProtTrans, ProtGPT2, RITA

### Antibody Protein Sequence Models
Specialized models: AbLang, IgBERT, IgT5, AntiBERTa, AntiBERTy, Sapiens. Trained on heavy chain variable region (VH) and light chain variable region (VL) sequences from the Observed Antibody Space (OAS, ~2.4 billion sequences). Interestingly, specializing on antibody-specific datasets often degrades performance on tasks like mutational effect prediction compared to general protein language models.

### RNA Sequence Models
- **Coding RNA:** CaLM, CodonBERT -- capture codon biases with functional effects on translation rate or fidelity
- **Noncoding RNA:** RiNALMo, RNA-FM, Uni-RNA, RNAErnie -- smaller than protein models (largest: RiNALMo at 650M parameters)

### Genomic DNA Sequence Models
Range from combining nucleotides into larger tokens (GenSLM, Nucleotide Transformer) to maintaining single nucleotide resolution (GPN, regLM). Recent architectures like Hyena/Mamba offer longer context windows. **Evo** (hybrid SSM + Transformer, trained on billions of base pairs) is notable for capacity across both predictive and generative tasks at multiple biological complexity levels.

### Molecular Structure Models
- **RFdiffusion:** Hybrid GNN + Transformer, continuous diffusion -- protein backbone generation
- **Chroma:** GNN, continuous diffusion
- **Protpardelle:** Transformer, continuous diffusion -- generates all atoms in a protein structure

### Cellular Transcriptome Models
- **Geneformer, scBERT, scFoundation, scGPT** -- learn patterns in single-cell RNA sequencing data
- Challenge: limited pretraining data compared to protein or genomic domains (50-100M publicly available transcriptomes representing ~several thousand underlying cell types)

### Multimodal Foundation Models
- **Evo:** Uses a single fundamental data type (DNA) to capture information across RNA and protein modalities
- **ESM3:** Explicitly combines data from disparate modalities (protein sequence, structure, function) with a masked reconstruction objective
- Motivation: incorporate biological priors that encode physics and expert knowledge, potentially democratizing access to powerful models by reducing parameter requirements
- Challenges: accounting for disparate processes, timescales, granularities, and varying fidelities of different biological data types

## Predictive Models (Table A-2)

### Molecular Structure Prediction
- **AlphaFold / AlphaFold2 / AlphaFold3:** Progressing from single proteins to multimodal biomolecular structures including small molecules, nucleic acids, and lipids
- **ESMFold, OmegaFold:** Single-sequence structure prediction using protein language model embeddings (faster but less accurate than AlphaFold)
- **RoseTTAFold All-Atom:** Biomolecular structures alongside nucleic acids, metal ions, small molecules, and post-translational modifications

### Image to Structure
- **CryoDRGN, cryoSPARC, tomoDRGN, CryoDRGN-ET:** Reconstruct 3D protein volumes from cryo-EM and cryo-ET images; valuable for capturing conformational heterogeneity and protein dynamics

### Protein Fitness Prediction
- Supervised models use sequence-to-fitness mappings with one-hot encoding or neural sequence embeddings
- Unsupervised models (protein language models) have demonstrated remarkable success in zero-shot prediction of mutational effects -- lower sequence likelihoods generally indicate more deleterious effects
- Benchmark suites: ProteinGym and FLIP for comprehensive evaluation

### Viral Protein Fitness Prediction
- **Constrained Semantic Change Search (CSCS):** Viral protein sequence to escape score
- **EVEscape:** Escape score prediction
- **Early-Warning System:** Escape scoring
- **CoVFit:** Epidemiological fitness prediction
- These models offer promising tools for studying near-term infectivity/escape, but long-term viral evolution prediction remains limited

### Multi-Omic Prediction
- **Enformer:** Predicts multiple epigenomic tracks from raw DNA sequence, capturing regulatory interactions across long genomic distances
- **Borzoi:** Predicts gene expression tracks reflecting activity across different cell types

## Design Models

### Generative Models + Predictive Models = Biological Design
The standard workflow:
1. Generative model proposes candidate sequences
2. Predictive model evaluates candidates via rejection sampling
3. Only "good" candidates proceed to experimental validation
4. New experimental data improves models (iterative cycle)

Alternative approaches: supervised fine-tuning (SFT), reinforcement learning, direct preference optimization (DPO).

### Function-Guided Adaptive Protein Design
- Bayesian optimization using Gaussian process surrogate models to navigate sequence space
- Iterates between computational predictions and experimental validation
- Example: Madani et al. (2023) generated lysozymes with active catalytic activity at just 40% sequence identity to natural lysozymes
- Hayes et al. (2024) designed GFP homolog with <60% identity to natural GFPs
- Recent trend: combining Bayesian optimization with automated experimental platforms (Rapp, Bremer, and Romero, 2024)

### Structure-Guided De Novo Protein Design
Modern two-step workflow:
1. Structure generation models (e.g., RFdiffusion) create protein backbones with constraints (binding interfaces, symmetry)
2. Inverse folding methods (e.g., ProteinMPNN, ESM-IF1) determine amino acid sequences likely to fold into generated structures
3. Designs evaluated by "self-consistency" metric using AlphaFold or ESMFold

Achievements: creation of de novo proteins with complex functions including enzymes, protein binders, and designed proteins forming large assemblies or spanning cell membranes.

### Other Design Tasks
- **Genomic language model Evo:** Enables design of multimodal biological systems including CRISPR-Cas systems (protein-RNA co-design) and transposon systems (protein-DNA co-design)
- **Promoter design:** Machine learning-guided design for controlling gene expression, paralleling protein design approaches

## Biological Datasets (Tables A-3 and A-4)

### Comprehensive Database Catalog
The appendix catalogues major biological databases by category:

**Genome Sequence:** GenBank, ENA, RefSeq, Ensembl, GTDB, UHGG, JGI IMG, MGnify, Tara Oceans Project, and others

**Protein Sequence:** UniProt, UniRef50/UniRef90, Pfam, Observed Antibody Space (OAS)

**Viral Sequence:** GISAID, BV-BRC, Influenza Research Database, LANL HIV database

**Noncoding RNA:** Rfam, RNAcentral

**Biomolecular Structure:** PDB, CATH, CASP, AlphaFoldDB, ESM Metagenomic Atlas

**Protein Function:** ProteinGym, FLIP, ClinVar, SKEMPI, PDBbind, BindingDB, BRENDA, Binding MOAD, 2P2Idb, ProThermDB, STITCH, DrugBank, Gene Ontology

**Epigenomic Datasets:** ENCODE, Roadmap Epigenomics, PsychENCODE, 4D Nucleome, FANTOM

**Transcriptomic Datasets:** Human Cell Atlas, Tabula Sapiens, Tabula Muris, Fly Cell Atlas, CELLxGENE, Broad Single Cell Portal

### Example Training Datasets (Table A-4)
| Model | Training Data |
|-------|--------------|
| ESM-2 | UniRef90 |
| Evo | GTDB, IMG/PR, IMG/VR |
| AlphaFold2 | PDB |
| ProGen2 | UniRef90, metagenomic sequences, OAS |
| AbLang | OAS |
| CaLM | Coding sequences from ENA |
| Enformer | ENCODE datasets |
| scGPT | CELLxGENE |

## Key Findings

1. **Protein engineering is the most mature area** of AI-enabled biological design, with both structure prediction and de novo design achieving remarkable results
2. **Foundation models exhibit scaling behavior** similar to language models -- larger models trained on more data generally perform better
3. **Multimodal models** (Evo, ESM3) represent a promising frontier that can capture multiple levels of biological complexity
4. **Unsupervised models often outperform supervised models** at prediction tasks in zero-shot settings, suggesting that broad evolutionary information is a powerful prior
5. **Data availability is the primary bottleneck** for many biological modalities (especially single-cell transcriptomics, epigenomics, viral phenotype data)
6. **The gap between digital design and physical validation remains substantial** -- all computational designs require experimental testing

## Practical Takeaways for Scientists

- The landscape of AI biological tools is rapidly expanding -- the timeline of model development since 2021 (Figure A-2) shows accelerating pace
- For protein design: the RFdiffusion + ProteinMPNN + AlphaFold pipeline represents the current state-of-the-art workflow
- Unsupervised protein language models (ESM-2, etc.) are powerful tools for zero-shot fitness prediction without needing task-specific training data
- Consider multi-omic prediction tools (Enformer, Borzoi) for DNA regulatory element design
- When using viral fitness prediction models, be aware that near-term predictions are more reliable than long-term evolutionary forecasts
- Datasets highlighted in light blue in Table A-3 are those of sufficient diversity and quality to train foundation models
- The review identifies promising areas for future development: integration of physics-based priors with data-driven approaches, and synergy between computational simulation and experimental validation

## Notable References

- Bommasani, R., et al. 2021. "On the Opportunities and Risks of Foundation Models." *arXiv.*
- Jumper, J., et al. 2021. "Highly accurate protein structure prediction with AlphaFold." *Nature* 596(7873):583-589.
- Watson, J. L., et al. 2023. "De novo design of protein structure and function with RFdiffusion." *Nature* 620:1089-1100.
- Dauparas, J., et al. 2022. "Robust deep learning-based protein sequence design using ProteinMPNN." *Science* 378(6615):49-56.
- Hayes, T., et al. 2024. ESM3 multimodal protein model.
- Nguyen, E., Poli, M., Durrant, et al. 2024. Evo genomic language model.
- Madani, A., et al. 2023. ProGen generates functional lysozymes with low sequence identity.
- Kaplan, J., et al. 2020. "Scaling laws for neural language models." *arXiv.*
- Hoffmann, J., et al. 2022. "Training compute-optimal large language models." *arXiv.*
