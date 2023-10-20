import cv2

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 represents the default camera, change it if you have multiple cameras

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(20, 20))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Face Detection - Khushi Choudhary', frame)

    # Exit the loop when the 'm' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
