import numpy as np
import cv2 as cv
from time import sleep

canvas = np.full((480, 640, 3), 255, dtype=np.uint8)
i = 0

while True:

    canvas = np.full((480, 640, 3), 255, dtype=np.uint8)

    sleep(1)

    cv.line(canvas, (320, i), (320, i+5), color=(200, 200, 200), thickness=2)
    i += 1

    canvas_copy = canvas.copy()
    cv.imshow('Shape Drawing', canvas_copy)

    key = cv.waitKey(1)
    if key == 27: # ESC
        break


cv.destroyAllWindows()
