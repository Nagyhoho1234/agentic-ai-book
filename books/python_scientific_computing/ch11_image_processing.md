# Chapter 11: Image Processing

## Summary

This chapter covers image processing using OpenCV, scikit-image, and Pillow libraries. It demonstrates how to manipulate, analyze, and extract information from digital images, with practical applications in medical imaging (brain tumor analysis, retinal image segmentation), microbiology (microbe counting), and general image analysis (edge detection, color manipulation, statistical analysis).

## Key Concepts

### Image Fundamentals
- Digital images as 2D/3D NumPy arrays (height x width x channels)
- **RGB color model**: Red, Green, Blue channels each with values 0-255
- **Grayscale** conversion: weighted average of RGB channels
- Image resolution, pixel coordinates, and array indexing

### OpenCV (cv2)
- **Reading/writing images**: `cv2.imread()`, `cv2.imwrite()`
- **Color space conversion**: `cv2.cvtColor()` for BGR to RGB, grayscale, HSV
- **Thresholding**: binary segmentation using pixel intensity cutoffs
- **Edge detection**: Canny edge detector for finding boundaries
- **Contour detection**: finding and drawing object boundaries

### Scikit-Image
- **Filters**: Gaussian blur, median filter, Sobel edge detection
- **Segmentation**: SLIC superpixels, watershed, Otsu thresholding
- **Morphological operations**: erosion, dilation, opening, closing
- **Region properties**: measuring area, perimeter, centroid of detected objects
- **Skeletonization**: reducing shapes to their topological skeleton

### Medical Image Analysis
- **Brain tumor detection**: segmenting tumors from MRI scans
  - Converting to grayscale, thresholding, measuring tumor area as percentage of total brain area
  - Result: approximately 11.27% tumor area in example
- **Retina image analysis**: detecting blood vessels and abnormalities
  - Masking and segmentation techniques
- **Statistical analysis of images**: histograms of pixel intensities, mean, variance

### Microbiology Applications
- **Microbe counting**: automated counting of bacteria/cells in microscope images
- **Color-based segmentation**: identifying objects by color (e.g., yellow pixels for specific microbes)
- Centroid marking for counted objects

### Image Manipulation
- **Peppers test image**: standard image processing benchmark
- Color channel separation and recombination
- Image arithmetic: addition, subtraction, blending
- Histogram equalization for contrast enhancement

## Code Examples Described
- Loading, displaying, and saving images in multiple formats
- Edge detection using Canny algorithm on test images
- Brain tumor segmentation from MRI with area percentage calculation
- Microbe counting with centroid marking
- Color image analysis and statistical characterization
- SLIC superpixel segmentation demonstration
- Retina image vessel detection

## Key Definitions
- **Pixel**: smallest addressable element of a digital image
- **Segmentation**: dividing an image into meaningful regions
- **Thresholding**: converting a grayscale image to binary based on an intensity cutoff
- **Edge detection**: identifying boundaries where image intensity changes sharply
- **SLIC (Simple Linear Iterative Clustering)**: algorithm for generating superpixels

## Practical Takeaways
- OpenCV is the most comprehensive image processing library; scikit-image is more Pythonic and integrates better with scikit-learn
- Medical image analysis can be automated with relatively simple thresholding and morphological operations
- Color-based segmentation is effective when objects have distinct colors from the background
- Always convert between color spaces (BGR/RGB) when moving between OpenCV and matplotlib
- Image processing pipelines typically follow: load -> preprocess -> segment -> measure -> report

## Notable References
- Howse, J. et al. (2016). *OpenCV 4 for Secret Agents*, Packt Publishing
- Van der Walt, S. et al. (2014). scikit-image: image processing in Python. *PeerJ*, 2, e453
- Solomon, C. and Breckon, T. (2011). *Fundamentals of Digital Image Processing*, Wiley
