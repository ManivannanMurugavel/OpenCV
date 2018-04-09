import cv2


img = cv2.imread('manivannan.jpg',-1)

# Display the Read Image

cv2.imwrite("manivannan.png",img)

cv2.waitKey(0)

cv2.destroyAllWindows()