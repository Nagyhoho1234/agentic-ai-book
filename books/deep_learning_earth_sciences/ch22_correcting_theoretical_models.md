# Chapter 22: Using Deep Learning to Correct Theoretically-derived Models

**Author:** Peter A. G. Watson

## Summary

This chapter presents a hybrid modeling approach where deep learning is used not to replace but to correct errors in theoretically-derived (physics-based) dynamical models. The total model takes the form dx/dt = M(x) + c(x), where M(x) is the physics-based prediction and c(x) is the ANN-learned correction term. This approach is more practical than pure DL replacement because c(x) only needs to learn the relatively small error term rather than the entire dynamics, and the physics-based component ensures behavior remains physically reasonable in novel conditions. Experiments with the Lorenz '96 chaotic system demonstrate that even simple ANNs can improve both short-range forecasts and long-term climate statistics.

## Key Concepts and Methods

### The Error-Correction Framework
- Dynamical model: dx/dt = M(x) + c(x)
- M(x): theoretically-derived model (physics-based, interpretable)
- c(x): ANN-learned correction (trained on differences between truth and model predictions)
- Key advantage: c(x) is much simpler than learning dx/dt from scratch since |c(x)| << |M(x)|
- Physics model retains its critical role; DL component only adds incremental improvement

### Prior Work
- Forssell and Lindskog (1997): Water tank problem -- hybrid model halved RMSE, avoided unphysical predictions
- Cooper and Zanna (2015): Stochastic linear corrections to ocean model; reduced bias/variance by 10x
- Karpatne et al. (2017d): Physics penalty in NN loss (lake temperature density constraint); 30% RMSE reduction
- Pathak et al. (2018): Reservoir computing + knowledge-based model for chaotic systems; hybrid predictions stayed accurate 2-3x longer

### Lorenz '96 Experiments

**System setup:**
- Two-scale chaotic system: slow X variables (K=8) and fast Y variables (J=32 per X)
- "Truth": full X+Y system at fine time step
- Coarse model: X variables only with polynomial parameterization U(X) for Y effects
- ANN correction: learns c_k = true tendency - coarse model tendency

**ANN architecture:**
- MLP with 1-3 hidden layers, 2 to 64 neurons per layer, ReLU activation
- Trained on 1000 time units (200,000 time steps)
- Local predictions: each grid point uses only nearby X values (up to 2 grid points away)

**Results:**

1. **Single-timestep tendency**: Every ANN tested reduces RMSE compared to No-ANN baseline; up to 42% reduction; improvements increase with parameter count but saturate around ~100 parameters

2. **Forecast skill** (1 time unit = ~week-equivalent):
   - All but simplest (2-neuron) ANNs improve both ACC and RMSE
   - ACC increases from ~0.46 to ~0.49; RMSE decreases from ~5.89 to ~5.73
   - Improvements are about half the maximum possible improvement (limited by how close the base model already is to truth)
   - No large gain from increasing complexity beyond ~50 parameters

3. **Climate statistics** (3000 time unit simulations):
   - KS statistic improved by nearly all ANN structures
   - Mean bias not clearly improved
   - ANNs correct the excessive central peak in X distribution and reduce deficit in the negative flank
   - Best results with ~100 parameters, 2-layer ANNs

4. **Seamless prediction**: Short-range skill correlates with long-range climate statistics (r = 0.15-0.81), suggesting weather forecast quality can indicate climate simulation quality

### Discussion and Outlook
- **Scaling to Earth system models**: Requires handling sparse observations (6-hourly), shorter model time steps, and backpropagation through time and space
- **Reanalysis data** could be used for training in lieu of "truth"
- **Climate change**: Hybrid models can represent forced changes (e.g., CO2 effects) through the physics component while ML handles variability
- **Event attribution**: Hybrid models could improve estimates of extreme weather risk under changing climate

## Practical Takeaways for Scientists

1. **Correct, don't replace**: Adding a DL correction to an existing physics model is more practical and robust than building a pure DL model.
2. **Even tiny ANNs help**: A network with just 4 neurons in one hidden layer can significantly improve a chaotic system simulation.
3. **Weather skill predicts climate quality**: Short-range forecast improvements correlate with better long-term statistics -- useful for model selection.
4. **The hybrid approach preserves interpretability**: The physics model explains most of the dynamics; DL only fills gaps.
5. **Training data requirements are modest**: 2 time units of training data suffice for good results in the Lorenz '96 system.

## Notable References

- Watson (2019) -- Lorenz '96 error-correction experiments
- Pathak et al. (2018) -- Hybrid reservoir computing for chaotic systems
- Karpatne et al. (2017a, 2017d) -- Theory-guided data science
- Chattopadhyay et al. (2019) -- Memory-incorporating error correction for extreme values
- Palmer et al. (2008) -- Seamless prediction concept
- Bocquet et al. (2020) -- Joint learning of model and state
