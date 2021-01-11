import cv2

camera_id = 0

video = cv2.VideoCapture(camera_id)

while True:
    ret, frame = video.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video", gray)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()


