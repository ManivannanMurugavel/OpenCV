
#install pyautogui package
#pip install pyautogui
import imutils
import pyautogui
import cv2



## Another Type
pyautogui.screenshot("straight_to_disk.png")
# we can then load our screenshot from disk in OpenCV format
image = cv2.imread("straight_to_disk.png")
cv2.imshow("Screenshot", imutils.resize(image, width=600))
cv2.waitKey(0)
