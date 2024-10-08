import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("Processing Images/High_Pass_Image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#arrays taken from project slides
filter_kernel5x5 = np.array([ 
                              [ 0, -1,  0],
                              [-1,  4, -1],
                              [ 0, -1,  0],
                             ])

filter_kernel7x7 = np.array([ [-1, -1, -1],
                              [-1,  8, -1],
                              [-1, -1, -1],
                              ])

#function to perform highpass filtering
def highpass(kernel, image):

    #Taking height and width of both kernel and image
    im_height, im_width = image.shape
    kernel_height, kernel_width = kernel.shape

    #Padding amount is half of window size to prevent window from using undefined pixel values
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode = 'constant')

    #initializing filtered_image
    filtered_image = np.zeros_like(image, dtype = np.float32)

    #loop to iterate through pixel values 
    for i in range(im_height):
        for j in range(im_width):

            #selecting area around pixel to apply high pass filter kernel to
            filtered_image[i,j] = np.sum(kernel * padded_image[i:i + kernel_height, j:j + kernel_width])

    #converting image back to visible range
    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)

    return filtered_image

#plotting
def plot(image, title, num):

    plt.subplot(1, 3, num)
    plt.imshow(image, cmap = 'gray')
    plt.axis('off')
    plt.title(title)

plt.figure(figsize = (14, 3))

plot(image, 'Original Image', 1)
plot(highpass(filter_kernel5x5, image), '5x5 Filter Kernel', 2)
plot(highpass(filter_kernel7x7, image), '7x7 Filter Kernel', 3)


plt.tight_layout()
plt.show()