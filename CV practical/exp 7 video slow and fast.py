import cv2

# Open the video file
cap = cv2.VideoCapture(r"C:\Users\Nadesa Krishnan\OneDrive\Documents\movies\TamilPrint - Dhurandhar (2025) Tamil HD DVD Print 720pHD.mkv")   # Replace with your video file name

# Check if video is opened successfully
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display video
    cv2.imshow("Video Playback", frame)

    # Delay controls the speed
    # 30 ms -> Normal speed
    # 100 ms -> Slow motion
    # 10 ms -> Fast motion

    key = cv2.waitKey(9) & 0xFF   

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()