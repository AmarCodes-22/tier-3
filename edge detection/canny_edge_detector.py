import cv2 as cv
import os
import numpy as np

#* Setting up directories
photos_loc = os.path.join(os.getcwd(), 'images')

img = cv.imread(os.path.join(photos_loc, 'cube.jpg'))

#resized = cv.resize(img, (img.shape[1]//4, img.shape[0]//4))

cv.imshow('Original', img)

# Canny edge detector works great.
canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

# Keeps the window(s) active indefinitely until ESC key is pressed.
while True:
    k = cv.waitKey(0) & 0xFF
    print(k)
    if k == 27:
        cv.destroyAllWindows()
        break