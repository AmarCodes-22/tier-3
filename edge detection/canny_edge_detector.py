import cv2 as cv
import os
import numpy as np

# Reads the image from the path specified.
img = cv.imread(os.path.join(os.getcwd(), 'images', 'cube.jpg'))

# Shows the image in a new window.
cv.imshow('Cube', img)

# Canny edge detector works great.
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges detected in the image', canny)

# Keeps the window(s) active indefinitely until a key is pressed.
cv.waitKey(0)