# Chapter 11: Deep Learning for Image Search and Retrieval in Large Remote Sensing Archives

**Authors:** Gencer Sumbul, Jian Kang, and Begum Demir

## Summary

This chapter reviews deep learning-based Content-Based Image Retrieval (CBIR) systems for searching massive remote sensing archives. As satellite data archives grow exponentially, efficient and accurate search becomes essential. The chapter covers two main topics: (1) DL-based CBIR systems that learn discriminative image descriptors, and (2) scalable retrieval via deep hashing methods that encode images into compact binary codes for fast Hamming-distance-based search. RS images present unique challenges for CBIR due to multi-label content, multi-source modalities, and extreme archive sizes.

## Key Concepts and Methods

### CBIR System Components
1. **Image characterization**: Extract descriptors (features) that capture spatial and spectral content
2. **Image retrieval**: Compute similarity between query descriptor and archive descriptors, return k-nearest neighbors

### Traditional CBIR Approaches
- Bag-of-visual-words (SIFT-based), bag-of-morphological-words, Local Binary Patterns (LBPs)
- Graph-based representations (nodes = regions, edges = spatial relations)
- Hashing methods (kernel-based, partial randomness)
- Limitation: Hand-crafted features cannot capture high-level semantic content

### DL-based CBIR Systems

**Network types:**
- Autoencoders (unsupervised, reconstruction-based)
- Convolutional autoencoders (CAE) -- better spatial awareness than vanilla AE
- CNNs (supervised, classification-based) -- most common approach
- Graph convolutional networks (GCNs) -- model region adjacency graphs

**Learning strategies:**
- **Classification (cross-entropy loss)**: Most common; learns class-discriminative features but not optimized for retrieval
- **Metric learning (contrastive loss)**: Siamese networks learn to minimize distance between similar images and maximize distance between dissimilar ones
- **Metric learning (triplet loss)**: Three CNNs with shared weights process anchor, positive, and negative images; learns ranking-appropriate feature spaces
- **Reconstruction (unsupervised)**: No labels needed but limited semantic discriminability

**Key systems:**
- LDCNN (Zhou et al., 2017a): Cross-channel parametric pooling, low-dimensional descriptors
- TDMLN (Cao et al., 2020): Triplet deep metric learning network, state-of-the-art pretrained initialization

### Scalable CBIR via Deep Hashing
- **Problem**: Linear search through millions of images is impractical
- **Solution**: Hash high-dimensional features into compact binary codes; search via Hamming distance (XOR operations)

**Key methods:**
- **DHNN** (Li et al., 2018b): Supervised, contrastive + quantization loss
- **MiLaN** (Roy et al., 2020): Triplet + bit balance + quantization loss
- **DHCNN** (Song et al., 2019): Contrastive + cross-entropy + quantization loss
- **SSHAAE** (Tang et al., 2019): Semi-supervised, adversarial autoencoder with 5-component loss

**Loss function comparison:**
- Contrastive and triplet losses enable similarity learning in feature space
- Bit balance loss ensures uniform distribution of hash codes (50% activation per bit)
- Quantization loss ensures binary approximation quality
- Adversarial loss enables unsupervised hash code generation

## Practical Takeaways for Scientists

1. **Triplet loss produces the most retrieval-specific descriptors** -- better than classification-based approaches for search tasks.
2. **Deep hashing is essential for large archives** -- binary codes reduce storage by orders of magnitude and enable near-instant search via XOR operations.
3. **Multi-label CBIR** is an open challenge -- RS images typically contain multiple land cover classes, but most methods assume single-label annotations.
4. **Multi-source CBIR** (searching across optical, SAR, hyperspectral) remains largely unexplored.
5. **Transfer learning from ImageNet** is the standard initialization strategy for RS CBIR networks.
6. **BigEarth project** (ERC-2017-STG, Grant 759764) is driving significant advances in this area.

## Notable References

- Cao et al. (2020) -- TDMLN (triplet deep metric learning)
- Roy et al. (2020) -- MiLaN (deep hashing with triplet loss)
- Chaudhuri et al. (2019) -- Graph convolutional network for CBIR
- Li et al. (2018b) -- DHNN (deep hashing neural network)
- Demir and Bruzzone (2016) -- Hashing-based RS CBIR
