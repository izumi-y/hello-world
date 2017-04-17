import numpy as np
import cv2

img = cv2.imread('lena.jpg')
imgg = cv2.imread('gray.jpg')
#sobel
dx = cv2.Sobel(imgg, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(imgg, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(dx ** 2 + dy ** 2)
#laplacian
laplacian = cv2.Laplacian(imgg, cv2.CV_64F)
#canny
canny =  cv2.Canny(imgg, 100, 200)

cv2.imshow('sobel', sobel)
cv2.imshow('laplacian', laplacian)
cv2.imshow('canny', canny)
cv2.imwrite('sobel.jpg',sobel)
cv2.imwrite('laplacian.jpg',laplacian)
cv2.imwrite('canny.jpg',canny)
cv2.waitKey(0)
cv2.destroyAllwindows()

