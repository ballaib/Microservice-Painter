import cv2 as cv
import numpy as np
from random import randrange
import sys

painting_file = "painting.png"
# perform operation
color = (randrange(255), randrange(255), randrange(255))
channels = 3
h, w = 250, 250
image = np.full((h, w, channels), color, dtype=np.uint8)
# output
cv.imwrite(painting_file, image)

sys.exit(0)
