# Chapter 17: A Review of Deep Learning for Cryospheric Studies

**Author:** Lin Liu

## Summary

This chapter provides a comprehensive review of deep learning applications across all major components of the cryosphere: glaciers, ice sheets, snow, permafrost, sea ice, and river ice. The cryosphere stores 75% of Earth's fresh water and is undergoing rapid changes due to climate warming -- Arctic sea ice has decreased ~12.8% per decade since 1979, and both Greenland and Antarctic ice sheets are losing mass at accelerated rates. DL has been applied to nearly all cryospheric remote sensing tasks (detection, delineation, classification, extraction, prediction) and a limited number of modeling tasks, though most applications remain demonstrative rather than operational.

## Key Concepts and Methods

### Glaciers
- **Calving front delineation**: U-Net applied to Landsat (Mohajerani et al., 2019), TerraSAR-X (Zhang et al., 2019), and Sentinel-1 + TanDEM (Baumhoer et al., 2019)
- **Debris-covered glacier mapping**: Feed-forward NN with 17 input layers (Landsat-8 + DEM + topo-geomorphic parameters); transfer learning from Karakoram to Nepal (Xie et al., 2020)
- **Surface mass balance**: DL parameterizes nonlinear link between topographic/climatic variables and glacier SMB; 6-layer FC network in ALpine Parameterized Glacier Model (ALPGM)
- **DeepBedMap**: GAN-based super-resolution of Antarctic ice sheet bed elevation from 1 km to 250 m resolution

### Ice Sheets
- DeepBedMap (Leong and Horgan, 2020): Conditional inputs include surface elevation, ice velocity, snow accumulation
- Supraglacial lake extraction from Landsat-8 using CNN (Yuan et al., 2020a)

### Snow
- Snow cover classification from multispectral imagery (DeepLabv3+, AlexNet hybrids)
- Snow depth retrieval from passive microwave radiometry using fully connected DL networks
- DL-estimated snow depth improves sea ice thickness retrieval from altimeters

### Permafrost
- **Ice wedge polygons**: Mask R-CNN detects/classifies ice wedge polygons from 0.15-1 m aerial/satellite imagery; 79% detection rate over 134 km2
- **Thermokarst landforms**: DeepLab v2/v3+ maps thermo-erosion gullies (UAV imagery) and retrogressive thaw slumps (CubeSat imagery, 220 mapped over 5200 km2)

### Sea Ice
- **Concentration retrieval**: CNNs from RADARSAT-2 SAR, AMSR-E passive microwave, GNSS reflectometry
- **Ice type classification**: From EO-1 hyperspectral and multi-temporal SAR
- **Ice thickness estimation**: From terrestrial laser scanning 3D geomorphic features
- **Prediction**: CNN with 8 predictors over 30 years achieves best performance for 1-month-ahead sea ice concentration forecasting

### River Ice
- Semantic segmentation (U-Net, SegNet, DeepLabv3+, DenseNet) of UAV/fixed camera imagery
- Classification: water, frazil ice, anchor ice

## Practical Takeaways for Scientists

1. **U-Net is the dominant architecture** for cryospheric segmentation tasks (calving fronts, snow cover, ice types).
2. **Transfer learning works** across glaciers/regions -- Karakoram-trained models improve Nepal glacier mapping.
3. **Labeled data is the major bottleneck** -- most studies create their own datasets; community benchmark datasets are needed.
4. **DL for cryospheric modeling** is still nascent -- only sea ice concentration prediction and glacier SMB have been attempted.
5. **Key data centers**: NSIDC, Arctic Data Center, ESA CCI (glaciers, sea ice, permafrost, snow).
6. **Code repositories** are listed in the appendix for each cryospheric component -- a valuable starting point.

## Notable References

- Baumhoer et al. (2019) -- Sentinel-1 glacier calving front detection
- Leong and Horgan (2020) -- DeepBedMap (GAN for ice sheet bed elevation)
- Zhang et al. (2018) -- Ice wedge polygon detection with Mask R-CNN
- Kim et al. (2020) -- CNN for sea ice concentration prediction
- Bolibar et al. (2020) -- DL for glacier surface mass balance (ALPGM)
- Huang et al. (2018, 2020) -- Thermokarst landform mapping with DeepLab
