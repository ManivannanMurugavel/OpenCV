### This is Only for Basics OpenCV Python

## Basics Functions in Opencv
        i) cv2.imread()
        ii)cv2.imwrite()
        iii)cv2.imshow()
        
       
## Read an image

Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.

Second argument is a flag which specifies the way image should be read.

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
Note Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.
See the code below:

```
import numpy as np
import cv2

#Load an color image in grayscale
img = cv2.imread('manivannan.jpg',0)
Warning Even if the image path is wrong, it won’t throw any error, but print img will give you None
```
