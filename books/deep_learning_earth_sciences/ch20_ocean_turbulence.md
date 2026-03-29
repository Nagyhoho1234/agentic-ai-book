# Chapter 20: Deep Learning of Unresolved Turbulent Ocean Processes in Climate Models

**Authors:** Laure Zanna and Thomas Bolton

## Summary

This chapter addresses the parameterization problem in ocean climate models: processes occurring at scales smaller than 100 km (mesoscale eddies) are unresolved by current models but critically affect large-scale ocean circulation, heat transport, and carbon uptake. The chapter presents the case for using deep learning -- particularly CNNs -- to learn subgrid eddy momentum parameterizations from high-resolution simulations, and demonstrates that physics-aware architectures (with hard-coded physical constraints) vastly outperform purely data-driven approaches. The work represents a frontier application where DL can directly improve climate projections.

## Key Concepts and Methods

### The Parameterization Problem
- Ocean models in CMIP5/CMIP6 have 0.1-1 degree resolution (~10-100 km)
- Mesoscale eddies (10-100 km) are key to ocean circulation but not resolved
- Parameterization: approximate subgrid effects P(Y_bar, u_bar) as a function of resolved fields only
- Requirements: (i) accuracy, (ii) conservation law compliance, (iii) numerical stability, (iv) generalization to new regimes

### Why DL for Subgrid Parameterization?
- Computational resources now sufficient for training large NNs
- CNNs extract spatial patterns from 2D fields -- natural for ocean dynamics
- DL can capture complex nonlinear relationships between resolved fields and subgrid forcing
- Still computationally cheaper than running high-resolution models

### Recent Advances

**Fully-connected NNs:**
- Ling et al. (2016b): Eddy momentum parameterization with Galilean-invariant tensor basis -- physical constraints improve performance over unconstrained NN
- Maulik and San (2017), Maulik et al. (2019): NN for eddy vorticity fluxes in 2D turbulence
- Salehipour and Peltier (2018): CNN for ocean vertical mixing rates -- generalizes beyond training data range

**CNNs for mesoscale eddies:**
- Bolton and Zanna (2019): CNNs parameterize eddy momentum forcing in idealized ocean models
- Generalize across different dynamical regimes and turbulence conditions
- First convolution layer learns to take spatial derivatives (velocity shears) -- a physically meaningful feature

### Physics-aware Deep Learning (Three Avenues)

1. **Learn coefficients of existing physics-based parameterizations**: Use DL to optimize unknown constants in established formulas (limited by assumption that structural form is correct)

2. **Modify loss function**: Add conservation constraints (mass, momentum, energy) as penalty terms; ensures approximate but not strict conservation (Beucler et al., 2019)

3. **Modify network architecture** (most promising):
   - Zanna and Bolton (2020): Final convolutional layer has FIXED filters representing central-difference stencils
   - Second-to-last layer outputs eddy stress tensor elements
   - Fixed final layer takes spatial derivatives (divergence) of the stress tensor
   - **Result**: Prediction is guaranteed to originate from a symmetric stress tensor, enforcing global momentum and vorticity conservation
   - 30 km coarse model + physics-aware CNN matches 3.75 km high-resolution model (Figure 20.2)

### Key Challenges

**Learning from data:**
- Defining "subgrid" via averaging is non-trivial; coarse-graining vs. spatial filtering vs. both produce different patterns
- Latitude-dependent Rossby deformation scale means filters should vary spatially

**Generalization:**
- ML parameterizations may fail outside training regime
- Solutions: train on diverse high-resolution simulations; transfer learning with observations; causal inference

**Interpretability:**
- First CNN layers interpretable (learn spatial derivatives)
- Deeper layers harder to interpret
- Data-driven equation discovery (Zanna and Bolton, 2020) can produce closed-form interpretable parameterizations

## Practical Takeaways for Scientists

1. **Physics-constrained architectures** (hard constraints via fixed layers) are essential -- soft constraints via loss penalties are insufficient for climate model stability.
2. **CNNs naturally learn spatial derivatives** as first-layer features, which is exactly what subgrid parameterizations need.
3. **Coarse-graining definition matters**: How you define the subgrid forcing determines what the ML algorithm learns.
4. **Start with idealized models**: Build and test parameterizations in simplified ocean configurations before scaling to realistic global models.
5. **Equation discovery** as a complementary approach can produce interpretable, closed-form parameterizations from DL features.

## Notable References

- Bolton and Zanna (2019) -- CNN for ocean eddy momentum parameterization
- Zanna and Bolton (2020) -- Physics-aware CNN with fixed-filter architecture
- Ling et al. (2016b) -- Galilean-invariant NN for turbulence
- Beucler et al. (2019) -- Conservation constraints in loss functions
- Gentine et al. (2018); Rasp et al. (2018) -- Atmospheric convection parameterization (related work)
