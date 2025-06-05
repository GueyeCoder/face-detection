#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import cv2 as cv

## chargger les classificateurs en cascade pre-entraines
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')


##Charger les images
img = cv.imread('obama.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Execution de la detection de visage
faces = face_cascade.detectMultiScale(gray, 1.1, 8)

i = 0
# Affichage des visages
for face in faces:
    x, y, w, h = face
    #dessiner le rectangle sur l'image
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

## Execution de la detection des yeux
eyes = eye_cascade.detectMultiScale(gray, 1.1, 3)

# Affichage des yeux
for (ex, ey, ew, eh) in eyes:
    # dessiner un rectangle autour des yeux sur l'image principale
    cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)


# Affiche image principale
cv.imshow("image principale", img)
cv.waitKey(0)
cv.destroyAllWindows()
