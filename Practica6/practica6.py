# coding=utf-8
# @author: Hernández López Ángel Zait
import cv2
import numpy as np
import matplotlib.pyplot as plt

# m=filas n=columnas

print("Operadores lógicos\n")
nom1=str(raw_input("Ingrese el nombre de la imagen con su extención: "))
nom2=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

iman1=cv2.imread(nom1)
iman2=cv2.imread(nom2)

m1,n1,canal1=iman1.shape
m2,n2,canal2=iman2.shape
mat1=np.array(iman1)
mat2=np.array(iman2)

m=min(m1,m2)
n=min(n1,n2)

imnot=np.ones((m1,n1,3),dtype=np.uint8)
imand=np.ones((m,n,3),dtype=np.uint8)
imor=np.ones((m,n,3),dtype=np.uint8)

# Operador not
def comp_not():
    for i in range(m1):
		for j in range(n1):
			imnot[i][j]=[255,255,255]-mat1[i][j]

# Operador and
def comp_and():
    for i in range(m):
		for j in range(n):
			imand[i][j]=mat1[i][j] & mat2[i][j]

# Operador or
def comp_or():
    for i in range(m):
		for j in range(n):
			imor[i][j]=mat1[i][j] | mat2[i][j]

comp_not()
comp_and()
comp_or()

cv2.imshow('Operador not',imnot)
cv2.imshow('Operador and',imand)
cv2.imshow('Operador or',imor)

cv2.waitKey(0)

print("Programa terminado")