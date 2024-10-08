import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("Processing Images/Median_Image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Function to perform the median filtering
def median(window_size, image, num):

    #gathering height and width of image
    im_height, im_width = image.shape

    #padding image to prevent window from using undefined pixel values
    pad_size = window_size // 2

    padded_image = np.pad(image, ((pad_size), (pad_size)), mode = 'constant')

    #initializing filtered_image array
    filtered_image = np.zeros_like(image)

    #for loop that iterates through each pixel and applying median computations
    for i in range(im_height):
        for j in range(im_width):
            window = padded_image[i:(i + window_size), j:(j + window_size)]
            median_value = np.median(window)

            #setting pixel values to median 
            filtered_image[i, j] = median_value

    #converting image back to observable pixel range
    filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)

    plt.subplot(1, 5, num)
    plt.imshow(filtered_image, cmap = 'gray')
    plt.axis('off')
    plt.title(f'Filtered Image Window Size {window_size}x{window_size}')



plt.figure(figsize = (15, 5))

plt.subplot(1, 5, 1)
plt.imshow(image, cmap = 'gray')
plt.axis('off')
plt.title('Original Image')

median(3, image, 2)
median(5, image, 3)
median(7, image, 4)

plt.tight_layout()
plt.show()