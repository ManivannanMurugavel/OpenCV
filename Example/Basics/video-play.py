import cv2

cap = cv2.VideoCapture('../Falls9.mov')

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        frame = cv2.resize(frame,(480,270))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
    else:
    	break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()