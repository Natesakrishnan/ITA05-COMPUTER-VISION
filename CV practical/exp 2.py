import cv2 
image = cv2.imread(r"C:\Users\Nadesa Krishnan\OneDrive\Pictures\Screenshots\gettyimages-2233760409-612x612.jpg")  
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Original Image", image) 
cv2.imshow("Blurred Image", blurred_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()