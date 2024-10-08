import cv2
import numpy as np
import matplotlib.pyplot as plt


dimension = [206, 206]

#Images aligned before using them in the code
Image1 = cv2.resize(cv2.imread("Processing Images/mask_Image1.png"), dimension)
Image2 = cv2.resize(cv2.imread("Processing Images/mask_Image2.png"), dimension)
Image3 = cv2.resize(cv2.imread("Processing Images/mask_Image3.png"), dimension)
Image4 = cv2.resize(cv2.imread("Processing Images/mask_Image4.png"), dimension)
Image5 = cv2.resize(cv2.imread("Processing Images/mask_Image5.png"), dimension)

def plot(Image, title, num):
	Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
	plt.subplot(1, 5, num)
	plt.imshow(Image)
	plt.axis('off')
	plt.title(title)

plt.figure(figsize = (14, 4))

plot(Image1, 'Image 1', 1)
plot(Image2, 'Image 2', 2)
plot(Image3, 'Image 3', 3)
plot(Image4, 'Image 4', 4)
plot(Image5, 'Image 5', 5)


plt.tight_layout()


#eyes and mouth start and end coordinates
y1e, y2e, x1e, x2e = 65, 105, 50, 160
y1m, y2m, x1m, x2m = 145, 175, 75, 135

#Swapping mouth and eyes of base Image 1 with eyes of Image 4 and mouth of Image 3
# Extract the facial features from the original images
roi_eyebrows1 = Image1[y1e:y2e, x1e:x2e].copy()
roi_mouth1 = Image1[y1m:y2m, x1m:x2m].copy()

roi_eyebrows3 = Image4[y1e:y2e, x1e:x2e].copy()
roi_mouth3 = Image3[y1m:y2m, x1m:x2m].copy()

Image1_swapped = Image1.copy()
Image1_swapped[y1e:y2e, x1e:x2e] = roi_eyebrows3
Image1_swapped[y1m:y2m, x1m:x2m] = roi_mouth3


#Swapping mouth and eyes of base Image 1 with eyes of Image 2 and mouth of Image 5
roi_eyebrows1 = Image1[y1e:y2e, x1e:x2e].copy()
roi_mouth1 = Image1[y1m:y2m, x1m:x2m].copy()

roi_eyebrows3 = Image2[y1e:y2e, x1e:x2e].copy()
roi_mouth3 = Image5[y1m:y2m, x1m:x2m].copy()

Image2_swapped = Image1.copy()
Image2_swapped[y1e:y2e, x1e:x2e] = roi_eyebrows3
Image2_swapped[y1m:y2m, x1m:x2m] = roi_mouth3


# Display the swapped image
plt.figure(figsize=(15, 5))

# Display the swapped image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(Image1, cv2.COLOR_BGR2RGB))
plt.title('Base Image')

#Image uses Image1 as base, Image 4 eyes, and image 3 mouth
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(Image1_swapped, cv2.COLOR_BGR2RGB))
plt.title('Image 1 Base, Image 4 Eyes, Image 3 Mouth')

#Image uses Image1 as base, Image 2 eyes, and image 5 mouth
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(Image2_swapped, cv2.COLOR_BGR2RGB))
plt.title('Image 1 Base, Image 2 Eyes, Image 5 Mouth')


plt.show()