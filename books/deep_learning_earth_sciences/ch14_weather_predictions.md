# Chapter 14: Deep Learning to Improve Weather Predictions

**Authors:** Peter D. Dueben, Peter Bauer, and Samantha Adams

## Summary

This chapter provides a strategic overview of how machine learning and deep learning can enhance the entire workflow of numerical weather prediction (NWP), from data acquisition through forecast dissemination. Written from the perspective of operational weather prediction centers (ECMWF, UK Met Office), it identifies concrete opportunities at every stage of the NWP pipeline. The chapter argues that while ML will not replace physics-based models in the near term, it can augment them significantly -- particularly for subgrid parameterizations, data assimilation, nowcasting, and post-processing.

## Key Concepts and Methods

### The NWP Workflow
1. **Observations**: Collected from satellites, ships, planes, weather balloons, ground stations (hundreds of millions per day)
2. **Data Assimilation (DA)**: Combines observations with model state to produce initial conditions; must estimate observation errors and model biases
3. **Forecast Model**: Propagates initial conditions forward using equations of motion; 10 km grid spacing, millions of lines of code
4. **Post-processing & Dissemination**: Selection, compression, and distribution of model output; ECMWF produces 70 TB/day

### Key Challenges in NWP
- Error doubling time limits forecast horizon (Edward Lorenz)
- Subgrid processes (clouds, convection, turbulence) must be parameterized -- these are approximations
- Doubling resolution requires 2^4 = 16x computational cost (space + time)
- Forecast model software is >1M lines of code, difficult to port to new hardware

### ML Opportunities Across the Workflow

**Observations:**
- Feature detection and error correction in satellite observations
- Bias correction for systematic measurement errors
- Gap-filling strategies for incomplete coverage
- Nowcasting (0-6 hour predictions) directly from radar/satellite data

**Data Assimilation:**
- ML for error covariance matrix estimation (currently assumed linear/Gaussian)
- Neural network emulators as tangent linear/adjoint models for 4DVar DA
- GANs for learning mappings between observation and model space (Hall et al., 2018)
- Adaptive localization in ensemble Kalman filters (Moosavi et al., 2019)

**Forecast Model:**
- **Emulating parameterizations**: Train NNs on high-resolution simulations to replace subgrid schemes
  - Cloud physics and convection (Brenowitz and Bretherton, 2019; Gentine et al., 2018; Rasp et al., 2018)
  - Radiation schemes: NNs can represent 3D cloud effects too expensive for current schemes
  - Ozone representation (He et al., 2019b)
- **Replacing entire models**: Learn equations of motion from reanalysis data (Dueben and Bauer, 2018; Scher and Messori, 2019; Weyn et al., 2019)
- **Hardware acceleration**: NNs naturally suited to GPUs/TPUs; TensorCores for spectral transforms

**Post-processing & Dissemination:**
- Automated anomaly/extreme event detection in model output
- Data compression via feature extraction
- Regional downscaling using NNs trained on topography + local observations
- Bias correction and ensemble spread correction
- Seasonal prediction (El Nino indices via NN correction of simple dynamical models)

### Critical Assessment
- Short-term: ML will augment physics-based models (hybrid approach)
- Medium-term: ML may replace specific model components (parameterizations)
- Long-term (speculative): ML could potentially replace entire forecast models, but many scientists remain skeptical about representing complex process interactions
- Physics-guided neural networks (hybrid models) are the most promising direction

## Practical Takeaways for Scientists

1. **Nowcasting is the lowest-hanging fruit** -- ML predictions from radar/satellite data for 0-6 hour horizons can complement NWP.
2. **Emulating parameterizations** is the most impactful near-term opportunity -- NNs trained on high-resolution simulations can replace expensive subgrid schemes.
3. **Data assimilation with ML** can relax the linearity/Gaussianity assumptions that limit current methods.
4. **Post-processing with NNs** (bias correction, downscaling) provides immediate value with relatively low risk.
5. **ECMWF data volumes** (233 TB/day growth, 210 PB archive) make ML-based data compression and feature extraction essential.
6. **Hardware synergy**: NNs run naturally on GPUs/TPUs that weather centers are already deploying.

## Notable References

- Dueben and Bauer (2018) -- First NN-based global weather forecasts
- Brenowitz and Bretherton (2019) -- NN parameterizations for cloud physics
- Rasp et al. (2018) -- NN for convective parameterization
- Scher and Messori (2019) -- NN as complete weather model
- Bauer et al. (2015) -- NWP revolution overview
- Reichstein et al. (2019) -- Deep learning for Earth system science
