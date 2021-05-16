# importing cv2
import cv2

# importing os module
import os
cap = cv2.VideoCapture("IsraeliSoldiers.mp4")

counter=0
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow('frame', frame)
    if(counter%5==0):
        filename = "frame"+str(counter)+".jpg"
        cv2.imwrite(filename, frame)
        cv2.imshow('frame', frame)

    counter+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()