# Chapter 10: Multisource Remote Sensing Image Fusion

**Authors:** Wei He, Danfeng Hong, Giuseppe Scarpa, Tatsumi Uezato, and Naoto Yokoya

## Summary

This chapter reviews deep learning methods for two key spatial-spectral resolution enhancement tasks: pansharpening (fusing panchromatic and multispectral images) and multiband image fusion (fusing hyperspectral and multispectral images). DL methods consistently outperform traditional approaches in reconstruction quality while maintaining fast inference times. The chapter provides detailed experimental comparisons on WorldView-2 data for pansharpening and Chikusei/CAVE datasets for multiband fusion.

## Key Concepts and Methods

### Pansharpening
- **Goal**: Combine high-spatial-resolution panchromatic (PAN) band with lower-resolution multispectral (MS) bands to produce a high-resolution multispectral image
- **Training data challenge**: Ground truth pansharpened images do not exist; training uses Wald's protocol (downgrading resolution by 4x to create input-output pairs)

**DL Methods for Pansharpening:**
- **PNN** (Masi et al., 2016): First CNN-based method; three convolutional layers with ReLU; simple but effective
- **DRPNN** (Wei et al., 2017): Deeper residual architecture; significant quality improvement
- **PanNet** (Yang et al., 2017): Works on image residuals (high-pass components), preserving spectral and spatial information
- **PNN+** (Scarpa et al., 2018): Residual network extending PNN; best overall performance across most quality indices
- **Architecture choices**: Residual connections are critical; some models use 3 layers (PNN), others use dozens (DRPNN)
- **Loss functions**: L2 (MSE) is standard but produces smooth results; L1 gives sharper output; ERGAS relates to RMSE

**Experimental Results (WorldView-2):**
- PNN+ achieves best performance on most reference metrics (Q8=0.923, Q=0.933, PSNR=31.598)
- DL methods far superior to non-DL methods (BDSD, MTF-GLP, SIRF)
- DL methods have similar or faster running times (~0.1 sec) compared to classical methods

### Multiband Image Fusion (Hyperspectral + Multispectral)
- **Goal**: Produce high-resolution hyperspectral (HR-HS) image from low-resolution HS and high-resolution MS inputs

**Supervised Approaches:**
- **SSF-CNN** (Han et al., 2018): Learns nonlinear mapping from concatenated LR-HS + MS to HR-HS
- **3D-CNN** (Palsson et al., 2017): Uses 3D convolutions on spatially decimated data
- **MHF-net** (Xie et al., 2019): Formulates fusion from observation models (Y=XR+N, Z=CX+N); deep network solves the optimization problem; interpretable architecture

**Unsupervised Approaches:**
- **uSDN** (Qu et al., 2018): Two coupled encoder-decoders with shared decoder; no training data needed
- **Fu et al. (2019)**: Learns spectral response function alongside fusion

**Experimental Results (Chikusei, CAVE datasets):**
- MHF-net achieves best results: PSNR=39.52, RMSE=4.09 (Chikusei); PSNR=39.22, RMSE=3.34 (CAVE)
- MHF-net is 273x faster than uSDN at test time (1 sec vs. 273 sec)
- Supervised DL methods outperform both unsupervised DL and traditional matrix/tensor factorization methods

## Practical Takeaways for Scientists

1. **PNN+ is the recommended pansharpening method** -- best quality with reasonable computation.
2. **Residual learning is essential** for both pansharpening and multiband fusion -- predicting the difference (residual) rather than the full image dramatically improves results.
3. **MHF-net** is recommended for HS-MS fusion -- it incorporates physical observation models into the network architecture, making it both accurate and interpretable.
4. **Training data must be synthesized** via resolution downgrading (Wald's protocol) since ground truth fused images do not exist.
5. **Scale invariance is not guaranteed**: Models trained at reduced resolution may not perfectly generalize to full resolution.
6. **Unsupervised methods** are promising for generalization across sensor combinations but currently lag behind supervised approaches.

## Notable References

- Masi et al. (2016) -- PNN (first DL pansharpening)
- Scarpa et al. (2018) -- PNN+ (best performer)
- Yang et al. (2017) -- PanNet (residual-based)
- Xie et al. (2019) -- MHF-net (observation model-based HS-MS fusion)
- Qu et al. (2018) -- uSDN (unsupervised fusion)
- Vivone et al. (2015) -- Pre-DL pansharpening survey
