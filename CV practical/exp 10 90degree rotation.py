import cv2 
# Load the image 
img = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\MS Dhon wal.png") 

rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 

cv2.imshow("Rotated Image", rotated_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()