import cv2
import matplotlib.pyplot as plt

# --------------------------------
# Step 1: Read the input image
# --------------------------------
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png")

# Check whether image is loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# --------------------------------
# Step 2: Convert to grayscale
# --------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------------
# Step 3: Preprocessing
# --------------------------------
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# --------------------------------
# Step 4: Edge detection
# --------------------------------
edges = cv2.Canny(blur, 50, 150)

# --------------------------------
# Step 5: Create SIFT detector
# --------------------------------
sift = cv2.SIFT_create()

# --------------------------------
# Step 6: Detect keypoints
# and calculate descriptors
# --------------------------------
keypoints, descriptors = sift.detectAndCompute(
    gray, None
)

# --------------------------------
# Step 7: Draw keypoints
# --------------------------------
output = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# Convert images from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

# --------------------------------
# Step 8: Display results
# --------------------------------
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
plt.title("Canny Edge Detection")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(output_rgb)
plt.title("Detected SIFT Features")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Step 9: Display information
# --------------------------------
print("Feature Detection Completed")
print("Number of keypoints:", len(keypoints))

if descriptors is not None:
    print("Descriptor size:", descriptors.shape)
else:
    print("No descriptors were generated.")