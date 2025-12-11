import cv2 as cv

def to_grayscale(frame):
   return cv.cvtColor(frame,cv.COLOR_BGR2GRAY)


def resize_frame(frame, new_width=120):
    h, w = frame.shape[:2]
    ratio = h / w * 0.55
    new_height = int(new_width * ratio)
    return cv.resize(frame, (new_width, new_height))


