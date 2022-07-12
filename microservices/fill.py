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
    color = (randrange(255), randrange(255), randrange(255))
    image[:] = color
    # output
    cv.imwrite(painting_file, image)

sys.exit(0)
