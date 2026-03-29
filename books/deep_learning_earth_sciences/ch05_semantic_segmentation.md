# Chapter 5: Deep Learning-based Semantic Segmentation in Remote Sensing

**Authors:** Devis Tuia, Diego Marcos, Konrad Schindler, and Bertrand Le Saux

## Summary

This chapter provides a thorough review of deep learning approaches for semantic segmentation (pixel-wise classification) in remote sensing. It covers the evolution from computer vision architectures to RS-specific adaptations, including handling of rotation invariance, 3D point clouds, and multi-temporal data. Three detailed case studies demonstrate key innovations: rotation-equivariant networks (RotEqNet), 3D point cloud segmentation (SnapNet), and lake ice detection from SAR/webcam imagery.

The central argument is that while off-the-shelf computer vision models are a good starting point, significant gains come from tailoring architectures to the unique characteristics of Earth observation data: rotation invariance in overhead imagery, multi-modal inputs (optical, SAR, LiDAR), temporal consistency, and 3D point cloud structure.

## Key Concepts and Methods

### Semantic Segmentation Architectures for Images

**Hard-coded upsampling approaches:**
- **FCN (Fully Convolutional Networks)**: Replaces fully connected layers with 1x1 convolutions; upsamples coarse maps
- **Hypercolumns**: Feature maps from different scales are upsampled and stacked
- **PSPNet**: Applies average pooling at different bin sizes to increase receptive field

**Learned upsampling (encoder-decoder) approaches:**
- **SegNet**: Transfers pooling indices from encoder to decoder for upsampling
- **U-Net**: Appends entire feature maps from encoder to decoder via skip connections
- Dilated (a-trous) convolutions increase receptive field without losing resolution
- **DeepLab**: Uses dilated convolutions + Conditional Random Fields post-processing

**Loss functions:**
- Cross-entropy loss (most common), often with class re-weighting for imbalanced datasets
- Distance-based losses (to nearest semantic boundary)
- Geometry-aware losses for segmented objects

### Architectures for Point Clouds
- **Graph-based**: SuperPointGraph builds graphs over superpoints for contextual segmentation
- **3D-based**: VoxNet uses 3D convolutions; OctNet uses octrees for adaptive resolution
- **2D projection**: MultiViewCNN, SnapNet project 3D to 2D views
- **Point-based**: PointNet/PointNet++ apply MLPs directly on point sets; PointCNN uses chi-convolutions

### Case Study 1: RotEqNet -- Rotation Equivariance
- Overhead imagery has no preferred orientation; rotation is arbitrary
- RotConv applies filters at R discrete orientations, returns both magnitude and orientation
- On ISPRS Vaihingen benchmark: RotEqNet with 10^5 parameters matches standard CNN with 10^6 parameters
- Especially beneficial for geometric classes (cars, buildings) vs. texture classes (vegetation)

### Case Study 2: SnapNet -- 3D Point Cloud Segmentation
- Generates thousands of 2D views from a point cloud at multiple scales
- Applies standard 2D semantic segmentation (SegNet, U-Net) on generated views
- Back-projects 2D labels to 3D via mesh-face voting
- Leverages pretrained 2D models and handles appearance + geometric features

### Case Study 3: Lake Ice Detection
- Essential climate variable (ECV) requiring high temporal resolution
- Two data sources: Sentinel-1 SAR (cloud-independent, 2-day revisit) and webcams
- DeepLab v3+ with mobilenetv2 (SAR) and Xception65 (webcams)
- SAR models achieve ~90% mIoU across winters; webcams achieve 78-96% depending on train/test setup
- Pretrained models (PASCAL VOC) improve performance even for SAR amplitude images

## Practical Takeaways for Scientists

1. **Use encoder-decoder architectures** (U-Net, DeepLab) rather than patch-based classification for efficiency and spatial coherence.
2. **Rotation-equivariant networks** can match larger models with 10x fewer parameters -- valuable for overhead RS imagery.
3. **Pretraining on natural images helps** even for SAR data, suggesting that low-level features transfer across very different sensing modalities.
4. **Point cloud segmentation** can leverage mature 2D CNN technology via multi-view projection (SnapNet approach).
5. **Key datasets**: ISPRS Vaihingen/Potsdam, IEEE GRSS Data Fusion Contest, DeepGlobe, SpaceNet, So2Sat LCZ42, DOTA, Sen1Floods11.
6. **Class imbalance** is pervasive in RS segmentation -- use weighted loss functions or specialized sampling strategies.

## Notable References

- Long et al. (2015) -- Fully Convolutional Networks (FCN)
- Ronneberger et al. (2015a) -- U-Net
- Chen et al. (2017a) -- DeepLab with dilated convolutions
- Marcos et al. (2018a) -- RotEqNet for rotation equivariance
- Boulch et al. (2018) -- SnapNet for point cloud segmentation
- Tom et al. (2020) -- Lake ice detection with Sentinel-1
- Qi et al. (2017b) -- PointNet for point cloud processing
