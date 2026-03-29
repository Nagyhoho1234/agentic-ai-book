# Chapter 12: Deep Learning for Detecting Extreme Weather Patterns

**Authors:** Mayur Mudigonda, Prabhat Ram, Karthik Kashinath, Evan Racah, Ankur Mahesh, Yunjie Liu, Christopher Beckham, Jim Biard, Thorsten Kurth, Sookyung Kim, Samira Kahou, Tegan Maharaj, Burlen Loring, Christopher Pal, Travis O'Brien, Ken Kunkel, Michael F. Wehner, and William D. Collins

## Summary

This chapter presents the first comprehensive application of deep learning to detect extreme weather patterns in climate model output and reanalysis data. Three progressively more sophisticated approaches are demonstrated: (1) binary classification of tropical cyclones and atmospheric rivers from cropped patches, (2) pixel-level front detection using FCN-like architectures, and (3) simultaneous classification and localization of multiple extreme event types using semi-supervised and segmentation methods (modified YOLO, Tiramisu, DeepLabv3+). The work demonstrates that DL can match or exceed traditional heuristic-based detection methods while being more objective and scalable.

## Key Concepts and Methods

### Scientific Motivation
- High-resolution climate models (25 km) produce TB-PB datasets with realistic extreme storms
- Traditional heuristic detection methods rely on subjective thresholds that vary by region and may change under climate change
- DL offers threshold-free, pattern-based detection that scales to massive datasets
- Key event types: Tropical Cyclones (TC), Extra-Tropical Cyclones (ETC), Atmospheric Rivers (AR), weather fronts (cold, warm, occluded, stationary)

### Approach 1: Binary Classification of TCs and ARs
- **Data**: CAM5.1 historical run (1979-2005, 3-hourly, 0.23x0.31 degree) for TCs; ERA-Interim reanalysis for ARs
- **Architecture**: Two convolutional layers + two FC layers (AlexNet-inspired), Bayesian hyperparameter optimization
- **Input variables**: TC -- PSL, wind, temperature, water vapor (32x32 patches); AR -- TMQ + land-sea mask (148x224 patches)
- **Results**: TC classification 99.1% accuracy; AR classification 90.0% accuracy
- **Failure modes**: TC misses on weakly developed storms; AR confusion with ETC jet streams

### Approach 2: Front Detection (Pixel-level)
- **Architecture**: 4-layer FCN with 64 5x5 filters per layer, weighted cross-entropy loss
- **Data**: MERRA-2 reanalysis (3-hourly, 2003-2016); truth from NOAA Coded Surface Bulletin (manually drawn fronts)
- **5 categories**: Cold, warm, occluded, stationary fronts + no-front
- **Results**: CNN detects ~80% of fronts found by NWS meteorologists; best for cold/occluded fronts (79-80% accuracy), worst for warm fronts (42%)
- **Spatial patterns**: Mean annual frontal frequency maps match CSB patterns well

### Approach 3: Semi-supervised Classification and Localization
- **Data**: CAM5 with 768x1152 grid cells, 16 state variables, 30 atmospheric levels
- **Architecture**: Modified YOLO predicting 64x64 bounding boxes (not from the full image)
- **Semi-supervised**: Encoder-decoder with dual objectives: (1) bounding box prediction from labeled data, (2) input reconstruction from unlabeled data
- **3D version**: Uses 8 consecutive time steps with 3D convolutions for spatiotemporal features
- **Results**: 3D semi-supervised achieves best mAP=52.92% (IOU=0.1); semi-supervised gains modest but promising

### Approach 4: Segmentation (Pixel-level Masks)
- **Architectures**: Modified Tiramisu (DenseNet-based) and DeepLabv3+ (ResNet-50 core with ASPP)
- **Data**: 63K high-resolution CAM5 samples, 16 climate variables, 3 classes (TC, AR, background)
- **Extreme class imbalance**: 98.2% background, 1.7% AR, <0.1% TC
- **Innovation**: Weighted loss using inverse square root of class frequencies (not inverse frequency -- more numerically stable)
- **Results**: DeepLabv3+ achieves 73% IoU vs. Tiramisu 59% IoU; predictions sometimes superior to heuristic labels

## Practical Takeaways for Scientists

1. **DL replaces subjective thresholds** with learned spatiotemporal patterns for extreme event detection.
2. **Start simple**: Binary classification on cropped patches achieves 99%+ accuracy for TCs and is a good proof-of-concept.
3. **Segmentation produces pixel-level masks** that can be directly compared to traditional tracker output.
4. **Class imbalance is severe** in climate data (~98% background); use inverse-square-root frequency weighting rather than inverse frequency.
5. **Semi-supervised learning** can leverage abundant unlabeled climate simulation data alongside limited labeled samples.
6. **ClimateNet** (https://www.nersc.gov) and climatecontours tool are community resources for labeled climate data.

## Notable References

- Liu et al. (2016b, c) -- TC and AR binary classification with CNNs
- Racah et al. (2016) -- Semi-supervised extreme event detection
- Mudigonda et al. (2018) -- Segmentation-based climate event detection
- Prabhat et al. (2018) -- ClimateNet and labeled climate datasets
- Kurth et al. (2017, 2018) -- Scaled DL for climate on supercomputers
