# capture.py
import numpy as np
import cv2

# Capture video from camera
# cap = cv2.VideoCapture(0)

# Capture video from file
cap = cv2.VideoCapture('yolov7-pose/shortvideo.m4v')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('yolov7-pose/shortvideo_hsv.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))



while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    out.write(hsv)
    # Display the resulting frame
    cv2.imshow('frame',hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()