import cv2

img = cv2.imread("C:/Users/abdul/PycharmProjects/OpencvPython/Resources/anya.jpg")

imgCanny = cv2.Canny(img,500,500)

cv2.imshow("Image", imgCanny)
cv2.waitKey(0)
