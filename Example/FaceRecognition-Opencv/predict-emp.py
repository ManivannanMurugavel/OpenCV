import cv2
# import np

font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


face_detector = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(2)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('employee.yml')

names = ['','Manivannan','Akshay','Kallil']

id= 0

while True:
	ret,img = cam.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_detector.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
		id,conf = recognizer.predict(gray[y:y+h,x:x+w])
		cv2.putText(img, str(names[id]), (x,y), font, 2, (255,0,0), 3)

	cv2.imshow('Image',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()