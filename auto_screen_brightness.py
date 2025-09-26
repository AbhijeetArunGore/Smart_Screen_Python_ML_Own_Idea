import cv2
import time
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_present = 0

def check_face():
    global face_present
    cap = cv2.VideoCapture(0)  # Open webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to access camera")
        cap.release()
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) > 0:
        face_present = 1
        print("Face detected!")
    else:
        face_present = 0
        print("No face detected.")

    cap.release()

import screen_brightness_control as sbc
current = sbc.get_brightness()
print("Current brightness:", current)
while True:
    check_face()
    print("Result variable:", face_present)
    time.sleep(60)
    if face_present:
        sbc.set_brightness(50)
    else:
        sbc.set_brightness(0)