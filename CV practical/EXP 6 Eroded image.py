# Import required libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read input image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png")

# Convert image into grayscale
gray_image = cv2.cvtColor(
image,cv2.COLOR_BGR2GRAY)
# Create kernel
kernel = np.ones(
(5,5),
np.uint8
)
# Apply erosion
eroded_image = cv2.erode(
gray_image,
kernel,
iterations=1
)
# Display images
plt.figure(figsize=(10,4))
# Original Image
plt.subplot(1,2,1)
plt.imshow(
gray_image,
cmap="gray"
)
plt.axis("off")
plt.title("Original Image")
# Eroded Image
plt.subplot(1,2,2)
plt.imshow(
eroded_image,
cmap="gray"
)
plt.title("Eroded Image")
plt.axis("off")
plt.show()