# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

nombre=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

iman=cv2.imread(nombre)

matriz=np.array(iman)

m,n,canal=iman.shape

# Escala a grises de la imagen
def grises():
	gris_mat=np.array(iman)
	for i in range(m):
		for j in range(n):
			b,g,r=matriz[i][j]
			gris_mat[i][j]=((r*0.3)+(g*0.59)+(b*0.11))
	return gris_mat

aux_mat1=grises()
cv2.imshow('Grises',aux_mat1)
#cv2.imwrite("grises.jpg",aux_mat1)

cv2.waitKey(0)


print("Hernández López Ángel Zait")