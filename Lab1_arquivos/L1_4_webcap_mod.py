import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Get current width of frame
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# Get current height of frame
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# Define Video Frame Rate in fps
fps = 25.0

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('saida.avi', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # write the frame
    out.write(frame)
    
    # Display the frame
    cv.imshow('frame', frame)
    
    # wait for 'q' key to exit
    if cv.waitKey(int(1000 / fps)) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
