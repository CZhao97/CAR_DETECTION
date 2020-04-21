import cv2
import numpy as np
from numpy.linalg import norm
import sys
import os
import json



# training images' width and height
SZ = 20

# width of original image
MAX_WIDTH = 1000

# maximum allowable plate area in an image
MIN_AREA = 2000

PROVINCE_STATE = 1000

# read images
def image_re