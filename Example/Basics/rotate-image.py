# Two types of rotate image
import cv2
import imutils
import time
# load the image from disk
image = cv2.imread('manivannan.jpg')
 
# loop over the rotation angles
for angle in range(0, 360, 15):
	rotated = imutils.rotate(image, angle)
	cv2.imshow("Rotated (Problematic)", rotated)
	time.sleep(0.2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
 
# loop over the rotation angles again, this time ensuring
# no part of the image is cut off
for angle in range(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	time.sleep(0.2)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cv2.destroyAllWindows()