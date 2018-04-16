import cv2
import numpy as np

### Draw Line

# Create a black image
img = np.full((500,500,3),255, np.uint8)
# img.fill(255)
# Draw a diagonal blue line with thickness of 2 px
line = img.copy()
rect = img.copy()
cir = img.copy()

#cv2.circle('image','(From Point)',(To Point),(rgb color),Thickness_line)
cv2.line(line,(100,120),(400,120),(255,0,0),2)

#cv2.circle('image','(From Point)',(To Point),(rgb color),Thickness_line)
cv2.rectangle(rect,(10,10),(430,128),(0,255,0),2)

#cv2.circle('image','(center_point)',radius,(rgb color),fill_width)
cv2.circle(cir,(250,250), 50, (0,0,255), -1)

cv2.imshow('Line Image',line)
cv2.imshow('Rectangle Image',rect)
cv2.imshow('Circle Image',cir)
cv2.waitKey(0)
cv2.destroyAllWindows()