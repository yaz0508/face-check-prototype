import cv2
from deepface import DeepFace
import os

PHONE_URL = "http://192.168.254.100:8080/video"
DB_PATH = "faces_db"

cap = cv2.VideoCapture(PHONE_URL)
print("Taking a snapshot...")
ret, frame = cap.read()
cap.release()

if not ret:
    print("No frame received from phone camera")
else:
    temp_file = "temp.jpg"
    cv2.imwrite(temp_file, frame)

    result = DeepFace.find(
        img_path=temp_file,
        db_path=DB_PATH,
        detector_backend="opencv"
    )

    if len(result) == 0:
        print("No faces detected in the frame.")
    else:
        for i, df in enumerate(result):
            if not df.empty:
                matches = df["identity"].tolist()
                names = [os.path.basename(m) for m in matches]
                print(f"Face {i+1} matched with: {names}")
            else:
                print(f"Face {i+1}: No match found.")
