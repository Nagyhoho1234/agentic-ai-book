# Chapter 21: Deep Learning for the Parametrization of Subgrid Processes in Climate Models

**Authors:** Pierre Gentine, Veronika Eyring, and Tom Beucler

## Summary

This chapter presents pioneering work on using deep neural networks to replace traditional cloud and convection parameterizations in climate models. Cloud and convection processes operate at scales smaller than the ~100 km grid spacing of current Earth system models and are the largest source of uncertainty in climate sensitivity estimates (which have ranged from 2.1 to 4.7 degrees C for decades). The authors demonstrate that NNs trained on high-resolution cloud-resolving model (CRM) simulations can accurately emulate subgrid convective heating and moistening, and discuss the critical challenges of enforcing physical conservation laws and achieving generalization to unseen climate states.

## Key Concepts and Methods

### The Climate Sensitivity Problem
- Effective Climate Sensitivity (ECS): temperature change from doubling CO2; range 2.1-4.7 degrees C unchanged since Charney (1979)
- Largest uncertainty source: cloud and convection parameterizations
- High-resolution CRMs (few km) explicitly resolve deep clouds but are too expensive for long climate simulations
- Goal: Train NNs on CRM output to create better parameterizations for coarse GCMs

### Super-Parameterization (SP) Approach
- Embed 2D CRMs within each GCM grid column (SP-CAM setup)
- Aquaplanet configuration (no continents/topography, steady latitudinal temperature gradient)
- NN inputs: vertical profiles of temperature T(z) and humidity q(z), surface pressure, insolation, sensible/latent heat fluxes
- NN outputs: heating and moistening tendencies (dT/dt, dq/dt)
- Bypasses the difficult coarse-graining step since CRM is already embedded at GCM scale

### Key Results (Gentine et al., 2018; Rasp et al., 2018)
- NN correctly reproduces CRM convective heating/moistening patterns in offline mode
- In coupled online mode: captures equatorial wave dynamics, Walker circulation, Madden-Julian Oscillation (not in training data!)
- Better precipitation distribution than traditional parameterizations (less "drizzle")
- Training requires >6 months (~140M samples) for convergence; alternatively 40M samples with hyperparameter optimization
- Random forests with very fine time steps (<1 min) can nearly perfectly reproduce precipitation extremes (Yuval and O'Gorman, 2020)

### Physical Constraints and Conservation (Beucler et al., 2019)
- **Problem**: Standard NNs violate mass and energy conservation (~1 W/m2 spurious energy), which is unacceptable for climate modeling
- **Solution**: Architecture-constrained NNs with fixed "constraints layers" that combine NN outputs to enforce exact conservation
- Constrained NN enforces enthalpy, mass, longwave, and shortwave conservation to machine precision (~10^-8 W^2/m^-4 vs ~10^2 for unconstrained)
- Goes beyond soft constraints (Lagrange multiplier regularization) which are only approximately satisfied
- Also enforces nonlinear constraints (unlike random forests which only enforce linear constraints by default)

### Generalization Challenges
- NNs trained on one climate state (0 K) fail to generalize to warmer (+4 K) or cooler (-4 K) climates
- Typical failure mode: double-ITCZ bias (same as traditional parameterizations)
- Solutions: (1) Train on multiple climate states; (2) Rescale inputs/outputs to transform extrapolation into interpolation (Beucler et al., 2020); (3) Switch to traditional parameterization when NN error detected
- Coupled model instabilities remain a concern (Brenowitz and Bretherton, 2019)

## Practical Takeaways for Scientists

1. **NNs can replace convection parameterizations** in climate models -- the proof of concept is established.
2. **Conservation must be enforced architecturally** (hard constraints), not via loss function penalties (soft constraints).
3. **Generalization to new climates is the critical bottleneck** -- models trained on present climate may not work for future climate projections.
4. **Coupled model stability** requires careful attention; diagnostic tools exist to detect when NNs create unrealistic convection (Brenowitz et al., 2020).
5. **Future directions**: 3D CRMs (not just 2D), inclusion of topography and land surfaces, shallow cloud parameterization (crucial for climate sensitivity).

## Notable References

- Gentine et al. (2018) -- First NN emulation of deep convection
- Rasp et al. (2018) -- NN convection parameterization in coupled SP-CAM
- Beucler et al. (2019) -- Architecture-constrained NNs for conservation
- Brenowitz and Bretherton (2018, 2019, 2020) -- 3D CRM emulation, stability analysis
- Yuval and O'Gorman (2020) -- Random forests for precipitation extremes
- Schneider et al. (2017b) -- Climate sensitivity and cloud parameterization
