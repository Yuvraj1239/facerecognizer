#cvzone face recognition pyttsx3 
import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)
imgBackground = cv2.imread('resources/background.png')
folderModePath = 'resources/Modes'
modePath = os.listdir(folderModePath)
imgModeList =[]
for path in modePathList:
	imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))

while True:
	success, img = cap.read()
	imgBackground[162:162+480,55:55+640] = img
	imgBackground[44:44+633,808:808+414] = imgModeList[0]
	cv2.imshow("web cam",img)
	cv2/imshow("face attendance",imgBackground)
	cv2.waitKey(1)