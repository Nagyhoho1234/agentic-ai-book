# Chapter 19: Applications of Deep Learning in Hydrology

**Authors:** Chaopeng Shen and Kathryn Lawson

## Summary

This chapter provides a comprehensive review of deep learning applications in hydrology, covering the rapid evolution from 2017 to early 2020. Hydrology was among the earliest geoscience fields to adopt DL, with LSTM networks proving remarkably effective at rainfall-runoff modeling, soil moisture prediction, and streamflow forecasting. The chapter organizes applications along two axes: data availability (big data vs. limited data) and physics integration (pure data-driven vs. physics-informed), and surveys dynamical system modeling, information retrieval, physics-constrained ML, and subsurface flow modeling. The key finding is that LSTMs can outperform decades-old conceptual hydrologic models across hundreds of basins when trained with sufficient data.

## Key Concepts and Methods

### Dynamical System Modeling with Big Data
- **Soil moisture prediction**: LSTM trained on SMAP satellite data achieves test error of 0.027, smaller than SMAP's design accuracy (Fang et al., 2017)
- **Rainfall-runoff modeling**: Regional LSTM trained across CONUS basins matches or exceeds SAC-SMA and other conceptual models (Kratzert et al., 2018, 2019); median NSE ~0.75
- **Data integration (DI)**: Closed-loop kernel assimilates recent SMAP observations into LSTM predictions; median 1-day forecast error <0.021 (Fang and Shen, 2020)
- **Streamflow forecasting**: LSTM with DI on CAMELS dataset achieves unprecedented median daily NSE of 0.86 (Feng et al., 2020a)
- **Flood prediction**: LSTM improves global flood peak timing predictions (Yang et al., 2019b)

### Data-limited LSTM Applications
- Groundwater level forecasting (up to 18 hours lead time)
- Lake water level prediction (Dongting Lake, centimeter accuracy)
- Flood forecasting at individual stations (NSE > 0.97 with lagged discharge)
- Reservoir operation modeling (NSE 0.66-0.93 across Southeast Asian reservoirs)
- Urban water systems: wastewater flow, water quality at intakes

### Information Retrieval for Hydrology
- Reservoir/lake identification from Landsat-8 imagery (ResNet-50)
- Precipitation estimation from surveillance camera imagery
- Snow cover detection from crowdsourced camera networks (97% accuracy)
- Urban water-logging depth extraction from video (transfer learning with Inception V3)
- Precipitation downscaling from NCEP reanalysis using CNNs

### Physics-constrained Hydrologic Machine Learning
- **Penman-Monteith + LSTM**: Hybrid model estimates stomatal resistance with LSTM, couples to Penman-Monteith ET equation; conserves surface energy balance; better extrapolation than pure data-driven models (Zhao et al., 2019)
- **Process-guided DL for lake temperature**: LSTM with soft penalty for energy conservation violation; pre-trained with process-based model outputs (Read et al., 2019)
- Physics principles that can be integrated are few and engineering complexity increases rapidly

### Physically-informed ML for Subsurface Flow
- **GANs for inverse problems**: Generate hydraulic conductivity (K) fields from hydraulic head (H) observations (Sun, 2018)
- **DenseNet surrogates**: Multi-phase flow and reactive transport as image-to-image regression (Mo et al., 2019)
- **Physics-Informed Neural Networks (PINNs)**: Supervise network derivatives to satisfy PDEs; extended to groundwater flow (Tartakovsky et al., 2018; Raissi et al., 2019)
- PINNs still nascent: require retraining for each boundary/initial condition combination

## Practical Takeaways for Scientists

1. **LSTMs are the go-to architecture for hydrologic time series** -- they can match or beat decades of hydrologic model development when sufficient data is available.
2. **Regional/continental training** (many basins, many years) produces better models than site-specific training.
3. **Data integration** (assimilating recent observations) dramatically improves forecast accuracy.
4. **Physics-constrained DL** improves extrapolation and generalization but is harder to engineer.
5. **Uncertainty quantification** via Monte Carlo dropout is promising but needs more testing.
6. **Key limitations**: Interpretability is weak; site-specific models don't transfer; DL focuses on single tasks rather than integrated modeling.

## Notable References

- Fang et al. (2017) -- LSTM for soil moisture from SMAP
- Kratzert et al. (2018, 2019) -- LSTM for rainfall-runoff modeling
- Feng et al. (2020a) -- LSTM with data integration on CAMELS
- Raissi et al. (2019) -- Physics-Informed Neural Networks
- Sun (2018) -- GANs for subsurface inverse problems
- Shen (2018a) -- Review of DL in hydrology
