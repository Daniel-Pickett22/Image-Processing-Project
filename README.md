# Image-Processing-Project
## Project Overview
This project focuses on various image processing techniques using Python and libraries such as OpenCV and NumPy. The goal is to explore and demonstrate fundamental image manipulation methods, including Fourier transforms, high-pass filtering, feature swapping, median filtering, and image averaging. Each technique is implemented in separate scripts, showcasing different aspects of image processing and enhancing the understanding of how these methods can be applied to real-world scenarios. All five programs can be run with no modifications after installing the libraries in the requirements.txt file. 

Contains 5 separate programs as well as labelled images that can be used to run them. 1. High Pass Filter, 2. Median Filter, 3. Facial Expression Mask, 4. Double Exposure, 5. Image Phase Visualization. 

## High Pass Filter
High-pass filtering is a signal processing technique used to allow high-frequency components of a signal to pass through while attenuating (reducing) the lower-frequency components. In the context of image processing, high-pass filters are primarily used to enhance the edges and fine details of images. 

This program implements high-pass filtering on an image using two different filter kernels (5x5 and 7x7) to enhance edges and details. 

### Features
- Reads an input image and converts it to grayscale.
- Applies high-pass filters with different kernel sizes (5x5 and 7x7).
- Displays the original image alongside the filtered results.

### Image Requirements
- No requirements. It is best to use an image with well-defined, sharp edges, similar to the image provided.

### Outputs
![image](https://github.com/user-attachments/assets/f070d99e-318d-425f-8a48-faa28b4f1d45)

## Median Filter
Median filtering is a nonlinear image processing technique used primarily for noise reduction while preserving edges in an image. 

This program applies median filtering to a grayscale image to reduce noise while preserving edges. The median filter is particularly effective for removing salt-and-pepper noise from images, making it a valuable preprocessing step in image processing tasks.

### Features
- Reads an input image and converts it to grayscale.
- Uses various window sizes to demonstrate various levels of smoothing.
- Displays the original image alongside the filtered results.

### Image Requirements
- No requirements. It is best to use a color image that has some degree of noise in it, as opposed to an already clean image.

### Outputs
![image](https://github.com/user-attachments/assets/6d01091a-ff8e-43fe-9d93-4177e22b0bd6)

## Facial Expression Mask
Facial masks refer to regions of interest (ROIs) on the images that represent specific facial landmarks—such as the eyes and mouth. These masks are defined by pixel coordinates, which can be removed and applied to other faces to manipulate facial features.

This program demonstrates facial feature swapping between images of a man with various facial features. The code resizes and aligns five input images to a specified dimension, then swaps the eyes and mouth between different images to create various facial expressions. 

### Features
- Resizes and aligns multiple input images to a uniform dimension for consistent feature swapping. 
- Swaps specific facial features (eyes and mouth) between multiple images using predefined regions of interest (ROIs).
- Displays the original images alongside the modified ones.

### Image Requirements
- The program only works with the images provided.
- The program can be easily modified to feature swap any combination of input images.

### Inputs
<img width="944" alt="image" src="https://github.com/user-attachments/assets/473dd1ef-bed4-462a-8cac-ef8dfeca0dbe">

### Outputs
<img width="861" alt="image" src="https://github.com/user-attachments/assets/5f3253ce-cdb3-4081-8596-cc76e7c307f6">

## Double Exposure
Double exposure is a photographic technique that combines two different images into a single frame, creating a surreal or artistic effect. This is achieved by layering one image over another, often resulting in a blend of textures, shapes, and colors.

This program creates a double exposure effect by averaging multiple images into a single composite image. The program resizes five input images to a common dimension, sums their pixel values, and produces an output that visually blends the features of all input images.

### Features
- Resizes multiple input images to a uniform dimension for consistent blending.
- Computes the average of pixel values across multiple images to create a smooth composite.
- Displays the original images alongside the modified one.

### Image Requirements
- Any images can be used for this program, though it is recommended to use images with complementary shapes and colors so that they may blend more harmoniously. 

### Inputs
<img width="723" alt="image" src="https://github.com/user-attachments/assets/6918f13f-8f80-43aa-a0f9-c12e7c785ccc">

### Output
<img width="155" alt="image" src="https://github.com/user-attachments/assets/069f78a6-8c8b-4341-8f02-1e23e0ccd221">

## Image Phase Visualization

An image exists in the spatial domain, where the value of each pixel corresponds to the intensity at a specific position in the image. Applying the Fourier transform to the image will convert the spatial domain into the frequency domain, revealing the image's spatial frequency components. Each frequency represents how sudden the pixel intensities change across the image, and each frequency point is represented as a complex number. The complex number encodes two pieces of information: the phase and magnitude. 

This program isolates the phase information of every spatial frequency of the image, and visualizes the variation of waveform phases across the image. The u and v values represent spatial frequency coordinates. The phase images generated by this program correspond to how each frequency component contributes to the overall structure of the image. 

### Features
- Reads an input image and converts it to grayscale.
- Computes the Fourier transform of the image.
- Generates phase images based on different frequency combinations of u and v.

### Image Requirements
- Any image can be used for this program. ***However***, larger images can be computationally intensive and may significantly increase processing time, while the smaller image currently used is expected to take 1-3 minutes to compute, depending on the machine being used.

### Input
![Fourier_Image](https://github.com/user-attachments/assets/3b4c07da-dbbc-4b33-a9df-52f9ab7b347b)

### Outputs
![image](https://github.com/user-attachments/assets/ff10ad4b-5496-4fc8-bda7-d6adb306a974)
