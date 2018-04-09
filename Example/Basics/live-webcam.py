import cv2

cap = cv2.VideoCapture(0)
#Note 0 or -1 is mention to your default webcam
#If you added new camera please mention 1 or etc(2,3,4,....) 

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to Gray from BGR
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Original',frame)
    cv2.imshow('Gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Press 'Q' to Close