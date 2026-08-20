import cv2
import numpy as np

# Read image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce noise
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Hough Line Transform
lines = cv2.HoughLinesP(edges,
                        1,
                        np.pi/180,
                        threshold=100,
                        minLineLength=50,
                        maxLineGap=10)

# Draw detected lines
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1,y1), (x2,y2), (0,255,0), 2)

# Display images
cv2.imshow("Original Image", cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png"))
cv2.imshow("Detected Lines", image)

cv2.waitKey(0)
cv2.destroyAllWindows()