# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Imagen():
    def __init__(self,h,w,mat,matgris):
        self.alto=h                                    # Altura de la imagen
        self.ancho=w                                   # Ancho de la imagen
        self.matriz=mat                                # Imagen
        self.grises=matgris                            # Escala de grises

class Filtro():
    def __init__(self,h,w):
        self.alto=h+2                                             # Altura de la imagen
        self.ancho=w+2                                            # Ancho de la imagen
        self.matriz=np.zeros((h+2,w+2),dtype=np.uint8)            # Imagen
        self.promedio=np.zeros((h,w),dtype=np.uint8)
        self.gaussiano=np.zeros((h,w),dtype=np.uint8)
        self.maskGauss=np.ones((3,3),dtype=np.uint8)
        self.maskGauss[0][1]=2; self.maskGauss[1][0]=2; self.maskGauss[1][2]=2;
        self.maskGauss[2][1]=1; self.maskGauss[1][1]=4;

    
    def filtProm(self):
        for i in range(0,self.alto-2):
            for j in range(0,self.ancho-2):
			    self.promedio[i][j]=self.__promedio(self.matriz[i:i+3,j:j+3])

    def filtGauss(self):
        for i in range(0,self.alto-2):
            for j in range(0,self.ancho-2):
			    self.gaussiano[i][j]=self.__convolucion(self.matriz[i:i+3,j:j+3],self.maskGauss,16)
    
    def __promedio(self,a):
        su=0
        for i in range(3):
            for j in range(3):
                su=a[i][j]+su
        return round((1.0/9.0)*su)

    def __convolucion(self,a,b,c):
        sz=0
        for i in range(3):
            for j in range(3):
                sz=sz+(float((a[i][j])*(b[i][j])/c))
        return int(sz)

nom=str(raw_input("Ingrese el nombre de la imagen: "))
iman1=cv2.imread(nom)
f,c,canal=iman1.shape
iman1gris=cv2.imread(nom,cv2.IMREAD_GRAYSCALE)

# Creamos un objeto tipo imagen
imagen1=Imagen(f,c,iman1,iman1gris)
asd=imagen1.grises

# Creamos un objeto tipo filtro
filtro1=Filtro(f,c)
filtro1.matriz[1:f+1,1:c+1]=asd

filtro1.filtProm()
#filtro1.filtGauss()

cv2.imshow('Imagen',filtro1.promedio)
#cv2.imshow('Filtro Gaussiano',filtro1.gaussiano)
cv2.waitKey(0)