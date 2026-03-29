# Chapter 6: Object Detection in Remote Sensing

**Authors:** Jian Ding, Jinwang Wang, Wen Yang, and Gui-Song Xia

## Summary

This chapter provides a comprehensive treatment of object detection in remote sensing images, covering both optical and SAR imagery. Unlike natural image object detection, RS object detection faces unique challenges: arbitrary object orientation, huge scale variations (10 to 1000+ pixels), very large images (20,000+ pixels), and densely packed instances. The chapter reviews the evolution from two-stage (R-CNN family) to one-stage (YOLO, SSD) detectors, discusses RS-specific adaptations including oriented bounding box (OBB) representations, and presents two novel methods: Mask OBB for resolving OBB representation ambiguity, and RoI Transformer for efficient oriented object detection.

## Key Concepts and Methods

### RS-Specific Object Detection Challenges
- **Arbitrary orientation**: Objects viewed from above have no preferred direction, requiring rotation-invariant features
- **Huge scale variations**: Objects range from 10 pixels (vehicles) to 1000+ pixels (fields) in the same scene
- **Large images**: RS images can exceed 20,000 pixels, requiring tiling/cropping strategies
- **Dense packing**: Harbors, parking lots contain hundreds of tightly packed objects

### Object Representation
- **HBB (Horizontal Bounding Box)**: Standard (cx, cy, w, h) -- simple but cannot capture orientation
- **OBB (Oriented Bounding Box)**: (cx, cy, w, h, theta) -- captures orientation but suffers from representation ambiguity at angle discontinuity points
- **Mask OBB**: Binary segmentation mask representation that avoids all discontinuity/ambiguity problems

### Two-Stage Detectors
- **R-CNN**: Selective search for proposals, CNN feature extraction, SVM classification
- **Fast R-CNN**: Shares computation via RoI pooling, 213x faster than R-CNN
- **Faster R-CNN**: Learns proposals via Region Proposal Network (RPN), end-to-end trainable
- **R-FCN**: Position-sensitive cropping reduces per-proposal computation

### One-Stage Detectors
- **YOLO**: Divides image into SxS grid, predicts B boxes per cell, single forward pass
- **SSD**: Multi-scale anchor boxes on different feature maps, multitask loss

### RS-Specific Innovations

**For scale variance:**
- Feature Pyramid Network (FPN): Top-down pathway fuses multi-scale features
- Image Cascade Network (ICN): Joint image cascade + feature pyramid

**For orientation variance:**
- Spatial Transformer Networks (STN), Deformable Convolutions (DCN)
- Rotation-Invariant CNN (RICNN): rotation-invariant layer plugged into R-CNN
- Rotated RoI Pooling and Rotated Region Proposal Network (RRPN)

**For oriented object detection (regression-based):**
- DRBox, FR-O, ICN, SCRDet: Regress OBB offsets from HBBs
- Mask OBB (segmentation-based): Represents OBBs as binary masks, no discontinuity points, gap between HBB and OBB mAP reduced to 0.17% (vs. 1.16-3.10% for regression methods)

**RoI Transformer:**
- Lightweight module that efficiently generates rotated proposals from horizontal RoIs
- RRoI Learner infers rotated RoIs from horizontal features
- RRoI Warping extracts rotation-invariant features
- Achieves 69.56 mAP on DOTA (best among compared methods)

### Key Datasets
- **DOTA**: 2806 aerial images, 188,282 instances in 15 categories, oriented bounding boxes
- **VisDrone**: 263 drone videos + 10,209 images, 2.5M annotations, 10 categories
- **DIOR**: 23,463 images, 192,472 instances, 20 categories (Google Earth)
- **xView**: WorldView-3, 0.3m GSD, 60 classes, 1M+ objects over 1400 km2
- **SAR datasets**: SAR-Ship-Dataset, SSDD, SpaceNet 6, AIR-SARShip-1.0

### SAR Object Detection
- Fundamentally different from optical: speckle noise, different scattering mechanisms
- Traditional: CFAR (Constant False Alarm Rate) detection
- DL approaches: CNN-based ship detectors, often requiring learning from scratch due to domain gap with ImageNet

## Practical Takeaways for Scientists

1. **Use oriented bounding boxes** for RS object detection -- HBBs lose critical orientation information.
2. **Mask OBB representation** eliminates angle discontinuity problems that plague regression-based OBB methods.
3. **Feature Pyramid Networks** are essential for handling the extreme scale variations in RS imagery.
4. **Tile large images** with overlap (e.g., 1024x1024 patches with 500-pixel overlap) for processing.
5. **SAR object detection** requires different approaches; pretrained ImageNet models may introduce domain bias.
6. **DOTA** is the most important benchmark for oriented object detection in aerial images.

## Notable References

- Xia et al. (2018) -- DOTA dataset
- Ding et al. (2019) -- RoI Transformer
- Wang et al. (2019b) -- Mask OBB
- Ren et al. (2017) -- Faster R-CNN
- Lin et al. (2017) -- Feature Pyramid Network
- Redmon et al. (2016) -- YOLO
