# Zuri

Real-Time Facial Recognition using OpenCV

This Python script leverages the OpenCV library to perform real-time facial recognition on video streams. The script captures video from the default camera (usually the webcam) but can be configured to read from a specific video file by modifying the 'video_path' variable. 
It processes each frame, converts it to grayscale, and utilizes the Haar Cascade classifier for face detection. When a face is detected, a green rectangle is drawn around it, making it visible to the user in real-time.

Instructions:

Make sure you have OpenCV installed (pip install opencv-python).
Modify the 'video_path' variable to specify the video source (default is the webcam).
Run the script to start real-time facial recognition.
Press the 'd' key to exit the application.
This script provides a simple and efficient way to perform facial recognition on live video feeds, making it suitable for various applications like security systems, access control, and face tracking.
