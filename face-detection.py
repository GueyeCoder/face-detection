#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cv2 as cv

## chargger les classificateurs en cascade pre-entraines
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

##Charger les images
img = cv.imread('dan.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Execution de la detection de visage
faces = face_cascade.detectMultiScale(gray, 1.1, 3)

# Affichage des visages
for face in faces:
    print(face)
