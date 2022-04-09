import cv2
import numpy as np

imgAlfa = cv2.imread('OpenCV_Logo.png', 1)
#img = cv2.imread("OpenCV_Logo.png", 1)
# print(imgAlfa[1])

for a in imgAlfa:
    for b in a:
        if b[0] != 255:
            print(b)
print(type(imgAlfa))
cv2.namedWindow('Hello World')
#cv2.imshow('Hello World', img)156
cv2.imshow('Hello World', imgAlfa)
cv2.waitKey()