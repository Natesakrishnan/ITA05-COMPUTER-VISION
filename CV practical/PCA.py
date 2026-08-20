import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png", cv2.IMREAD_GRAYSCALE)

# Apply PCA
pca = PCA(n_components=50)
reduced_data = pca.fit_transform(img)

# Reconstruct image
reconstructed = pca.inverse_transform(reduced_data)

# Display images
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(reconstructed, cmap='gray')
plt.title("PCA Reconstructed Image")
plt.axis("off")

plt.show()