import cv2
try:
    # open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # check if the camera is opened successfully
    if not cap.isOpened():
        print("Error opening the camera")
        exit()

    # capture a frame
    ret, frame = cap.read()

    # save the captured frame as selfie.png
    cv2.imwrite("selfie.jpg", frame)

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
except:
    pass
print('Picture saved as selfie.png')