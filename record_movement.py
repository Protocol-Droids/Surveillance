from cv2 import VideoCapture, cvtColor, absdiff, threshold, getStructuringElement, dilate, findContours, MORPH_ELLIPSE, THRESH_BINARY, RETR_EXTERNAL, imwrite, imshow, waitKey, destroyAllWindows, CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_mail(message = 'This is a test email.', recipient_email = 'martin.arthur.andersen@gmail.com', subject = 'Email from bot'):
    sender_email = 'bot@nettking.no'
    sender_name = 'Nettking Surveillance Bot'
    msg = MIMEText(message)
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient_email
    msg['Subject'] = subject

    with smtplib.SMTP('smtp.proisp.no', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email, 'JabbaJabbaHei1990')
        smtp.sendmail(sender_email, recipient_email, msg.as_string())

# open the default camera (index 0)
cap = VideoCapture(0)

# initialize the first frame
_, frame1 = cap.read()
gray1 = cvtColor(frame1, COLOR_BGR2GRAY)
last_email_time = time.time() # initialize last email time
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
        if current_time - last_email_time >= 3600:
            send_mail('Movement Detected')
            last_email_time = current_time
    
    # update the previous frame
    gray1 = gray2


    # display the frame
    imshow('Preview', frame2)

    # wait for key press and exit if 'q' is pressed
    if waitKey(1) & 0xFF == ord('q'):
        break
# release the camera and close the window
cap.release()
destroyAllWindows()
