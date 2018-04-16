import cv2
import os

face_detector = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(2)

emp_id = input('Enter Your EMP ID >')

if not os.path.isdir('training-data/{}'.format(emp_id)):
	os.mkdir('training-data/{}'.format(emp_id))
else:
	print('Folder Already Exists')

cnt = 0

while (True):
	ret,img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cnt += 1
		cv2.imwrite('training-data/{}/{}.jpg'.format(emp_id,cnt),gray[y:y+h,x:x+w])
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
	cv2.imshow('Ori Image',img)
	if cv2.waitKey(1) & 0xFF == ord('q') or cnt == 20:
		break

cam.release()
cv2.destroyAllWindows()







