# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

nombre=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

umbral=int(raw_input("Ingrese el umbral: "))

iman=cv2.imread(nombre)

matriz=np.array(iman)

m,n,canal=iman.shape

# Escala a grises de la imagen
def binar():
	gris_mat=np.array(iman)
	for i in range(0,m):
		for j in range(0,n):
			b,g,r=matriz[i][j]
			gris_mat[i][j]=checumb((r*0.3)+(g*0.59)+(b*0.11))
	return gris_mat

def checumb(a):
    if a>umbral:
        r=255
    else:
        r=0
    return r

aux_mat1=binar()

cv2.imshow('Binarización',aux_mat1)
#cv2.imwrite("binar.jpg",aux_mat1)

cv2.waitKey(0)

print("Hernández López Ángel Zait")