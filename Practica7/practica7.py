# coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Histograma y sus propiedades")
nombre=str(raw_input("Ingrese el nombre de la imagen con su extención: "))

iman=cv2.imread(nombre)
matriz=np.array(iman)
f,c,canal=iman.shape    # f=filas  c=columnas
cantpix=np.zeros((256),dtype=np.uint8)   # Vector para contar los pixeles
gris_mat=cv2.imread(nombre,cv2.IMREAD_GRAYSCALE)

# Cuenta el numero de pixeles
def contar():
    for i in range(f):
        for j in range(c):
            ind=gris_mat[i][j]
            cantpix[ind]=cantpix[ind]+1

def histograma():
    plt.title('Histograma')
    histo=cv2.calcHist([gris_mat],[0],None,[256],[0,256])
    plt.plot(histo,color='black')
    plt.show()

def media():
    suma=0
    for i in range(255):
        suma=suma+float((cantpix[i]*i)/float(f*c))
    return suma

def varianza():
    suma=0
    for i in range(255):
        suma=suma+(float(pow((i-med),2))*float(cantpix[i])/(f*c))
    return suma

def asimetria():
    suma=0
    for i in range(255):
        suma=suma+(float(pow((i-med),3))*float(cantpix[i])/(f*c))
    return suma

def energia():
    suma=0
    for i in range(255):
        suma=suma+(pow(float(cantpix[i])/(f*c),2))
    return suma

contar()
cv2.imshow('Imagen',gris_mat)

med=media()
var=varianza()
ener=energia()
asi=asimetria()
print('Media: '+str(med))
print('Varianza: '+str(var))
print('Asimetría: '+str(asi))
print('Energía: '+str(ener))
histograma()
cv2.waitKey(0)

#print("\nPrograma terminado")