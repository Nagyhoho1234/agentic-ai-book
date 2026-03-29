# Chapter 2: The Digital Twin Landscape

## Comprehensive Summary

This chapter establishes the conceptual framework for the entire report by defining the key elements of a digital twin ecosystem and surveying the state of the art across three application domains: aerospace/defense engineering, atmospheric/climate/sustainability sciences, and biomedical sciences.

### Definition and Core Elements

The committee proposes a formal definition: a digital twin is a set of virtual information constructs that mimics the structure, context, and behavior of a natural, engineered, or social system; is dynamically updated with data from its physical twin; has predictive capability; and informs decisions that realize value.

The digital twin ecosystem consists of:

- **Physical counterpart** -- sensors, observing systems, data acquisition and integration
- **Virtual representation** -- modeling and simulation, AI, first-principles/mechanistic/empirical models, visualization
- **Physical-to-virtual flow** -- sensor fusion, data assimilation, inverse problems
- **Virtual-to-physical flow** -- automated control and decision-making
- **Human-digital twin interaction** -- human-in-the-loop decision-making
- **Cross-cutting concerns** -- VVUQ, ethics, security

### Parameters, States, and Quantities of Interest

The computational models are characterized by **parameters** (geometry, constitutive properties, boundary conditions), **states** (solved-for quantities in dynamical systems), and **quantities of interest** (metrics relevant to predictions and decisions). The distinction between parameter and state can blur when multiple models are coupled across disciplines.

### Verification, Validation, and Uncertainty Quantification (VVUQ)

VVUQ is identified as essential for responsible development, implementation, monitoring, and sustainability of digital twins. The committee defines:
- **Verification**: determining whether code correctly solves the mathematical model's equations
- **Validation**: determining the degree to which a model is an accurate representation of the real world
- **Uncertainty quantification**: quantifying uncertainties associated with model calculations of physical quantities of interest

Key VVUQ challenges unique to digital twins include: the bidirectional feedback loop between virtual and physical; evolving physical counterparts; changing data sources; dynamic model updating; and the need for continual (not one-time) VVUQ.

### Ethics, Privacy, and Data Governance

Digital twins aggregate sensitive, potentially identifiable data. Key concerns include:
- Biomedical digital twins that contain a patient's entire health history can "never be completely de-identifiable"
- Algorithmic bias from missing data and historical/systemic biases
- Data repurposing and the need for transparency about how data are used
- Governance questions around ownership and responsibility for data accuracy

### Security

The tight integration between physical and digital systems creates novel cybersecurity risks:
- Malicious actors could inject attacks into the feedback loop
- Digital twins could be interrogated to glean intellectual property or discover vulnerabilities in the physical system
- Scaling digital twins requires balancing information sharing with security

### Domain-Specific State of the Art

**Aerospace and Defense**: The USAF Airframe Digital Twin program is a leading example, focused on structural integrity of military aircraft. Key needs include connecting simulations across length scales, probabilistic analysis, optimal sensor placement, and uncertainty quantification. DoD needs to move from "models to action."

**Atmospheric, Climate, and Sustainability Sciences**: The European Destination Earth (DestinE) initiative is a major effort. Key needs include increased observational abilities, computational capacity, federated resource management, uncertainty quantification using Bayesian frameworks, and methods for validating extreme events and long-term climate predictions. The atmosphere is inherently chaotic with limited predictability.

**Biomedical Sciences**: Digital twins are not yet in practical clinical use but extensive R&D is underway. The European Virtual Human Twin (EDITH) project aims for fully integrated multiscale, multiorgan whole-body digital twins. Key barriers include sparse and invasive medical data, data heterogeneity, and the critical need for trust and transparency in clinical settings.

### Advancing the State of the Art

The committee concludes that publicity around digital twins currently outweighs the evidence base of success. The chief scientist of The Alan Turing Institute stated that the "Digital Twin evidence base of success and added value is seriously lacking." Realizing the potential requires an integrated research agenda that advances each element holistically.

## Key Research Gaps Identified

- **Priority 1 gaps (highest priority)**:
  - Building trust through transparent VVUQ communication to stakeholders
  - Scalable algorithms for DoD (uncertainty quantification, fast inference, causality, surrogates, interoperability)
  - Digital twins for defense handling classified data with near-real-time processing
  - Large-scale atmospheric/climate digital twins requiring increased observational abilities and computational capacity
  - Harmonizing, aggregating, and assimilating heterogeneous biomedical data
- **Priority 2 gaps**:
  - Development of decision-enabling digital twins for emergency response
  - Privacy and ethical considerations in biomedical digital twins
  - Methods for validating long-horizon climate predictions and extreme events
  - Cross-disciplinary collaboration mechanisms for atmospheric/climate sciences

## Practical Takeaways for Scientists

- Always include VVUQ in your digital twin design from the beginning -- it is not optional or an add-on
- Use the DOE Predictive Science Academic Alliance Program (PSAAP) as a model for how to structure interdisciplinary VVUQ-centered research
- The "fit for purpose" concept means your digital twin's fidelity should match the decision it supports -- not every application needs a high-fidelity replica
- Be honest about what is aspirational vs. demonstrated when describing digital twin capabilities
- For climate/Earth system applications: the existing data assimilation infrastructure is already a form of digital twin; build on it rather than starting from scratch

## Notable References

- Girolami, M. 2022. "Digital Twins: Essential, Mathematical, Statistical and Computing Research Foundations" (Alan Turing Institute perspective on evidence gaps)
- Bennett, H., M. Birkin, J. Ding, A. Duncan, and Z. Engin. 2023. "Towards Ecosystems of Connected Digital Twins to Address Global Challenges" (Alan Turing white paper)
- Niederer, S.A., M.S. Sacks, M. Girolami, and K. Willcox. 2021. "Scaling Digital Twins from the Artisanal to the Industrial" (scaling challenges)
- European Commission. 2023. "Destination Earth" (DestinE initiative)
- NRC. 2012. *Assessing the Reliability of Complex Models* (VVUQ foundations)
