# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Imagen():
    def __init__(self,h,w,mat,matgris):
        self.alto=h                                     # Altura de la imagen
        self.ancho=w                                    # Ancho de la imagen
        self.matriz=mat                                 # Imagen
        self.grises=matgris                             # Escala de grises
        self.despalzado=np.zeros((h,w),dtype=np.uint8)  # Imagen desplazada
        self.comprimido=np.zeros((h,w),dtype=np.uint8)  # Imagen comprimida
        self.expan=np.zeros((h,w),dtype=np.uint8)       # Imagen expandida
        self.rmax=float(np.max(self.grises))
        self.rmin=float(np.min(self.grises))

    def desplazamiento(self):                           # Desplazamiento del histograma
        for i in range(self.alto):
            for j in range(self.ancho):
                self.despalzado[i][j]=self.grises[i][j]+dez

    def compresion(self):
        for i in range(self.alto):
            for j in range(self.ancho):
                self.comprimido[i][j]=int((((cmax-cmin)/(self.rmax-self.rmin))*(float(self.grises[i][j])-self.rmin))+cmin)


    def expansion(self):
        for i in range(self.alto):
            for j in range(self.ancho):
                self.expan[i][j]=int(round((((float(self.grises[i][j])-self.rmax)/(self.rmax-self.rmin))*(big-small))+small))


nom=str(raw_input("Ingrese el nombre de la imagen: "))
dez=int(raw_input("Desplazamiento [-100,100]: "))
cmax=float(raw_input("Contraccion maxima [0,255]: "))
cmin=float(raw_input("Contraccion minima [0,255]: "))
big=float(raw_input("Expansion maxima [0,255]: "))
small=float(raw_input("Expansion minima [0,255]: "))
iman1=cv2.imread(nom)
iman1gris=cv2.imread(nom,cv2.IMREAD_GRAYSCALE)
f,c,canal=iman1.shape
imagen1=Imagen(f,c,iman1,iman1gris)

imagen1.desplazamiento()
imagen1.compresion()
imagen1.expansion()


cv2.imshow('Imagen',imagen1.grises)
cv2.imshow('Desplazamiento',imagen1.despalzado)
cv2.imshow('Contraccion',imagen1.comprimido)
cv2.imshow('Expansion',imagen1.expan)
cv2.waitKey(0)