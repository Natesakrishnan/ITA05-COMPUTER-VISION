# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Read input image
image = cv2.imread(
r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png"
)
# Convert image into grayscale
gray_image = cv2.cvtColor(
image,
cv2.COLOR_BGR2GRAY
)
# Create kernel
kernel = np.ones(
(5,5),
np.uint8
)
# Apply dilation
dilated_image = cv2.dilate(
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
plt.title("Original Image")
plt.axis("off")
# Dilated Image
plt.subplot(1,2,2)
plt.imshow(
dilated_image,
cmap="gray"
)
plt.title("Dilated Image")
plt.axis("off")
plt.show()