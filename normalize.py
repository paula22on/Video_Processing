# capture.py
import numpy as np
import cv2

# Capture video from camera
# cap = cv2.VideoCapture(0)

# Capture video from file
cap = cv2.VideoCapture('yolov7-pose/videos/shortvideo.m4v')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('yolov7-pose/videos/shortvideo_normalized.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #change colorspace 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #normalize
    norm_img = np.zeros((800,800))
    normalized_frame = cv2.normalize(frame,  norm_img, 0, 255, cv2.NORM_MINMAX)

    frame = cv2.cvtColor(normalized_frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',frame)
  
    
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()


