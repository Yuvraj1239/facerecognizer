import cv2
import face_recognition 
import pickle
import os 

folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []

studentIds = []

for path in PathList:
	imgList.append(cv2.imread(os.path.join(folderPath,path)))
	print(path)
	print(os.path.splitext(path)[0])
	studentIds.append(os.path.splitext(path)[0])
	print(studentIds)
def findEncodings(imageList):
	encodeList =[]
	for img in imageList:
		#img = cv2.cvtColor(img.cv2.COLOR_BGR2RCB)
		encode = face_recognition.face_encodings(img)[0]
		encodeList.append(encode)
		return encodeList
print("encoding stareted ..")
encodeListKnown = findEncodings(imgList)

encodeListKnownWithIds = [encodeListKnown,studentIds]
print("encoding complete ..")
file = open("encodefile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")


