import numpy as np
import cv2 as cv

canvas = np.full((480, 640, 3), 255, dtype=np.uint8)
i = 0

while True:

    canvas = np.full((480, 640, 3), 255, dtype=np.uint8)

    cv.line(canvas, (320, i), (320, i+10), color=(200, 200, 200), thickness=2)
    i += 5
    if i+10 == 480:
        i = 0

    canvas_copy = canvas.copy()
    cv.imshow('Shape Drawing', canvas_copy)

    key = cv.waitKey(1)
    if key == 27: # ESC
        break


cv.destroyAllWindows()
