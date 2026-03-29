# Chapter 3: Virtual Representation -- Foundational Research Needs and Opportunities

## Comprehensive Summary

This chapter addresses the computational models that form the core of a digital twin's virtual representation. It covers fit-for-purpose modeling, multiscale modeling, hybrid modeling (combining mechanistic and ML approaches), integration of component/subsystem digital twins, and surrogate modeling.

### Fit-for-Purpose Virtual Representations

There is no one-size-fits-all approach. The virtual representation can take many mathematical forms: dynamical systems, differential equations, statistical models, and ML models. Model types, fidelity, resolution, parameterization, and quantities of interest must be chosen to fit the particular decision task and computational constraints.

The committee introduces a distinction between **data-centric** and **model-centric** digital twin views:
- **Data-centric**: appropriate when data is abundant and decisions fall within the realm of conditions represented by data. The data forms the core, with empirical/ML models wrapping around it. Example: aircraft engine fleet management.
- **Model-centric**: appropriate when data is sparse and predictions must extrapolate beyond available observations. Mathematical models form the core, with data assimilated through the lens of models. Example: climate projections, cancer patient digital twins.

### Multiscale Modeling

A fundamental challenge is the vast range of spatial and temporal scales. Examples:
- Earth's atmosphere: millimeters to tens of thousands of kilometers; seconds to centuries
- Biological systems: nanometers to meters; nanoseconds to years
- Engineering systems: multiphysics phenomena (chemical reactions, heat transfer, phase change, fluid-structure interactions)

Currently, the demarcation between resolved and unresolved scales is determined by **available computing resources, not by a priori scientific considerations**. There is a gap between scales that can be simulated and scales that are actionable for decision-making.

### Hybrid Modeling (Mechanistic + Machine Learning)

Hybrid approaches that combine data-driven and model-driven formulations were repeatedly emphasized across all workshops. They can leverage the strengths of both:
- ML can bridge unresolved scales, identify correlations, create surrogates
- Mechanistic models provide physical constraints, extrapolation capability, interpretability

Five major gaps in hybrid modeling:
1. Data quality, availability, and affordability
2. Model coupling and integration
3. Model validation and calibration (harmonizing data-driven and mechanistic validation processes)
4. Uncertainty quantification and interpretability (accounting for uncertainties from both components)
5. Model scalability and management

### Integrating Component and Subsystem Digital Twins

A digital twin of a system of systems will couple multiple constituent digital twins. This creates additional challenges:
- Models calibrated individually may behave differently when coupled due to error propagation and nonlinear feedback
- Interoperability of software and data across domains is a major challenge
- Semantic and syntactic interoperability must be addressed

Examples include Earth system models (coupling atmosphere, ocean, land, ice) and gas turbine engines (coupling compressors, combustors, turbines).

### Surrogate Modeling

Surrogate models are essential for computational tractability. Three types:
- **Statistical data-fit models**: fit approximate input-output maps (e.g., Gaussian process, deep neural networks)
- **Reduced-order models**: incorporate low-dimensional structure from governing equations
- **Simplified models**: coarser grids, simplified physics, loosened tolerances

Three key challenges for surrogates in digital twin contexts:
1. **Scale**: digital twins require modeling at the full system scale with high-dimensional parameter spaces
2. **VVUQ**: critical need for VVUQ of surrogate models, especially in extrapolatory regimes
3. **Dynamic updating and adaptation**: surrogates must be updated as the digital twin evolves

A significant but often unreported cost is **generating sufficient training data** for surrogates. Many papers fail to account for the computational expense of training data generation.

### Data Assimilation, Dynamic Updating, and Adaptation of Surrogate Models

Dynamic updating is central to the digital twin concept. Surrogates must be updated on the fly under computational and time constraints, while the surrogates themselves must also be validated. Research at the intersection of data assimilation and surrogate models is an important gap -- data assimilation with surrogates has been considered in some settings but not at the scale and complexity required for digital twins.

## Key Research Gaps Identified

**Priority 1 (highest):**
- Increasing available computing resources to close the gap between simulated and actionable scales
- Uncertainty quantification, explainability, and interpretability for hybrid models
- Uncertainty quantification for calibrating component models and quantifying uncertainty in coupled complex systems
- Interoperability when integrating component and subsystem digital twins

**Priority 2:**
- Model validation and calibration for hybrid models (harmonizing data-driven and mechanistic approaches)
- Balancing computational complexity of mechanistic and data-driven techniques at affordable cost
- Coupled multiphysics systems pose particular challenges to surrogate modeling
- Surrogate modeling with limited training data and methods for accounting for extrapolation
- Dynamic adaptation of surrogate models under computational constraints with continual VVUQ
- Consequences of prior distribution choices on Bayesian solutions for parameter estimation

## Practical Takeaways for Scientists

- Decide early whether your problem is data-centric or model-centric -- this fundamentally shapes the digital twin architecture
- When publishing surrogate model results, always report the full cost of training data generation (compute time, hardware, energy), not just the speedup factor
- For multiscale problems, identify the gap between what you can simulate and what you need for decision-making -- this gap is the most important research target
- Hybrid approaches are promising but immature; be explicit about the assumptions and limitations at each fidelity level when coupling models
- When integrating subsystem digital twins, expect models calibrated in isolation to behave differently when coupled -- budget for this in your validation plan

## Notable References

- Alber, M., et al. 2019. "Integrating Machine Learning and Multiscale Modeling -- Perspectives, Challenges, and Opportunities in the Biological, Biomedical, and Behavioral Sciences" (Figure 3-2 source on ML + multiscale modeling synergies)
- Bauer, P., B. Stevens, and W. Hazeleger. 2021. "A Digital Twin of Earth for the Green Transition" (Earth system digital twin vision)
- Cohen, A., and R. DeVore. 2015. "Approximation of High-Dimensional Parametric PDEs" (rigorous theory for high-dimensional approximation)
- Hartmann, D., M. Herz, and U. Wever. 2018. "Model Order Reduction a Key Technology for Digital Twins" (reduced-order models for digital twins)
