# Chapter 5: Feedback Flow from Physical to Virtual -- Foundational Research Needs and Opportunities

## Comprehensive Summary

This chapter addresses the physical-to-virtual direction of the digital twin feedback loop: how observational data from the physical system are used to calibrate, update, and improve the virtual representation. The key technical areas are inverse problems, data assimilation, parameter estimation, and optimization under uncertainty.

### Inverse Problems and Digital Twin Calibration

Digital twin calibration involves estimating numerical model parameters for individualized virtual representations. This is mathematically an **inverse problem** -- estimating parameters and states that are not directly observable from available data. Key challenges:

- The inverse problem may be **ill-posed**: the solution may not exist, may not be unique, or may not depend continuously on the data
- **Identifiability**: can the parameters be uniquely determined from the available data?
- **Stability**: small errors in data can produce large errors in reconstructed parameters

**Bayesian approaches** are central to handling these challenges. They encode priors as probability distributions to handle missing information, ill-posedness, and uncertainty. However, digital twins present specific Bayesian challenges:
- Standard priors (e.g., simple Gaussian) may not be informative for high-stakes decisions
- Updated models need to be incorporated on the fly without restarting from scratch (the prior for one problem becomes the posterior from the previous)
- Priors that capture distribution tails are needed for extreme events

**Data-driven regularization** can learn priors from existing data (e.g., ML-informed bias correction), but may not accurately represent extreme events due to limited relevant training data.

### Parameter Estimation and Regularization

Parameter estimation from data is ill-posed by nature. Approaches include:
- Bayesian regularization with informative priors
- Data-driven priors learned from historical data
- Methods tuned to risk and extreme events rather than just average performance
- Risk-adaptive loss functions for capturing extreme events during inversion

A key challenge is **non-differentiability**: many models exhibit discontinuous behavior or chaotic dynamics, making standard gradient-based methods (including adjoint methods) intractable. Robust optimization techniques beyond gradient-based methods are needed.

### Optimization of Numerical Model Parameters Under Uncertainty

Every computational model must be calibrated to meet its requirements and be fit for purpose. Challenges:
- Cost functions are stochastic and must incorporate different types of uncertainty
- Methods must be tuned to risk and extreme events for high-consequence decisions
- Non-differentiability complicates gradient-based optimization and advanced UQ methods (stochastic Galerkin, stochastic collocation)
- Monte Carlo sampling becomes extremely inefficient for low-probability events

### Data Assimilation and Digital Twin Updating

Data assimilation -- combining model predictions with observations to improve model states -- has been used extensively in numerical weather forecasting. But for digital twins, several gaps remain:

1. **Assumptions of high-fidelity models**: existing DA methods assume model fidelity that may evolve or degrade over time as the physical counterpart changes
2. **Uncertainty quantification for high-consequence decisions**: DA provides predictions with uncertainties but lacks the decision-making interface (risk measures) needed for digital twins
3. **Integration of AI/ML/data science tools**: few mechanisms exist for integrating these with DA codes at the unprecedented data rates of modern digital technologies

### Digital Twins Demand Continual Updates

Updates must be incorporated in a timely way (often immediately) using partial and noisy observations. Sequential approaches (particle filters, ensemble Kalman filters) are natural but have disadvantages: sampling errors, rank deficiency, inconsistent assimilation of asynchronous observations.

DA techniques must handle:
- Continuous data streams from different sources
- Varying levels of uncertainty
- Evolving system state under uncertainty
- Discrepancies between predictions and observed data
- Tools for model update documentation and hierarchy tracking

### Digital Twins Demand Actionable Time Scales

Most DA literature focuses on offline assimilation, but digital twins require real-time or near-real-time assimilation. For weather forecasting, this means gathering, ingesting, processing, and assimilating global observations within hours. High-performance computing implementations and new DA approaches that exploit effective dimensionality (e.g., latent data assimilation) are needed.

### Large-Scale Uncertainty Quantification

For many digital twins, the number of parameters to estimate is enormous (e.g., climate models with hundreds of millions of spatial degrees of freedom). Strategies include:
- Reducing dimensionality via surrogate models
- Imposing structure or informative priors (e.g., Bayesian neural networks, sparsity-promoting regularizers)
- Goal-oriented approaches where quantities of interest from predictions are identified and estimated directly

## Key Research Gaps Identified

**Priority 1:**
- Tools for tracking model and related data provenance (maintaining history of model updates)
- New uncertainty quantification methods for large-scale problems that can capture extreme behavior and provide reliable risk analysis
- New data assimilation methods handling multiple channels/scales with different uncertainty levels
- Risk-adaptive loss functions and data-informed prior distributions for capturing extreme events during inversion
- Standards and governance policies for data quality, accuracy, security, and integrity

**Priority 2:**
- High-performance computing implementations of state-of-the-art DA codes (particle filters, ensemble Kalman filters, emulators)
- Machine learning for uncertainty quantification (diffusion models, generative AI)
- More realistic prior distributions or data-driven regularization for Bayesian solutions

## Practical Takeaways for Scientists

- If you are building a digital twin that will be updated over time, plan for **sequential Bayesian updating** from the start -- the posterior from each assimilation cycle becomes the prior for the next
- Do not assume your model parameters are identifiable -- perform identifiability analysis before investing in expensive calibration campaigns
- For high-consequence applications, standard loss functions (least-squares) are insufficient; invest in risk-adaptive loss functions that account for tail behavior
- If your model is non-differentiable (common in chaotic systems, phase transitions, switching dynamics), standard adjoint methods will fail -- explore gradient-free or Monte Carlo gradient estimation approaches
- The weather/climate data assimilation community has decades of experience in real-time DA at scale -- seek collaboration and technology transfer
- Track and document every model update with provenance metadata -- this is essential for reproducibility and trust

## Notable References

- Blair, G.S. 2021. "Digital Twins of the Natural Environment" (DA for environmental digital twins)
- Royset, J.O. 2023. "Risk-Adaptive Decision-Making and Learning" (risk-adaptive approaches for digital twins)
