import cv2 
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('FindingWeapons\cascade.xml')  #classifying file
camera = cv2.VideoCapture(0)  #camera 

firstFrame = None
gun_exists = None

while True:
    ret, frame = camera.read()

    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize =(100,100))

    if len(gun)>0:
        gun_exists = True

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)
        roi_gray = gray[y : y + h, x: x + w]
        roi_color = frame[y : y + h, x: x + w]
    
    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)

    if gun_exists:
        print("Weapon")
    
    else:
        print("Not a Weapon")
        

    key = cv2.waitKey(1) &0xff
    if key == ord('q'):
        break
     
camera.release()
cv2.destroyAllWindows()
