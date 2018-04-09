import cv2
import imutils

coin_img = cv2.imread('coin.jpg')

gray = cv2.cvtColor(coin_img, cv2.COLOR_BGR2GRAY)

edgeMap = imutils.auto_canny(gray)

cv2.imshow("Original", coin_img)

cv2.imshow("Automatic Edge Map", edgeMap)


cv2.waitKey(0)