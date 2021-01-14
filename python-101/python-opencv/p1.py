import cv2
# import sys

camera_id = 0

video = cv2.VideoCapture(camera_id)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Video", gray)

    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


