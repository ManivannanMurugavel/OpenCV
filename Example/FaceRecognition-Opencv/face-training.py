import cv2
import numpy as np
import os
from PIL import Image


recog = cv2.face.LBPHFaceRecognizer_create()

path = 'training-data'

faces = []
ids = []
def ImagewithID(path):
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.endswith('.jpg'):
				print(root.split('/')[-1],file)
				faceImg = Image.open(os.path.join(root,file)).convert('L')
				faceNP = np.array(faceImg,'uint8')
				id = int(root.split('/')[-1])
				faces.append(faceNP)
				ids.append(id)
				cv2.imshow('Training Image',faceNP)
				cv2.waitKey(10)

	return np.array(ids),faces

ids,faces = ImagewithID(path)

recog.train(faces,ids)

recog.save('employee.yml')