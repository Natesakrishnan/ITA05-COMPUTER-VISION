import cv2
import numpy as np

# Load the input image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\walp 2.jpeg")

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

# Save the output image
cv2.imwrite("eroded_image.jpg", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()