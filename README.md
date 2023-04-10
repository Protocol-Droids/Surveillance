# Surveillance
This Python script captures images from the default camera (index 0) on the user's computer and saves them as JPEG files if motion is detected. Motion detection is based on changes in pixel values between successive frames, and the script uses the OpenCV library to compute the absolute difference between two grayscale frames, apply thresholding to the frame difference, and dilate the thresholded image to fill in gaps. The script then finds contours in the dilated image and saves the current frame as a JPEG image if contours are detected.
<br/>Requires Python version >= 3.9 <br>
## Usage 
Clone this repository to your local machine using 
```sh
git clone https://github.com/Protocol-Droids/Surveillance.git
```
Install OpenCV2
```sh
pip install opencv-python
```

Navigate to the directory where the script is located using the command line. <br/>
The script will open the default camera and start capturing frames. If motion is detected, the current frame will be saved as a JPEG image in the same directory as the script with a file name in the format "YYYY-MM-DD_HH-MM-SS.jpg". You can adjust the sensitivity of the motion detection by changing the threshold value in cv2.absdiff() and cv2.threshold() functions. <br/>
Press Ctrl+C to stop the script and release the camera.

## clean.py
This code deletes all JPEG files (files with the ".jpg" file extension) in the current working directory.
