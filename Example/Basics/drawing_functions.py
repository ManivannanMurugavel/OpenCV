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
elipse = img.copy()
poly = img.copy()

#cv2.circle('image','(From Point)',(To Point),(rgb color),Thickness_line)
cv2.line(line,(100,120),(400,120),(255,0,0),2)

#cv2.circle('image','(From Point)',(To Point),(rgb color),Thickness_line)
cv2.rectangle(rect,(10,10),(430,128),(0,255,0),2)

#cv2.circle('image','(center_point)',radius,(rgb color),fill_width)
cv2.circle(cir,(250,250), 50, (0,0,255), -1)

#cv2.ellipse('image',(Center point),(width,height),angle,start_angle,end_angle,(rgb color),fill width size)
cv2.ellipse(elipse,(256,256),(100,50),0,0,180,(0,0,255),-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,2,1))
cv2.polylines(poly,[pts],True,(0,255,255))


# Font Names

'''
Enumerator
FONT_HERSHEY_SIMPLEX 
Python: cv.FONT_HERSHEY_SIMPLEX
normal size sans-serif font

FONT_HERSHEY_PLAIN 
Python: cv.FONT_HERSHEY_PLAIN
small size sans-serif font

FONT_HERSHEY_DUPLEX 
Python: cv.FONT_HERSHEY_DUPLEX
normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)

FONT_HERSHEY_COMPLEX 
Python: cv.FONT_HERSHEY_COMPLEX
normal size serif font

FONT_HERSHEY_TRIPLEX 
Python: cv.FONT_HERSHEY_TRIPLEX
normal size serif font (more complex than FONT_HERSHEY_COMPLEX)

FONT_HERSHEY_COMPLEX_SMALL 
Python: cv.FONT_HERSHEY_COMPLEX_SMALL
smaller version of FONT_HERSHEY_COMPLEX

FONT_HERSHEY_SCRIPT_SIMPLEX 
Python: cv.FONT_HERSHEY_SCRIPT_SIMPLEX
hand-writing style font

FONT_HERSHEY_SCRIPT_COMPLEX 
Python: cv.FONT_HERSHEY_SCRIPT_COMPLEX
more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX

FONT_ITALIC 
Python: cv.FONT_ITALIC
flag for italic font
'''


font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img,'Manivannan',(100,100), font, 2,(255,0,255),2,cv2.LINE_AA)


cv2.imshow('Line Image',line)
cv2.imshow('Rectangle Image',rect)
cv2.imshow('Circle Image',cir)
cv2.imshow('Elipse Image',elipse)
cv2.imshow('Polygon Image',poly)
cv2.imshow('Text',img)
cv2.waitKey(0)
cv2.destroyAllWindows()