import cv2
import numpy as np

img = cv2.imread('coin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.medianBlur(img,5)
# cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
#                             param1=25,param2=40,minRadius=0,maxRadius=100)

# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

# cv2.imshow('detected circles',cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


blur = cv2.GaussianBlur(gray,(7,9),6)
cimg = cv2.cvtColor(blur,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,
                            param1=120,param2=10,minRadius=2,maxRadius=30)


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()