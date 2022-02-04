import cv2
#from ev3.ev3Publisher import release_gate
import numpy as np

from numpy.core.numerictypes import obj2sctype
from numpy.lib.type_check import imag
import os
#import fer as fr 
import time as tm

import matplotlib.pyplot as plt 

print('importando as bibliotecas...')

videoUrl = 'https://192.168.1.103:4747/video'
path = "cascades/data/"
video = cv2.VideoCapture(0)

cascaedeType = 'haarcascade_frontalface_alt2.xml' 

#setting the width and the height

video.set(3,640)
video.set(4,480)
video.set(10,100)

#motor = MediumMotor(OUTPUT_A)
 

faceCascade = cv2.CascadeClassifier(path + cascaedeType)
colorProfile = (0,0,255) #BGR
timeout = tm.time() + 30 #countdown 
person = False 
# CROPPED THE IMAGE 

def Analize_face(video):
    while True:
        sucess, img = video.read()
        #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  #turn the video 
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(imgGray,1.0485258 ,10)    
        for (x,y,w,h) in faces:
            user_img = "faces_checkImages/user-image.jpg"
            crop = img[y:y+h+60, x:x+w+60] # making the rectancgle image crop!
            cv2.imwrite(user_img, crop)   
            cv2.rectangle(img, (x,y),(x+w,y+h), colorProfile,2) #rectangle drawned in the video 

        cv2.imshow("VIDEO", img) #show the image  
        #Close 
        if tm.time() > timeout: #system clock
            cv2.destroyAllWindows()
            break 
        if cv2.waitKey(1) & 0xFF ==ord('q'): #user 
            break

def Comparing_faces():
    unknown_picture = fr.load_image_file('faces_checkImages/user-image.jpg')
    try:    
        unknown_face_encoding = fr.face_encodings(unknown_picture)[0]
    except IndexError:
        print('I cant find a face in this picture, try again!')
        exit()    
    picture_of_user = fr.load_image_file("faces_checkImages/user-image.png") #loading the picture sended by the user
    user_face_encoding = fr.face_encodings(picture_of_user)[0]

    results = fr.compare_faces([user_face_encoding], unknown_face_encoding)

    if results[0] == True:
            print('Mesma Pessoa')
            return person == True 
            #release_gate(person = person)
            
    else: 
            print("Não é a mesma Pessoa")
            return person == False
            #release_gate(person = person)
        

        
#ANALIZE AND COMPARE THE IMAGES TO KNOW IF IS THE SAME PERSO WHO IS RECEVING THE PRODUCT!.
Analize_face(video)
Comparing_faces()
