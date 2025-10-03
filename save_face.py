import cv2
import os

PHONE_URL = "http://192.168.254.100:8080/video"
DB_PATH = "faces_db"
os.makedirs(DB_PATH, exist_ok=True)



cap = cv2.VideoCapture(PHONE_URL)
print("Press SPACE to capture your face, ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No frame received from phone camera")
        break

    cv2.imshow("Capture Face", frame)
    key = cv2.waitKey(1)

    if key == 27:  
        break
    elif key == 32:
        NAME = input("Enter Name: ")

        file_path = os.path.join(DB_PATH, f"{NAME}.jpg")
        cv2.imwrite(file_path, frame)
        print(f"Saved face to {file_path}")
        break

cap.release()
cv2.destroyAllWindows()
