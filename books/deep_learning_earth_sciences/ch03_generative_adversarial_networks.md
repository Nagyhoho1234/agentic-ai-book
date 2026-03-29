# Chapter 3: Generative Adversarial Networks in the Geosciences

**Authors:** Gonzalo Mateo-Garcia, Valero Laparra, Christian Requena-Mesa, and Luis Gomez-Chova

## Summary

This chapter provides a comprehensive review of Generative Adversarial Networks (GANs) and their applications in Earth observation and geosciences. The authors describe the three main GAN families -- unsupervised GANs, conditional GANs (CGANs), and cycle-consistent GANs (CycleGANs) -- with their mathematical formulations, and then survey their wide-ranging applications in remote sensing. Two detailed case studies are presented: domain adaptation across different satellites (Landsat-8 to Proba-V) and landscape emulation from climatic/geological/anthropogenic variables.

The key message is that GANs offer a fundamentally new approach to Earth system modeling: instead of building physics-based simulators, generative models can learn complex spatio-temporal dynamics directly from observational data, enabling both data augmentation and Earth system emulation.

## Key Concepts and Methods

### Three GAN Families

1. **Unsupervised GANs**: Generator G converts random vector r into synthetic sample; Discriminator D distinguishes real from fake. The adversarial training uses a novel non-parametric adaptive cost function that learns the likelihood function during training.

2. **Conditional GANs (CGANs)**: Input to generator is random vector r PLUS feature vector y (auxiliary information). Discriminator evaluates joint distribution of X and Y. Requires paired training samples. Avoids mode collapse by forcing consistency with auxiliary input.

3. **Cycle-consistent GANs (CycleGANs)**: Two coupled conditional GANs for unpaired image-to-image translation. Cost function has three parts: two GAN losses + cycle consistency loss ensuring a sample passed through both generators returns to itself. Does NOT require paired training data.

### GANs in Earth Observation Applications
- **Data generation**: Synthesizing EO images, improving SAR simulators
- **Domain adaptation**: Adapting between satellite sensors, finding invariant features across SAR/optical
- **Feature extraction**: Unsupervised/semi-supervised spatial-spectral feature learning
- **Change detection**: Modeling bitemporal image relationships, seasonal invariant terms
- **Super-resolution**: Higher perceptual quality than MSE-based methods; edge-enhancement, multiband approaches
- **Cloud removal**: CycleGANs learning mapping between cloudy and cloud-free images
- **Inpainting**: Filling voids in radar data, removing cloud occlusions from SST records

### Case Study 1: Domain Adaptation Across Satellites
- Landsat-8 to Proba-V adaptation using modified CGAN
- Physical transformation first (point spread function, spectral response matching)
- Then CGAN removes remaining statistical differences
- Result: Cloud detection models trained on Landsat-8 work better on GAN-denoised Proba-V than raw Proba-V

### Case Study 2: Landscape Emulation
- Conditional GAN predicts landscapes as seen from space given climatic, geological, and anthropogenic variables
- Convolutional encoder-decoder with skip connections and probabilistic latent space
- Model generates multiple plausible landscapes for each set of environmental conditions
- Demonstrates that convolutions + adversarial training are key to realistic landscape prediction

## Practical Takeaways for Scientists

1. **CycleGANs are most practical** when paired training data is unavailable (common in multi-sensor scenarios).
2. **Domain adaptation with GANs** enables reusing models trained on one satellite for another, saving the cost of relabeling.
3. **GANs for super-resolution** produce visually sharper results than MSE-based methods, which tend to generate blurry outputs.
4. **Earth system emulation** with conditional GANs can replace expensive numerical simulators and provide uncertainty estimates through multiple samples.
5. **Physical preprocessing** (sensor response matching) before GAN-based domain adaptation improves results.

## Notable References

- Goodfellow et al. (2014b) -- Original GAN paper
- Mirza and Osindero (2014) -- Conditional GANs
- Zhu et al. (2017); Kim et al. (2017b) -- CycleGANs
- Mateo-Garcia et al. (2019) -- Landsat-8 to Proba-V domain adaptation
- Requena-Mesa et al. (2019) -- Landscape prediction with conditional GANs
- Hoffman et al. (2018) -- Comprehensive reference on CGANs/CycleGANs for domain adaptation
