# Chapter 13: Spatio-temporal Autoencoders in Weather and Climate Research

**Authors:** Xavier-Andoni Tibau, Christian Reimers, Christian Requena-Mesa, and Jakob Runge

## Summary

This chapter presents autoencoders (AEs) as a powerful tool for weather and climate science, covering their theoretical foundations, variants, and diverse applications. AEs are particularly well-suited to climate data because they are unsupervised (no labels needed), can handle high-dimensional spatio-temporal fields, and can capture nonlinear relationships that PCA/EOF analysis cannot. The chapter surveys five AE archetypes (GAE, RAE, SAE, DAE, CAE) and VAEs, then demonstrates applications in two categories: using the latent space (dimensionality reduction, feature extraction, prediction) and using the decoder (sample generation, denoising, anomaly detection).

## Key Concepts and Methods

### Autoencoder Fundamentals
- Encoder phi maps input X to latent space H; decoder varphi maps H back to reconstructed X'
- Training minimizes reconstruction loss (typically MSE)
- Linear AEs converge to PCA projection; nonlinear AEs approximate kernel-PCA
- Key advantage over PCA: can capture nonlinear dependencies in weather data

### AE Variants (Table 13.1)
| Variant | Additional Loss | Goal |
|---------|----------------|------|
| **GAE** (Generalized) | Loss on similar inputs | Reproduce input AND similar inputs |
| **RAE** (Relational) | Loss on inter-sample relations | Preserve relationships between samples |
| **SAE** (Sparse) | KL-divergence sparsity penalty | Sparse activations; bottleneck can be larger than input |
| **DAE** (Denoising) | Input is corrupted version | Learn to denoise; captures data manifold |
| **CAE** (Contractive) | Frobenius norm of Jacobian | Robust to small input perturbations |

### Variational Autoencoders (VAE)
- Maps inputs to a probability distribution (not a point) in latent space
- Optimizes Evidence Lower Bound (ELBO): reconstruction + KL divergence to standard normal
- Reparameterization trick: h = sigma * h_tilde + mu (enables backpropagation through sampling)
- Enables generation of new samples from the learned distribution

### Applications: Using the Latent Space

**Understanding system dynamics:**
- SupernoVAE (Tibau et al., 2018): VAE as unsupervised kernel-PCA approximation; captures hidden driving patterns in Lorenz '96 and cellular automata that PCA and kernel-PCA fail to recover (R2=0.756 vs ~10^-5 for other methods)
- Koopman-based AE (Lusch et al., 2018): Projects nonlinear dynamics into a space where Koopman operator K linearizes them; demonstrated on pendulum, continuous spectrum, and fluid flow problems

**Feature extraction and prediction:**
- Wind vector determination from SAE features (McAllister and Sheppard, 2017)
- Rainfall prediction from AE-extracted features
- Nuclear plume dispersion classification from multiple AE architectures
- Polar vortex clustering with sparse VAE (Krinitskiy et al., 2019)

### Applications: Using the Decoder

**Sample generation:**
- VAEs can emulate expensive GCM ensemble runs by sampling from learned latent distribution
- Spatio-temporal decoders (recurrent) can generate novel temporal sequences

**Denoising:**
- DAE corrects weather forecast errors by treating forecasts as "noisy" versions of truth
- Chapman et al. (2019): State-of-the-art atmospheric river forecasting via DAE

**Anomaly detection:**
- Reconstruction error as anomaly score: samples far from training distribution produce large errors
- Largely unexplored in climate science but well-established in other fields

## Practical Takeaways for Scientists

1. **AEs are the natural choice** when labeled data is unavailable -- most climate datasets lack labels.
2. **VAEs outperform PCA/EOF** for capturing nonlinear drivers of climate dynamics.
3. **SupernoVAE** (code: github.com/ClimateInformatics/SupernoVAE) discovers hidden forcing patterns that linear methods miss entirely.
4. **DAEs for forecast correction** are a practical near-term application -- treat forecast errors as "noise" and train the DAE to remove them.
5. **Benchmark datasets** for climate AE applications are needed -- the community lacks standardized comparisons.
6. **Physical knowledge integration** into AE architectures remains the key frontier for community acceptance.

## Notable References

- Tibau et al. (2018) -- SupernoVAE for climate dynamics
- Lusch et al. (2018) -- Koopman-based autoencoders for dynamical systems
- Kingma and Welling (2013) -- Variational Autoencoders
- Chapman et al. (2019) -- DAE for atmospheric river forecasting
- Vincent et al. (2010) -- Denoising Autoencoders
- Krinitskiy et al. (2019) -- Sparse VAE for polar vortex clustering
