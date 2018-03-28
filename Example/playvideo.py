import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="Please mention your video file")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args['video'])
if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    frame = cv2.resize(frame,(480,270))
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
