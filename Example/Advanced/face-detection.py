import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frontalface-default", required=True,
	help="path to haarcascade_frontalface_default")
ap.add_argument("-i", "--image", required=True,
	help="path to input image file")
args = vars(ap.parse_args())

print("[INFO] haarcascade_frontalface_default...")

face_cascade = cv2.CascadeClassifier(args["frontalface_default"])

img = cv2.imread(args["image"])

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow('Original Image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
