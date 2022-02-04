# For run in micropython in ev3 
# import upip
# upip.install('micropython-uasyncio')

"""[settings and imports]
    
video = cv2.VideoCapture(1)

#setting the width and the height
video.set(3,640)
video.set(4,480)
video.set(10,100)

while True:
    sucess, img = video.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("VIDEO", img)    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
"""
"""
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation  = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)
"""
"""
img = cv2.imread("Resources/lena.jpg")

print(img.shape)

imgResize = cv2.resize(img,(400,400))
#use the array for crop the pixels!
imgCropped = img[0:200,200:450]

cv2.imshow("Image original", img)
cv2.imshow("Image", imgResize)
cv2.imshow("Crop image", imgCropped)

cv2.waitKey(0)
"""
"""
img = np.zeros((512,512,3),np.uint8)

#use the last part of the array for collored the img
#fisrt especify the crop part and the color after
#img[200:300,100:300] = 255,0,0

cv2.line(img, (0,0), (img.shape[1],img.shape[0]),(0,255,255),3)
cv2.rectangle(img, (0,0),(250,350),(0,0,255),2)
cv2.circle(img, (400,50), 30, (255,255,0),5)
cv2.putText(img, " OPENCV ",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,150,0),1)


cv2.imshow("image",img)
cv2.waitKey(0)
"""
"""
img = cv2.imread('Resources/cards.jpg')
width,height = 250,350
pst1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pst2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pst1,pst2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))


cv2.imshow("Image",img)
cv2.imshow("Output image", imgOutput)
"""
"""
def empty(a):
    pass

path = 'Resources/lambo.jpg'
    cv2.namedWindow('Trackerbars')
    cv2.resizeWindow('Trackerbars',640,240)
cv2.createTrackbar("Hue Min", "Trackerbars", 0, 179,empty)
cv2.createTrackbar("Hue Max", "Trackerbars", 163, 179,empty)
cv2.createTrackbar("Sat Min", "Trackerbars", 0, 255,empty)
cv2.createTrackbar("Sat Max", "Trackerbars", 255, 255,empty)
cv2.createTrackbar("Val Min", "Trackerbars", 141, 255,empty)
cv2.createTrackbar("Val Max", "Trackerbars", 255, 255,empty)



while True:        
    img = cv2.imread(path)
    img = cv2.resize(img,(500,400))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "Trackerbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackerbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackerbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackerbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackerbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackerbars")
    
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask= mask)    
    cv2.imshow('Original', img)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('Mask', mask)
    cv2.imshow('Image result', imgResult)
    cv2.waitKey(1)
"""
"""
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area) 
        if area > 1:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),1)
            perimeter = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
            print(len(aprox))
            objCor = len(aprox)
            x,y,w,h = cv2.boundingRect(aprox)
            if objCor ==3:objectType = "Triangulo"
            else: objectType = "none"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(imgContour, objectType,
                        (x+(w/2)+10,y+(h/2)-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            
    


path = "Resources/shapes.jpg"
img = cv2.imread(path)

imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)
stack = np.concatenate((imgGray,imgBlur), axis=1)
stack = np.concatenate((stack, imgCanny), axis=1)






cv2.imshow("Stack image", stack)
cv2.imshow('Contours image', imgContour)
cv2.waitKey(0)
"""
#FACE DETECTION! 
"""   
video = cv2.VideoCapture(1)

#setting the width and the height
video.set(3,300)
video.set(4,300)
video.set(10,100)

myColors = [ [5,107,0,90,255,255],
             [133,56,0,159,156,255],
             [57,76,0,100,255,255]
            ]
myColorsValues = [[51,153,255], #bgr
                  [255,0,255],
                  [0,255,0]]
myPoints =[]



def findColor(img,myColors,myColorsValues):
    
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResults,(x,y),10,myColorsValues[count],cv2.FILLED)
        if x !=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1:
            cv2.drawContours(imgResults,cnt,-1,(255,0,0),1)
            perimeter = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
            x,y,w,h = cv2.boundingRect(aprox)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorsValues):
    for point in myPoints:
        cv2.circle(imgResults,(point[0],point[1]),10,myColorsValues[point[2]],cv2.FILLED)
        

while True:
    sucess, img = video.read()
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    imgResults = img.copy()    
    newPoints = findColor(img, myColors,myColorsValues)    
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorsValues)
    cv2.imshow("VIDEO", imgResults)    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

"""
