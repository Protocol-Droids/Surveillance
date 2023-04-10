import cv2
import datetime



# open the default camera (index 0)
cap = cv2.VideoCapture(0)

# initialize the first frame
_, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # get the current date and time
    now = datetime.datetime.now()
    new_file_name = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
    # capture a frame
    ret, frame2 = cap.read()
    if not ret:
        print("Error reading the frame")
        break
    
    # convert the frame to grayscale
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # compute the absolute difference between the two frames
    frame_diff = cv2.absdiff(gray1, gray2)
    
    # apply thresholding to the frame difference
    _, thresh = cv2.threshold(frame_diff, 150, 255, cv2.THRESH_BINARY)
    
    # dilate the thresholded image to fill in the gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilated = cv2.dilate(thresh, kernel, iterations=5)
    
    # find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # if contours are detected, capture the frame as a JPEG image and break the loop
    if len(contours) > 0:
        cv2.imwrite(new_file_name + ".jpg", frame2)
        #break
    
    # update the previous frame
    gray1 = gray2

# release the camera and close the window
#cap.release()
#cv2.destroyAllWindows()
