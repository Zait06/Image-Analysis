# coding=utf-8
# @author: Hernández López Ángel Zait
import cv2
import numpy as np
import matplotlib.pyplot as plt

# m=filas n=columnas

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

s=np.ones((m,n,3),dtype=np.uint8)
res=np.ones((m,n,3),dtype=np.int8)

def suma_mat():
    for i in range(m):
		for j in range(n):
			s[i][j]=(0.5*mat1[i][j]+0.5*mat2[i][j])

def resta_mat():
    for i in range(m):
		for j in range(n):
			res[i][j]=(mat1[i][j]-mat2[i][j])

def checa(num):
	efe=num
	if num<0:
		efe=255*(num-mi)/(ma-mi)
	return efe

def nuv_res():
	for i in range(m):
		for j in range(n):
			b,g,r=res[i][j]
			b=checa(b)
			g=checa(g)
			r=checa(r)
			res[i][i]=[b,g,r]

suma_mat()
resta_mat()
ma=np.max(res)
mi=np.min(res)
nuv_res()
# mi1=np.argmax(s)
# ii,jj,cc=np.unravel_index(mi1,s.shape)
# mi=np.min(r)

cv2.imshow('Suma',s)
cv2.imshow('Resta',res)
cv2.waitKey(0)

print("Programa terminado")