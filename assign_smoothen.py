#Gaussian blur-instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used 
# A Gaussian kernel is a kernel with the shape of a Gaussian (normal distribution) curve.
import cv2
img=cv2.imread("noi.jpg")
gaussian_blur=cv2.GaussianBlur(img,(17,17),0)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
#APPLICATION:Gaussian filtering is highly effective in removing Gaussian noise from the image.
