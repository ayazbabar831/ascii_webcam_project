import cv2 as cv
import sys,time
from utils.image_utils import resize_frame
from utils.ascii_utils import frame_to_ascii
cap = cv.VideoCapture(0)
fps = 30
delay = 1 / fps


sys.stdout.write("\033[?25l")
sys.stdout.flush()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = resize_frame(frame, 180)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    ascii_img = frame_to_ascii(gray)

    sys.stdout.write("\033[H")
    sys.stdout.write(ascii_img)
    sys.stdout.flush()

    time.sleep(delay)


sys.stdout.write("\033[?25h")
sys.stdout.flush()

cap.release()
