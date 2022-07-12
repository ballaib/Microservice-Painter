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
    radius = randrange(w)
    color = (randrange(255), randrange(255), randrange(255))
    thickness = randrange(10)
    cv.circle(image, (x1, y1), radius, color, thickness)
    # output
    cv.imwrite(painting_file, image)

sys.exit(0)