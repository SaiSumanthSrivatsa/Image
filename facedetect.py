import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
color_image=cv2.imread('my.jpg')
gray_image=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_image,1.1,7)
for (x,y,w,h) in faces:
    cv2.rectangle(color_image,(x,y),(x+w,y+h),(0,255,0),4)
cv2.imshow('Face Detect',color_image)
cv2.waitKey()
cv2.destroyAllWindows()