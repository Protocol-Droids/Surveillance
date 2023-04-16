from cv2 import VideoCapture, cvtColor, absdiff, threshold, getStructuringElement, dilate, findContours, MORPH_ELLIPSE, THRESH_BINARY, RETR_EXTERNAL, imwrite, imshow, waitKey, destroyAllWindows, CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY
import datetime
import time
from send_email import send_mail

def detect_motion(frame2, gray1):
        # convert the frame to grayscale
        gray2 = cvtColor(frame2, COLOR_BGR2GRAY)
        
        # compute the absolute difference between the two frames
        frame_diff = absdiff(gray1, gray2)
        
        # apply thresholding to the frame difference
        _, thresh = threshold(frame_diff, 150, 255, THRESH_BINARY)
        
        # dilate the thresholded image to fill in the gaps
        kernel = getStructuringElement(MORPH_ELLIPSE, (5, 5))
        dilated = dilate(thresh, kernel, iterations=5)
        
        # find contours in the dilated image
        contours, _ = findContours(dilated, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
        
        # if contours are detected, capture the frame as a JPEG image and break the loop
        if len(contours) > 0:
            imwrite(new_file_name + ".jpg", frame2)
            #break
            current_time = time.time()
            print('Time diff email delay: ' + str(current_time - last_email_time))
            if current_time - last_email_time >= email_delay:
                send_mail('Movement Detected')
                last_email_time = current_time
    
        # update the previous frame
        gray1 = gray2







# open the default camera (index 0)
cap = VideoCapture(0)

# initialize the first frame
_, frame1 = cap.read()
gray1 = cvtColor(frame1, COLOR_BGR2GRAY)
last_email_time = time.time() # initialize last email time
email_delay = input("Enter delay in seconds between email warning: ")

while True:
    # get the current date and time
    now = datetime.datetime.now()
    new_file_name = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
    
    # capture a frame
    ret, frame2 = cap.read()
    if not ret:
        print("Error reading the frame")
        break

    # detect motion
    detect_motion(frame2, gray1)

    # display the frame
    imshow('Preview', frame2)

    # wait for key press and exit if 'q' is pressed
    if waitKey(1) & 0xFF == ord('q'):
        break
# release the camera and close the window
cap.release()
destroyAllWindows()
