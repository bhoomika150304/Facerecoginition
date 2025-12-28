import cv2
import numpy as np
import sys
import os

# Load Face Cascade
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open Webcam
cam = cv2.VideoCapture(0)

# Get User ID from Command Line Argument
if len(sys.argv) < 2:
    print("Error: No User ID provided!")
    sys.exit(1)

user_id = sys.argv[1]  # Get ID from Flask

# Create Dataset Directory if Not Exists
dataset_path = "dataSet"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

sampleNum = 0
Max_sample = 1000  # Limit to 100 images

while True:
    ret, img = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sampleNum += 1
        img_path = f"{dataset_path}/User.{user_id}.{sampleNum}.jpg"
        cv2.imwrite(img_path, gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100)

    cv2.imshow("Capturing Faces", img)
    cv2.waitKey(1)

    if sampleNum >= Max_sample:
        break

cam.release()
cv2.destroyAllWindows()

print(f"✅ Dataset creation completed for User ID: {user_id}")
