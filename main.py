#cvzone face recognition pyttsx3 
import pyttsx3 
import numpy as np
import cv2
import pickle
import face_recognition
from flask import Flask,render_template,request
import pickle
import numpy as np
import speech_recognition as sr
import datetime
import mysql.connector
import cv2
import tkinter as tk
from PIL import ImageTk, Image
import sys

dt = "30/04/2023"
mydb =  mysql.connector.connect(host="localhost",user="root",passwd="nopassword")
mycursor = mydb.cursor()
mycursor.execute("use attendance")

current_time = datetime.datetime.now()

formatted_date = current_time.strftime("%d/%m/%Y")

print(formatted_date)



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)
engine.setProperty('voice',voices[1].id)
engine.say("hi welcome to face recognition application")
engine.runAndWait()
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
#load the encoding file
print("loading encode file") 
file = open('encodefile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown , studentIds = encodeListKnownWithIds
#peint(sudentIds)
print("encode file loaded")
yuvraj = []
def recognize_faces():
	while True:
		success, img = cap.read()
		imgS = cv2.resize(img,(0,0),None,0.25,0.25)
#conver bgr to rgb
		faceCurFrame = face_recognition.face_locations(imgS)
		encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

		for encodeFace, faceLoc in zip(encodeCurFrame,faceCurFrame):
			matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
			faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
			print("matches",matches)
			print("faceDis",faceDis)
			matchIndex = np.argmin(faceDis)
			print("match index",matchIndex)
			if matches[matchIndex] :
		
		
				if studentIds[matchIndex] in yuvraj:
					engine.say("face is already detected")
				
					break
				else:
					yuvraj.append(studentIds[matchIndex])
					engine.say("known Face detected    ")
					engine.say(studentIds[matchIndex])
				
					s ="insert into attend (date_attended,name) values(%s,%s)"
					t = (formatted_date,studentIds[matchIndex])
					mycursor.execute(s,t)
					mydb.commit()
				

					engine.runAndWait()
				break
		
			else:
		
				engine.say("no face detected")
				engine.runAndWait()
		
	 
		cv2.imshow("face attedance",img)
		cv2.waitKey(1)

# Function to perform face recognition

    
def exiter():
	sys.exit()
# Create a Tkinter window
window = tk.Tk()
window.title("Face Recognition")

# Create a button to perform face recognition
button = tk.Button(window, text="start recognition", command=recognize_faces)
button.pack(pady=10)
button2 = tk.Button(window, text="stop recognition", command=exiter)
button2.pack(pady=10)

# Create a label to display the image
label = tk.Label(window)
label.pack()

# Run the Tkinter event loop
window.mainloop()

