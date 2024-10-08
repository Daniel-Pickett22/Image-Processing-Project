import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load and convert the image to grayscale
image = cv2.imread("Processing Images/Fourier_Image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original image
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.title('Original Image')

# Define a function for the complex exponential
def f(X, Y, u, v):
    return np.exp(-1j * 2 * np.pi * (u * X + v * Y))

# Get the dimensions of the image
im_height, im_width = image.shape

# Initialize complex arrays to store phase information
phase1 = np.zeros_like(image, dtype=np.complex64)
phase2 = np.zeros_like(image, dtype=np.complex64)
phase3 = np.zeros_like(image, dtype=np.complex64)
phase4 = np.zeros_like(image, dtype=np.complex64)
phase5 = np.zeros_like(image, dtype=np.complex64)

phase6 = np.zeros_like(image, dtype=np.complex64)
phase7 = np.zeros_like(image, dtype=np.complex64)
phase8 = np.zeros_like(image, dtype=np.complex64)
phase9 = np.zeros_like(image, dtype=np.complex64)
phase10 = np.zeros_like(image, dtype=np.complex64)

phase11 = np.zeros_like(image, dtype=np.complex64)
phase12 = np.zeros_like(image, dtype=np.complex64)
phase13 = np.zeros_like(image, dtype=np.complex64)
phase14 = np.zeros_like(image, dtype=np.complex64)
phase15 = np.zeros_like(image, dtype=np.complex64)

phase16 = np.zeros_like(image, dtype=np.complex64)
phase17 = np.zeros_like(image, dtype=np.complex64)
phase18 = np.zeros_like(image, dtype=np.complex64)
phase19 = np.zeros_like(image, dtype=np.complex64)
phase20 = np.zeros_like(image, dtype=np.complex64)

phase21 = np.zeros_like(image, dtype=np.complex64)
phase22 = np.zeros_like(image, dtype=np.complex64)
phase23 = np.zeros_like(image, dtype=np.complex64)
phase24 = np.zeros_like(image, dtype=np.complex64)
phase25 = np.zeros_like(image, dtype=np.complex64)

# List to store all phase images
phase_images = []

# Loop over v and u values to calculate phase images
for v in range(2, -3, -1):
    for u in range(-2, 3):
        # Initialize a complex array for the current phase
        phase = np.zeros_like(image, dtype=np.complex64)

        # Loop over image pixels to calculate the phase
        for a in range(im_width):
            for b in range(im_height):
                phase[a, b] += image[a, b] * f(a, b, v, u)

        # Append the current phase to the list
        phase_images.append(phase)

# Create a 5x5 subplot for visualization
fig, axs = plt.subplots(5, 5, figsize=(12, 12))

axs = axs.flatten()

# Initialize u, v, and counter for titles
u = -2
v = 2
counter = 0

# Loop over phase images for visualization
for i, phase in enumerate(phase_images):
    # Get the phase spectrum using the angle function
    phase_spectrum = np.angle(phase)
    
    # Display the phase spectrum in the subplot
    axs[i].imshow(phase_spectrum, cmap='gray')
    axs[i].axis('off')  # Turn off axis labels and ticks
    axs[i].set_title(f'u = {u}, v = {v}')

    # Update u, v, and counter
    counter += 1 
    if counter == 5:
        u -= 5
        v -= 1
        counter = 0

    u += 1

# Show the subplots
plt.show()
