ASCII WebCam 
A simple program what cathes webcam frame resizes them,converts them to grayscale and converts them into ascii art and displays it to the terminal in real time.

Requirements:
  install dependencies
  pip install -r requirements.txt
it contains 
numpy 
opencv-contrib-python

How it works:
Captures the frame from webcam
Resizes them to reduce load
Converts them into grayscale 
maps the values from (0-255) to ascii characters using numpy.digitize
print ascii frmaes to the terminal 
repeat at 30 fps.

Lisence:
  Do whatever you want
