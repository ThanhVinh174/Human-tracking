import cv2
import numpy as np
import random
cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame,1)
    first_ponit = [random.randint(200,1000),random.randint(300,2000)]
    second_point = [random.randint(300,2000),random.randint(100,1000)]
    cv2.line(frame,first_ponit,second_point,[0,255,100],2)
    cv2.rectangle(frame,[20,10],[200,300],[255,0,0],5)
    cv2.putText(frame,"This is a rectangular",(0,300),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(255,0,0),thickness=3)
    cv2.circle(frame,[20,10],50,[200,200,200])
    print(frame)
    # cv2.imshow('Frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()