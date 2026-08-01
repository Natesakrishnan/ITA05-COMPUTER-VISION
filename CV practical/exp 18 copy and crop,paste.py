import cv2

# Load the source image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\walp 2.jpeg")

# Crop the Region of Interest (ROI)
# Format: image[start_row:end_row, start_col:end_col]
roi = image[50:200, 100:300]

# Copy and paste the ROI to another location
image[250:400, 350:550] = roi

# Display the original image with pasted ROI
cv2.imshow("ROI Copied and Pasted Image", image)

# Save the output image
cv2.imwrite("output.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()