import cv2
import numpy as np
import matplotlib.pyplot as plt

#common dimensions to set all images to
dimension = [193,300]

Image1 = cv2.resize(cv2.imread("Processing Images/Image 1.png"), dimension)
Image2 = cv2.resize(cv2.imread("Processing Images/Image 2.png"), dimension)
Image3 = cv2.resize(cv2.imread("Processing Images/Image 3.png"), dimension)
Image4 = cv2.resize(cv2.imread("Processing Images/Image 4.png"), dimension)
Image5 = cv2.resize(cv2.imread("Processing Images/Image 5.png"), dimension)


imagelist = [Image1, Image2, Image3, Image4, Image5]

#creating empty array for the summed image
summed_image = np.zeros_like(Image1, dtype = np.float64)

#summing all images
for image in imagelist:
    summed_image += image.astype(np.float64)

#dividing the resulting image by the amount of images given
summed_image /= len(imagelist)

#setting image pixel bounds to observable range to prevent overflow
summed_image = np.clip(summed_image, 0, 255).astype(np.uint8)

#plotting
def plot(image, title, num):

    plt.subplot(1, 6, num)
    plt.imshow(image, cmap = 'gray')
    plt.axis('off')
    plt.title(title)

plt.figure(figsize = (14, 3))

plot(Image1, 'Image 1', 1)
plot(Image2, 'Image 2', 2)
plot(Image3, 'Image 3', 3)
plot(Image4, 'Image 4', 4)
plot(Image5, 'Image 5', 5)
plot(summed_image, 'Double Exposure Image', 6)


plt.tight_layout()
plt.show()






