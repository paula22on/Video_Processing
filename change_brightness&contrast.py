# capture.py
import numpy as np
import cv2

# Capture video from camera
# cap = cv2.VideoCapture(0)

# Capture video from file
cap = cv2.VideoCapture('yolov7-pose/shortvideo.m4v')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('yolov7-pose/shortvideo_contrastbrighntess.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (frame_width,frame_height))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #change colorspace 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #modify contrast and brightness
    contrast = 0.5
    brightness = 2
    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',frame)
  
    
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# def increase_brightness(img, value=30):
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h, s, v = cv2.split(hsv)

#     lim = 255 - value
#     v[v > lim] = 255
#     v[v <= lim] += value

#     final_hsv = cv2.merge((h, s, v))
#     img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
#     return img

# while(cap.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     hsv = increase_brightness(frame, value=40)

    
    
#     out.write(hsv)
#     # Display the resulting frame
#     cv2.imshow('frame',hsv)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()