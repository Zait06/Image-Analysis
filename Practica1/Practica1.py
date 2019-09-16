# coding=utf-8
import cv2
import numpy as np

nombre=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

iman=cv2.imread(nombre)

newnombre=str(raw_input("Ingrese el nombre de la imagen a guardar: "))

cv2.imshow(newnombre,iman)

cv2.waitKey(0)

cv2.imwrite(newnombre,iman)

print("Programa terminado")