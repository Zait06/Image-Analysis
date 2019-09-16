# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImagenBinaria():
    def __init__(self,h,w):
        self.alto=h+2                                     # Altura de la imagen
        self.ancho=w+2                                    # Ancho de la imagen
        self.matriz=np.zeros((h+2,w+2),dtype=np.uint8)    # Imagen binaria
        self.dilatada=np.zeros((h+2,w+2),dtype=np.uint8)  # Imagen dilatada
        self.mascara=np.zeros((3,3),dtype=np.uint8)
        self.mascara[0][1]=255; self.mascara[1][0]=255;
        self.mascara[1][2]=255; self.mascara[2][1]=255;
        self.mascara[1][1]=255;

    def dilatacion(self):
        for x in range(0,self.alto-2):
            for y in range(0,self.ancho-2):
                if(self.matriz[x+1][y+1]==255):
                    self.__asignar(x,y)
                else:
                    continue

    def __asignar(self,i,j):
        for s in range(3):
            for t in range(3):
                self.dilatacion[i-s][j-t]=self.mascara[s][t]



nom=str(raw_input("Ingrese el nombre de la imagen: "))
iman1=cv2.imread(nom)
f,c,canal=iman1.shape
iman1gris=cv2.imread(nom,cv2.IMREAD_GRAYSCALE)
media=int(np.mean(iman1gris))
a,iman1bin=cv2.threshold(iman1gris,media,255,cv2.THRESH_BINARY)

# Se crea una imagen binaria
imagen1=ImagenBinaria(f,c)
imagen1.matriz[1:f+1,1:c+1]=iman1bin

# Dilatacion
imagen1.dilatacion()

cv2.imshow('ImagenB',imagen1.matriz)
cv2.waitKey(0)