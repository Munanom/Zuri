import cv2

video_path = 0

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Could not open video file")
    exit()

while True:
    isTrue, frame = cap.read()

    if not isTrue:
        break

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if grayscale.size == 0:
        print("The image is empty")
        break

    # Detect faces using Haar Cascade classifier
    faces_rect = cv2.CascadeClassifier('/Users/muna/MachineLearning/Facerecog/haarcascade_frontalface_default.xml').detectMultiScale(grayscale, scaleFactor=1.1, minNeighbors=3)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Wait for a key press
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
