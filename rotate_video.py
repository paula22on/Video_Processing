import cv2
    
#that's my original video - the one that I want to rotate 180 degrees 
cap = cv2.VideoCapture('yolov7-pose/shortvideo.m4v')
    
frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Get width and height
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# here I'm trying to write the new rotated video
# Open the output video file before the loop, cv2.VideoWriter_fourcc(*"mp4v") = 0x7634706d
newvideoR = cv2.VideoWriter('yolov7-pose/shortvideo.m4v', cv2.VideoWriter_fourcc(*"mp4v"), 50, (frame_width, frame_height))
    
# Original Frames
#frames = []
for i in range(frame_number):
    ret, frame = cap.read()
    #frames.append(frame)  # No need to append the original frames

    #here's where I try to rotate the video 
    new = cv2.rotate(frame, cv2.ROTATE_180)
    
    newvideoR.write(new)

newvideoR.release()
cap.release()