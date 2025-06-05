#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2 as cv 
import sys


face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")


img = cv.imread('brad-angelina.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 3)

if len(faces) != 2:
    sys.exit("Deux visages requises")


x1, y1, w1, h1 = faces[0]
x2, y2, w2, h2 = faces[1]


face1 = img[y1:y1+h1, x1:x1+w1]
face2 = img[y2:y2+h2, x2:x2+w2]


face1 = cv.resize(face1, (w2,h2))
face2 = cv.resize(face2, (w1, h1))


img[y2:y2+h2, x2:x2+w2] = face1
img[y1:y1+h1, x1:x1+w1] = face2

cv.imshow("Echange", img)
cv.waitKey(0)
cv.destroyAllWindows()


