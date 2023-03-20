# Image-Acquisition-from-Web-Camera
## Aim
 
To write a python program using OpenCV to capture the image from the web camera and do the following image manipulations.
i) Write the frame as JPG 
ii) Display the video 
iii) Display the video by resizing the window
iv) Rotate and display the video

## Software Used
Anaconda - Python 3.7

## Algorithm

### Step 1:
Import cv2 and capture the video using cv2.VideoCapture(0).

### Step 2:
Write the captured image using cv2.imwrite("NewPicture.jpg",frame).

### Step 3:
Resize the image using cv2.resize(frame, (0,0), fx = 0.5, fy=0.5).

### Step 4:
Display the image until the loop gets over.

### Step 5:
Rotate the image using cv2.rotate(smaller_frame,cv2.ROTATE_180).

## Program:

### Developed By: Sanjay S
### Register No: 212221230086

## i) Write the frame as JPG file
```
import cv2
videoCaptureObject = cv2.VideoCapture(0)
while(True):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
```



## ii) Display the video
```
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()
```


## iii) Display the video by resizing the window

```
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(4))
    height = int(cap.get(5))
    
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()
```



## iv) Rotate and display the video
```
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:,: width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame


    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('s'):
        break
cap.release()
cv2.destroyAllWindows()
```

## Output

### i) Write the frame as JPG image

![ex2](https://user-images.githubusercontent.com/94231938/226421134-d6559824-7b42-434f-8b0f-62bdeb09cb30.png)

### ii) Display the video

![2023-03-20 (5)](https://user-images.githubusercontent.com/94231938/226421171-d29fe47c-ee8b-40fb-86bb-065043223971.png)

### iii) Display the video by resizing the window

![2023-03-20 (6)](https://user-images.githubusercontent.com/94231938/226421208-35d6210b-9dfd-41a8-8dad-c678700fd3a3.png)

### iv) Rotate and display the video

![2023-03-20 (7)](https://user-images.githubusercontent.com/94231938/226421226-f24497e4-fa72-4a16-82ae-8277c5a46284.png)

## Result:
Thus the image is accessed from webcamera and displayed using openCV.
