import os
import cv2
import numpy as np
from PIL import Image


recognizer=cv2.face.LBPHFaceRecognizer_create();


path='dataSet/'



def getImagesWithID(path):     #loop through all the images for that use a functions
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]  #to use a list .join to append the path with images 
	
	
	faces=[]
	IDs=[]
	for imagePath in imagePaths:
		faceImg=Image.open(imagePath).convert('L');
		faceNp=np.array(faceImg,'uint8')
		ID=int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		print( ID )
		IDs.append(ID)
		cv2.imshow("training",faceNp)
		cv2.waitKey(10)
	return IDs,faces


Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.write('recognizer/model.yml')
cv2.destroyAllWindows()
