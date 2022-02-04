from os import add_dll_directory
from local import get_dist_van_to_local, get_user_local

from pycep_correios import get_address_from_cep, WebService
from geopy.geocoders import Nominatim
from geopy.distance import distance
from ipregistry import IpregistryClient
import geocoder
import time as tm 
import json
import urllib
import cv2
import numpy as np 
def empty(a):
    pass




#getting the user local
user_local = get_user_local()
print(user_local)


videoUrl = 'http://192.168.1.103:4747/video'
video = cv2.VideoCapture(0)

cv2.namedWindow('Trackerbars')

cv2.resizeWindow('Trackerbars',640,240)
cv2.createTrackbar("Hue Min", "Trackerbars", 0, 179,empty)
cv2.createTrackbar("Hue Max", "Trackerbars", 163, 179,empty)
cv2.createTrackbar("Sat Min", "Trackerbars", 0, 255,empty)
cv2.createTrackbar("Sat Max", "Trackerbars", 255, 255,empty)
cv2.createTrackbar("Val Min", "Trackerbars", 141, 255,empty)
cv2.createTrackbar("Val Max", "Trackerbars", 255, 255,empty)

def distanceCalculate(p1,p2):  # p1 and p2 in format (x1,y1) and (x2,y2) tuples
    dis=((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
    dis=abs(dis)   #removing negative sign.
    return dis
def know_direction():
    h, w = mask.shape
    half = w//2
    left_part = mask[:, :half] 
    right_part = mask[:, half:]  
    #showing the images 
    cv2.imshow('Left part', left_part)
    cv2.imshow('Right part', right_part)
    #saving the images 
    
    cv2.imwrite('carImages/right.jpg', right_part)
    cv2.imwrite('carImages/left.jpg', left_part)
    
    #knowing the numbers of pixels of wich images
    
    Left_pixels = cv2.countNonZero(left_part)
    Right_pixels = cv2.countNonZero(right_part)
    
    print(Left_pixels, Right_pixels)
    
    if Left_pixels == Right_pixels:
        return print('Go Straight')
    if Left_pixels > Right_pixels:
        return print('Go left')
    if Left_pixels < Right_pixels:
        return print('Go right')    
        

while True:        
    
    sucess, img = video.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  #turn the video 
    img = cv2.resize(img,(500,400))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "Trackerbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackerbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackerbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackerbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackerbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackerbars")


    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([0,0,0])
    upper = np.array([179,121,164])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask= mask)    

    #getting the distance between the two points
    
    
    know_direction()
   
    #imshow 
    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.waitKey(1)
    
    dist = get_dist_van_to_local()
  
    if dist >= 10: #A condição está errada de proposito
        print('VAN ARRIVED')
        break
    tm.sleep(0) #atualiza a cada ## segundos 
