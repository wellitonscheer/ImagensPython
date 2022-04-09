import cv2

img = cv2.imread('OpenCV_Logo.png', 1)

cv2.namedWindow('Hello World')
cv2.imshow('Hello World', img)
cv2.waitKey()