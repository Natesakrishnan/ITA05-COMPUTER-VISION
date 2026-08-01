import cv2

# Load the original image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-28 104950.png")

# Load the watermark image
watermark = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\walp 2.jpeg")

# Resize watermark
watermark = cv2.resize(watermark, (200, 200))

# Get dimensions
(h_img, w_img) = image.shape[:2]
(h_wm, w_wm) = watermark.shape[:2]

# Position of watermark (bottom-right corner)
x = w_img - w_wm - 10
y = h_img - h_wm - 10

# Region of Interest (ROI)
roi = image[y:y+h_wm, x:x+w_wm]

# Blend watermark with ROI
blended = cv2.addWeighted(roi, 0.7, watermark, 0.3, 0)

# Replace ROI with blended image
image[y:y+h_wm, x:x+w_wm] = blended

# Display images
cv2.imshow("Original with Watermark", image)

# Save output
cv2.imwrite("watermarked_image.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()