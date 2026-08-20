import cv2
import matplotlib.pyplot as plt

# Read input image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png")

# Check whether image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Preprocessing - Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Feature extraction using SIFT
sift = cv2.SIFT_create()

keypoints, descriptors = sift.detectAndCompute(gray, None)

# Draw detected keypoints
feature_image = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
feature_rgb = cv2.cvtColor(feature_image, cv2.COLOR_BGR2RGB)

# Display results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(edges, cmap="gray")
plt.title("Preprocessed - Edge Detection")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(feature_rgb)
plt.title("Extracted SIFT Features")
plt.axis("off")

plt.tight_layout()
plt.show()

print("Number of keypoints detected:", len(keypoints))
print("Feature descriptor shape:", descriptors.shape)