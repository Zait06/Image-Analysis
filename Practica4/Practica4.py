# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

nombre=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

iman=cv2.imread(nombre)

matriz=np.array(iman)
rojo=np.array(iman)
azul=np.array(iman)
verde=np.array(iman)

m,n,canal=iman.shape


def rojito():
	for i in range(m):
		for j in range(n):
			b,g,r=matriz[i][j]
			rojo[i][j]=[0,0,r]

def azulito():
	for i in range(m):
		for j in range(n):
			b,g,r=matriz[i][j]
			azul[i][j]=[b,0,0]

def verdecito():
	for i in range(m):
		for j in range(n):
			b,g,r=matriz[i][j]
			verde[i][j]=[0,g,0]

rojito()
azulito()
verdecito()
cv2.imshow('Color',iman)
cv2.imshow('Rojo',rojo)
cv2.imshow('Azul',azul)
cv2.imshow('Verde',verde)
#cv2.imwrite("grises.jpg",aux_mat1)

cv2.waitKey(0)


print("Hernández López Ángel Zait")