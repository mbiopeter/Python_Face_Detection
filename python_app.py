import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test4.jpg')
number_of_people = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    number_of_people = number_of_people + 1

print("Number of faces detected: ", number_of_people)
cv2.imshow('img', img)
cv2.waitKey()

cv2.imWrite('face_ddetected.png', img)