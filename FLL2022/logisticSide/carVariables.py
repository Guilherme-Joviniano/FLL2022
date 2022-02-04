

from lib2to3.pytree import type_repr


import cv2
import time as tm
import os
from matplotlib.backend_bases import LocationEvent
import math
import json
from urllib3 import Retry
from geopy.distance import distance
from ipregistry import IpregistryClient
import folium
import urllib
import requests
import ee

# Trigger the authentication flow.
ee.Authenticate()

# Initialize the library.
ee.Initialize()

lst = ee.ImageCollection('MODIS/006/MOD11A1')
# Initial date of interest (inclusive).
i_date = '2017-01-01'

# Final date of interest (exclusive).
f_date = '2020-01-01'

# Selection of appropriate bands and dates for LST.
lst = lst.select('LST_Day_1km', 'QC_Day').filterDate(i_date, f_date)

lst_vis_params = {
    'min': 0, 'max': 40,
    'palette': ['white', 'blue', 'green', 'yellow', 'orange', 'red']}
lst_img = lst.select('LST_Type1').filterDate(i_date).first() 
truckLocation =[
    [-23.861813, -46.414284, '0',6], #0
    [-23.857492, -46.410722,'1',4],
    [-23.852233, -46.405679,'2',2]
                ]

distances = [    
             
]
    


# se 10km 
# lista 
# request 
# range 
# conversar

#this script will get and share the dates about warm, traffic jam and average speed in the road. 
#will use EV3.
# brick is the nod in the net who will get the datas, and the requested is the nod who will receive that data
def empty(a):
    pass

def get_closed_truck(requested,long, lat, id):
    print(f'esse é a distancia desse caminhão até o ponto {requested[3]}')
    for i in truckLocation:
        if i == requested or i[3] >= requested[3]:
            pass
        else:
            
            value = i[0], i[1]
            requestedValue = long,lat
            dist = distance(value, requestedValue)
            distances.append(dist)
            distances.append(i[2])
            
     
    try:    
        low = distances[0]
    except IndexError:
        print('IndexError Não existe nenhum caminhão a frente deste, infelizmente não consiguiremos fazer o preview da estrada a frente.')
        return False
    except TypeError:
        print('TypeError Não existe nenhum caminhão a frente deste, infelizmente não consiguiremos fazer o preview da estrada a frente.')
        return False
    count = 1
    NumberOfTrucks = len(distances)
    for i in range(0,2):
        if i % 2 == 0: 
            print(i)
            value = distances[i]
            if value < low:
                low = value
                count = i+1
   
    closedID = distances[count] 
        
        
    return closedID
    
    



def get_traffic_value(requested):
    
    path = f"carImages/roadimage_caminhao_0{requested}.jpg" 
   
    print(path)
    frame_with_traffic = cv2.imread(path)
    frame_without_traffic = cv2.imread('roadimage_non_traffic.jpg')
    colorProfile = (0,0,255) #BGR\
    TRAFFIC_COUNTER = ""
    timeout = tm.time() + 10
    while True:
        #img = cv2.rotate(img, cv2.)  #turn the video
        mask = cv2.Canny(frame_with_traffic,400,400)
        
        cv2.imwrite('carImages/RoadPicuture1.jpg', mask)
        
        Traffic_value = cv2.countNonZero(mask)
        
        #Divide the scale of traffic percent in 5 parts with differents colors degrees
        #BGR
        print(Traffic_value)
        if Traffic_value <= 900: TRAFFIC_COUNTER = '#CAF0F8'
        if Traffic_value > 4000 and Traffic_value <= 8000: TRAFFIC_COUNTER = '#90E0EF'
        if Traffic_value > 8000 and Traffic_value <= 12000: TRAFFIC_COUNTER = '#00B4D8'
        if Traffic_value > 12000 and Traffic_value <= 16000: TRAFFIC_COUNTER =  '#0077B6'
        if Traffic_value > 16000 : TRAFFIC_COUNTER = '#03045E'
        print(TRAFFIC_COUNTER) 
        
        #if tm.time() > timeout: 
         #   cv2.destroyAllWindows() 
          #  break 
        cv2.imshow('Cars detection', mask)
        cv2.imshow('Original1', frame_with_traffic)
        cv2.imshow('Original2', frame_without_traffic)

    
        if cv2.waitKey(1) & 0xFF ==ord('q'): 
            break 
        if tm.time() > timeout: 
            cv2.destroyAllWindows() 
            break 
        
        return TRAFFIC_COUNTER


        #Close 
     
    #setting the width and the height

 
 
#def get_average_speed_in_road(brick, requested):
    


""
    


#def final_report(brick):
    # average value of the truck travel. who will go to a csv file.
def add_ee_layer(self, ee_image_object, vis_params, name):
    """Adds a method for displaying Earth Engine image tiles to folium map."""
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles=map_id_dict['tile_fetcher'].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        overlay=True,
        control=True
    ).add_to(self)
def get_map_report():
    
    m = folium.Map(location = [truckLocation[0][0],truckLocation[0][1]],zoom_start= 15, )
    for i in range(0,len(truckLocation)):
        folium.CircleMarker(
            radius=100,
            location=[truckLocation[i][0],truckLocation[i][1]],
            popup= 'Caminhão_id_'+truckLocation[i][2] +' I can add somes like temperature and average speed.',
            color= get_traffic_value(requested=i),
            fill=True,
        ).add_to(m)
    map.add_ee_layer(lst_img, lst_vis_params, 'Land Superfice')

# Add a layer control panel to the map.
    map.add_child(folium.LayerControl())

  
    m.save('index.html')
    


get_map_report()
closedID = get_closed_truck(truckLocation[0],truckLocation[0][0], truckLocation[0][1], truckLocation[0][2])
print(f'O caminhão mais proximo é o caminhão {closedID}')