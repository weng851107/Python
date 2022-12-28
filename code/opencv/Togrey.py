import cv2 as cv


image = cv.imread('haha.bmp')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.resize(image, (640, 480), interpolation = cv.INTER_CUBIC)

cv.imshow('Result', image)

cv.imwrite("haha_grey.bmp", image)

cv.waitKey(0)