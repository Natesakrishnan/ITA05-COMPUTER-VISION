import cv2

# Load the pre-trained Haar Cascade for watch detection
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")

# Read the image
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Documents\ITA05 - COMPUTER VISION\CV practical\watch detect.webp")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches in the image
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw bounding boxes around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detections
cv2.imshow("Detected Watch", image)
cv2.waitKey(0)
cv2.destroyAllWindows()