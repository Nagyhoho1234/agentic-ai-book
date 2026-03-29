# Chapter 9: Deep Learning for Image Matching and Co-registration

**Authors:** Maria Vakalopoulou, Stergios Christodoulidis, Mihir Sahasrabudhe, and Nikos Paragios

## Summary

This chapter reviews deep learning methods for image matching (measuring similarity between image pairs) and image registration (aligning images via geometric transformation). These are fundamental tasks in Earth observation for change detection, multi-temporal analysis, image fusion, and 3D reconstruction. The chapter presents a novel unsupervised deep learning framework that jointly estimates affine and deformable transformations using a 2D spatial transformer, achieving sub-pixel accuracy 100x faster than classical methods.

## Key Concepts and Methods

### Challenges in EO Image Matching/Registration
1. **Radiation distortions**: Sensor properties and atmospheric effects alter pixel intensities
2. **Geometric distortions**: Different viewpoints, sensor heights, terrain relief
3. **Changed areas**: Temporal changes between acquisitions violate the assumption of identical content
4. **Multimodal data**: SAR-to-optical, multispectral-to-hyperspectral matching across very different imaging modalities

### Classical Approaches
- **Feature-based**: SIFT, SURF, DAISY, BRIEF, HOSS descriptors + similarity functions (mutual information, cross-correlation, RANSAC)
- **Rigid registration**: Affine/homography transformations (6-8 degrees of freedom)
- **Deformable registration**: Dense transformation grids for local variations (needed for high-resolution imagery)
- Classical methods: Repeatability rates below 50% for multi-sensor pairs

### Deep Learning for Image Matching
- **Siamese networks**: Most popular architecture; extract CNN features from patches, compute similarity scores
- **Optical-to-optical**: Attention-based architectures, densely-connected CNNs, deep hashing networks
- **SAR-to-SAR**: Siamese architectures adapted for SAR imagery
- **SAR-to-optical**: Cross-modal matching using GANs to generate SAR-like patches from optical, or direct Siamese matching
- **Other modalities**: Satellite imagery to maps (e.g., Tencent Maps), multimodal data fusion

### Deep Learning for Image Registration
- **Spatial Transformer Networks** (Jaderberg et al., 2015): Trainable module that transforms intermediate feature maps to eliminate intra-object variance
- Few RS-specific deep registration methods; most use matching results to compute transformation parameters separately

### Proposed Framework: Unsupervised Deep Registration
- **Key innovation**: Completely unsupervised -- no registered image pairs needed for training
- **2D transformer layer**: Regresses spatial gradients to create dense deformation grid G
- **Modular formulation**: Jointly optimizes affine (A) and deformable (Phi) components
- **Architecture-independent**: Works with dilated convolution or maxpooling encoder-decoders
- **Loss function**: MSE between reference R and warped image W(S,G), plus L1 regularization on A and Phi deviations from identity

### Experimental Results
- Dataset: Quickbird/WorldView-2 multitemporal imagery, Attica, Greece (14 km2, 2006-2007)
- Combined affine + deformable (A & Phi): Best performance with ds = 1.9 pixels (dilated) and 2.0 pixels (maxpool)
- Classical rigid methods: ds ~ 4 pixels; classical deformable: ds ~ 2.5 pixels
- **100x speed advantage**: ~0.02 seconds per 256x256 pair vs. 2-3 seconds for classical methods
- Deformable component essential for high-resolution imagery with local geometric variations

## Practical Takeaways for Scientists

1. **Use deformable registration** for high-resolution satellite imagery -- rigid methods cannot capture local geometric distortions from buildings, terrain relief.
2. **Unsupervised deep learning registration** eliminates the need for pre-registered training pairs.
3. **Combine affine + deformable** transformations for best results -- joint training yields easier convergence.
4. **Deep methods are 100x faster** than classical approaches, enabling real-time processing of large RS datasets.
5. **Siamese networks** are the go-to architecture for image matching across modalities.
6. **Code available** at https://github.com/stergioc/smooth-transformer

## Notable References

- Vakalopoulou et al. (2019) -- Deep unsupervised registration framework
- Jaderberg et al. (2015) -- Spatial Transformer Networks
- Merkle et al. (2017, 2018) -- SAR-to-optical matching with Siamese/GAN architectures
- Lowe (1999) -- SIFT descriptor (baseline)
- Shu et al. (2018) -- Spatial gradient integration for deformation fields
