import numpy as np
import cv2 as cv
import random

def mouse_event_handler(event, x, y, flags, param):

    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
        param[2] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False


canvas = np.full((480, 640, 3), 255, dtype=np.uint8)
i = 0
mouse_state = [False, (-1, -1), (255, 255, 255)]
cv.namedWindow('COD')
cv.setMouseCallback('COD', mouse_event_handler, mouse_state)

while True:
    
    mouse_left_button_click, mouse_xy, circle_color = mouse_state
    if mouse_left_button_click:
        cv.circle(canvas, mouse_xy, random.randint(10, 60), circle_color, -1)

    cv.line(canvas, (320, i), (320, i+10), color=(200, 200, 200), thickness=20)
    i += 5
    if i+10 == 480:
        i = 0

    canvas_copy = canvas.copy()
    cv.imshow('COD', canvas_copy)


    key = cv.waitKey(1)
    if key == 27: # ESC
        break


cv.destroyAllWindows()
