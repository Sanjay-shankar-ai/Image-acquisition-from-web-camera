import cv2
videocaptureobject=cv2.VideoCapture(0)
while True:
    ret,frame=videocaptureobject.read()
    cv2.imshow("example.jpg",frame)
    if cv2.waitKey(1) == ord('q'):
        break
videocaptureobject.release()
cv2.destroyAllWindows()

