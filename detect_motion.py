import time
from cv2 import cvtColor, absdiff, threshold, getStructuringElement, dilate, findContours, MORPH_ELLIPSE, THRESH_BINARY, RETR_EXTERNAL, imwrite, CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY


def detect_motion(frame2, gray1, new_file_name, threshold_detect_motion=150):
        # convert the frame to grayscale
        gray2 = cvtColor(frame2, COLOR_BGR2GRAY)
        
        # compute the absolute difference between the two frames
        frame_diff = absdiff(gray1, gray2)
        
        # apply thresholding to the frame difference
        _, thresh = threshold(frame_diff, threshold_detect_motion, 255, THRESH_BINARY)
        
        # dilate the thresholded image to fill in the gaps
        kernel = getStructuringElement(MORPH_ELLIPSE, (5, 5))
        dilated = dilate(thresh, kernel, iterations=5)
        
        # find contours in the dilated image
        contours, _ = findContours(dilated, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
        
        # if contours are detected, capture the frame as a JPEG image and break the loop
        if len(contours) > 0:
            imwrite(new_file_name + ".jpg", frame2)
            #break
    
        # update the previous frame
        gray1 = gray2