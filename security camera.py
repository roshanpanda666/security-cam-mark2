#we are creating 2 frames and the 2nd frame is need to in low FPS 
#and when ever any motion detects it will make some noise because the fps of the 2nd frame is low
#so opec cv has a function named diff 
#if any diffrance camera spotted it will crate a retangle 
#and when the rectangle detect the winsound module make some noise 
i=0
import cv2#imported the module
import winsound#the beep sound module
import pyttsx3

pwd=input("password-->")
        
if (pwd=="roshan"):
    engine = pyttsx3.init()
    engine.say("executing camera ")
    engine.runAndWait()

else:
    print("password is incorect ")
    ok=input()
    exit()



camnum=int(input("enter the cam number"))
cam=cv2.VideoCapture(camnum)#defining the camera
while cam.isOpened():  #while camera is open
    ret,frame1=cam.read()  #crete a frame
    ret,frame2=cam.read()  #create a second frame
    
    
    

    diff=cv2.absdiff(frame1,frame2)  #if any difference dected
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY) #converting RGB color to gray 
    blur=cv2.GaussianBlur(gray,(5, 5),0) #creating some blur effect because the differenc easily visible
    _, thresh=cv2.threshold(blur, 20, 255,cv2.THRESH_BINARY) #define how fps blur you want

    dilated=cv2.dilate(thresh, None, iterations=3)
    contours,_ =cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #creating a rectangle
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #if rectangle get detected 
        i=i+1
        print("movement detected "+str(i))
        
        winsound.Beep(5000, 200)#makes beeps
        
    if cv2.waitKey(10)==ord('q'):#if q is press the camera will be closed
        break#and break the camera loop
    cv2.imshow('cam1',frame1)#showing the frames


