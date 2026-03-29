# Chapter 7: Deep Domain Adaptation in Earth Observation

**Authors:** Benjamin Kellenberger, Onur Tasar, Bharath Bhushan Damodaran, Nicolas Courty, and Devis Tuia

## Summary

This chapter addresses one of the most pervasive challenges in Earth observation: dataset shift. Models trained on one sensor, location, or time period often fail when applied to data from another due to differences in atmospheric conditions, sensor characteristics, illumination, geographic variation, and temporal concept drift. The chapter presents a systematic categorization of deep domain adaptation (DA) methods into three families, with detailed experimental comparisons on real RS datasets. The key insight is that no single DA approach dominates; the choice depends on the nature and severity of the domain shift.

## Key Concepts and Methods

### Types of Domain Shift in Earth Observation
1. **Dataset shift**: Different sensors, atmospheric effects, illumination (e.g., morning vs. noon), different spectral ranges even for "same" bands across satellites
2. **Concept drift**: Class definitions change over time/space (e.g., crops at different growth stages, buildings with different architectural styles across regions)
3. **Multi-modal domain shift**: Source and target domains use different data modalities (e.g., optical vs. SAR, different sensor networks)

### Three Families of DA Methods

**Family 1: Adapting the Inner Representation**
- Impose a domain adaptation loss on intermediate feature vectors to make source and target representations similar
- **MMD (Maximum Mean Discrepancy)**: Assimilates source/target features by minimizing distances between expected values
- **DeepCORAL**: Minimizes covariance differences between source and target feature vectors
- **DeepJDOT (Deep Joint Optimal Transport)**: Minimizes feature vector discrepancy using Optimal Transport while incorporating label information -- best performer (0.75/0.73 accuracy vs. 0.66/0.59 baseline)

**Family 2: Adapting the Input Distribution**
- Transform input data to reduce domain gap before classification
- **Generate synthetic data**: CycleGAN, UNIT, MUNIT, DRIT, ColorMapGAN -- translate source images to look like target
- **Standardize both domains**: Map both to a common subspace (histogram matching, Gray world algorithm)
- **Key finding**: ColorMapGAN performed best (65.02% F1) among GAN-based methods; MUNIT and DRIT failed because they generated semantically inconsistent fake data

**Family 3: Using Few Labels from the Target Domain (Semi-supervised DA)**
- When unsupervised DA fails (severe shift, class imbalance), use active learning to select a few well-chosen target samples
- **Transfer Sampling (TS)**: Uses Optimal Transport to find correspondences between source and target true positives, robust to class imbalance
- Applied to wildlife detection from drone imagery (Kuzikus reserve, Namibia)
- TS finds 80% of target animals with fewer oracle queries than conventional AL methods

### Experimental Results
- Inner representation: DeepJDOT significantly outperforms MMD and DeepCORAL on RS classification (UC Merced vs. WHU-RS19)
- Input adaptation: ColorMapGAN best for semantic segmentation across cities (Bad Ischl to Villach, Pleiades imagery)
- Semi-supervised: Transfer Sampling most efficient for animal detection across years (drone survey data)

## Practical Takeaways for Scientists

1. **Always test for domain shift**: Apply your trained model to the target domain first; if accuracy drops >10%, domain adaptation is needed.
2. **DeepJDOT** is recommended for inner representation adaptation -- it considers label information and works with specific source-target correspondences.
3. **ColorMapGAN** is the most reliable GAN-based input adaptation method -- it preserves semantic consistency better than CycleGAN or UNIT.
4. **Avoid MUNIT and DRIT** for RS data -- they tend to generate semantically inconsistent images.
5. **Active learning with Transfer Sampling** is the best option when class imbalance is severe or the domain gap is too large for unsupervised methods.
6. **Reproducible code** is available at https://github.com/bkellenb/da-dl4eo

## Notable References

- Damodaran et al. (2018) -- DeepJDOT
- Sun and Saenko (2016) -- DeepCORAL
- Mingsheng et al. (2015) -- MMD for domain adaptation
- Tasar et al. (2020) -- ColorMapGAN
- Kellenberger et al. (2019) -- Transfer Sampling for wildlife detection
- Courty et al. (2017) -- Optimal Transport for domain adaptation
