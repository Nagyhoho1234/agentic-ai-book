# Chapter 4: Deep Self-taught Learning in Remote Sensing

**Author:** Ribana Roscher

## Summary

This chapter introduces Deep Self-Taught Learning (DSTL), a framework that combines the advantages of self-taught learning (STL) with deep learning to create interpretable and explainable feature representations for remote sensing classification. Unlike semi-supervised learning, STL can exploit unlabeled data that does not need to belong to the same classes or follow the same distribution as the labeled data. The DSTL framework stacks multiple layers of sparse representations built from interpretable dictionaries, maintaining explainability while achieving deep feature extraction.

The key advantage of DSTL over standard deep learning is interpretability: since dictionaries can be restricted to actual data samples, the learned representations can be directly related to real-world observations and explained in the context of a specific application.

## Key Concepts and Methods

### Self-Taught Learning (STL) Basics
- Originally proposed by Raina et al. (2007)
- Uses unlabeled data from arbitrary classes (not necessarily the same as labeled data)
- More flexible than semi-supervised learning (which requires same-distribution unlabeled data)
- Core procedure: sparse representation (SR) learns features unsupervised; features fed to supervised classifier

### Sparse Representation
- Each sample x represented as weighted linear combination of dictionary elements: x = D*alpha + epsilon
- Optimization: minimize ||D*alpha - x||_2 subject to sparsity constraint ||alpha||_f < rho
- L0-norm gives exact sparsity (number of non-zero elements); L1-norm is a convex relaxation
- Non-negativity constraints and sum-to-one constraints enhance interpretability (useful for unmixing)

### Dictionary Learning
- K-SVD and variants: alternating sparse coding + dictionary update (high approximation, but not interpretable)
- Interpretable alternatives: cluster centers, extremal points (archetypes), autoencoders
- Class-wise dictionaries: structured by class assignment, can enforce class-specific reconstruction

### Deep Self-Taught Learning (DSTL) Framework
- Stacks L layers of sparse representations: X = D^(1)*A^(1) + E^(1), A^(1) = D^(2)*A^(2) + E^(2), etc.
- Layer-wise initialization using dictionary element extraction from unlabeled data
- Four-step iterative update procedure:
  1. Compute classifier loss at last layer, update representations
  2. Propagate updates to lower layers
  3. Update dictionaries using gradient descent
  4. Readjust representations with updated dictionaries
- Final classification via logistic regression on last-layer representations

### Application Example
- UC Merced dataset: 21 land use classes, 3 used as labeled (agriculture, forest, buildings), rest as unlabeled
- 32x32 RGB images, 3072-dimensional input vectors
- DSTL with 2 layers: 10 archetypes in layer 1, 16 in layer 2
- Results: DSTL+LR achieved 92% overall accuracy vs. 86.7% for STL+LR vs. 66% for original features+LR
- Interpretable version: ~2% accuracy drop when restricting dictionary elements to nearest real data samples

## Practical Takeaways for Scientists

1. **Use DSTL when interpretability matters**: Unlike black-box deep learning, DSTL dictionary elements can be actual data samples, making the model explainable.
2. **Unlabeled data from different domains helps**: STL does not require unlabeled data to come from the same classes as labeled data -- any relevant RS imagery can be used.
3. **Few labeled samples suffice**: The framework is designed for scenarios with limited labeled data but abundant unlabeled data (typical in RS).
4. **Accuracy-interpretability tradeoff**: Restricting dictionaries to real data samples costs only ~2% accuracy.
5. **Parallels with CNNs**: DSTL dictionary elements are analogous to CNN convolutional filters; both can be extended with pooling and other operations.

## Notable References

- Raina et al. (2007) -- Original self-taught learning
- Gwon et al. (2016) -- Backpropagation applied to DSTL
- Bettge et al. (2017) -- Interpretable representations related to real data samples
- Roscher et al. (2020); Reichstein et al. (2019) -- Interpretability in remote sensing
- Bristow et al. (2013) -- Convolutional sparse coding (close relation to DSTL)
