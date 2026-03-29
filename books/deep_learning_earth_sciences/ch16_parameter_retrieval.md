# Chapter 16: Deep Learning for High-dimensional Parameter Retrieval

**Author:** David Malmgren-Hansen

## Summary

This chapter addresses the inverse problem of retrieving bio-geophysical parameters from remote sensing observations using deep learning. Parameter retrieval maps from measurements (radiometric observations) to physical quantities (temperature, vegetation indices, sea ice concentration, etc.) -- the inverse of what radiative transfer models (RTMs) compute. The chapter discusses the unique challenges of high-dimensional input data (e.g., 8461 spectral channels from IASI), presents three architectural strategies for handling spatial-spectral-temporal dependencies, and demonstrates two case studies: atmospheric temperature retrieval from IASI hyperspectral data and sea ice prediction from SAR imagery.

## Key Concepts and Methods

### The Inverse Problem
- Forward problem: physics models (RTMs) map parameters to observations
- Inverse problem: retrieve parameters from observations -- often ill-posed, multi-modal, or under-determined
- Bio-geophysical parameters: biological (LAI, chlorophyll), physical (soil moisture, temperature), chemical (trace gases), geographical (land cover, sea ice)

### Application Domains
- **Land**: LAI, leaf chlorophyll content, land surface temperature, crop yield, forest biomass
- **Ocean**: Chlorophyll, SST, sea ice concentration, water quality
- **Cryosphere**: Sea ice cover/concentration (SIC), sea ice types (SIT), snow depth, snow water equivalent
- **Weather models**: Temperature, humidity, pressure, wind speed profiles for NWP data assimilation

### Architectural Strategies for High-dimensional Data
Three ways to handle (X, Y, B, T) tensors -- spatial (X,Y), spectral (B), temporal (T):

1. **Cubic convolutions**: (X,Y,B) data cube with 3D filters spanning space and spectrum, stacking T time steps as additional channels
2. **Channel stacking**: Stack spectral bands B and time steps T as 2D convolution channels, yielding B*T input channels for 2D spatial convolutions
3. **CNN + RNN hybrid**: CNN extracts spatial-spectral features from (X,Y,B) at each time step; RNN (LSTM) processes the temporal sequence of feature vectors

### Computational Considerations
- IASI example: 43.8M product-sum operations for 639K-parameter CNN
- Full spectral cube convolutions: 2.8 billion operations vs. 11M with depth-wise separable convolutions
- PCA/MNF preprocessing can reduce spectral dimension 37.6x (4699 to 125 channels), dramatically cutting memory/compute
- Trade-off: memory chunk size (batch x spatial x spectral x data type) affects GPU utilization

### Loss Function Choice
- **MSE loss**: Maximum likelihood when errors are Gaussian; appropriate for continuous parameters (temperature, concentrations)
- **Cross-entropy loss**: Maximum likelihood for categorical/binary targets; can be used for concentration retrieval by discretizing
- **Mixture Density Networks (MDN)**: Predict probability distributions instead of point estimates -- handles multi-modal inverse problems

### Case Study 1: Atmospheric Temperature Retrieval from IASI
- IASI on MetOp satellites: 8461 spectral channels, 12 km footprint, 25 km resolution
- MNF reduces to 125 highest-SNR components; CNN operates on 15x15 spatial neighborhoods
- Retrieves 90 lowest atmospheric temperature levels simultaneously
- CNN achieves RMSE = 1.94 K vs. OLS regression RMSE = 2.85 K (32% improvement)
- CNN produces smoother, more physically consistent temperature profiles than independent OLS predictions
- Spatial context (neighborhood information) is the key advantage of CNNs

### Case Study 2: Sea Ice Prediction from SAR
- Sentinel-1 SAR over Arctic; predict sea ice concentration in 18x18 km blocks
- Binary classification (ice/no-ice) and regression (concentration percentage)
- CNN with 5 convolutional layers, 639K parameters
- Demonstrates that treating concentrations as classification (cross-entropy) or regression (MSE) can both work

## Practical Takeaways for Scientists

1. **Dimensionality reduction first**: Apply PCA/MNF to hyperspectral data before feeding to CNNs -- reduces compute by 30x+ with minimal information loss.
2. **CNNs capture spatial context** that point-wise regression cannot -- this is the primary advantage over traditional statistical retrieval.
3. **Depth-wise separable convolutions** reduce cubic convolution costs by ~250x -- essential for high-dimensional spectral data.
4. **MSE vs. cross-entropy**: Use MSE for continuous parameters, cross-entropy for categorical; consider MDNs for multi-modal inverse problems.
5. **Hybrid CNN+RNN** architectures are best when both spatial and temporal dependencies matter (e.g., sea ice monitoring over time).
6. **Code and data**: IASI data available from EUMETSAT; reference forecasts from ECMWF.

## Notable References

- Malmgren-Hansen et al. (2020) -- CNN for IASI atmospheric temperature retrieval
- Wang et al. (2017c) -- CNN for sea ice concentration from SAR
- Verrelst et al. (2015) -- Bio-geophysical parameter retrieval overview
- Bishop (2006) -- Mixture Density Networks for multi-modal regression
- Reichstein et al. (2019) -- DL for Earth system science
