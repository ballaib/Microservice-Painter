import cv2 as cv
import numpy as np
from random import randrange
import sys
import os

# read
painting_file = "painting.png"
if os.path.exists(painting_file):
    image = cv.imread(painting_file, cv.IMREAD_COLOR)
    # perform operation
    h, w = image.shape[:2]
    x1 = randrange(w)
    y1 = randrange(h)
    x2 = randrange(w)
    y2 = randrange(h)
    color = (randrange(255), randrange(255), randrange(255))
    thickness = randrange(1, 10)
    cv.line(image, (x1, y1), (x2, y2), color, thickness)
    # output
    cv.imwrite(painting_file, image)

sys.exit(0)
