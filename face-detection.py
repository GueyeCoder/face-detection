#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2 as cv

## chargger les classificateurs en cascade pre-entraines
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

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
    
    # Extraire les visages de l'image principale
    face =img[y:y+h, x:x+w]
    cv.imshow('face{}'.format(i), face)
    i += 1

# Affiche image principale
cv.imshow("image principale", img)
cv.waitKey(0)
cv.destroyAllWindows()