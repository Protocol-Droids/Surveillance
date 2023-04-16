from cv2 import VideoCapture, cvtColor, imshow, waitKey, destroyAllWindows, COLOR_BGR2GRAY
import datetime
from detect_motion import detect_motion
#from create_zip_archive import create_zip_archive


# open the default camera (index 0)
cap = VideoCapture(0)

# initialize the first frame
_, frame1 = cap.read()
gray1 = cvtColor(frame1, COLOR_BGR2GRAY)
threshold_detect_motion=input("Enter threshold for motion detection: ")
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
    detect_motion(frame2, gray1, new_file_name, threshold_detect_motion)

    # display the frame
    imshow('Preview', frame2)

    # wait for key press and exit if 'q' is pressed
    if waitKey(1) & 0xFF == ord('q'):
        break


# release the camera and close the window
cap.release()
destroyAllWindows()
