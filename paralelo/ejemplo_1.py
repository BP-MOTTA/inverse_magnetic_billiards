'''
EL SIGUIENTE CÓDIGO PERMITE GRAFICAR UNA TRAYECTORIA PARA CAMPOS MAGNÉTICOS PARALELOS.
PROPORCIONA COMO RESULTADO LOS DATOS DE S Y THETA PARA EL ESPACIO DE FASES
Y EL GRÁFICO DE LA TRAYECTORIA
'''
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

########################
#Parámetros de entrada #
#######################
print(10*'=')
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPO MAGNETICO PARALELO')
print(10*'=')

Bin = float(input('INGRESE CAMPO MAGNETICO INTERIOR: '))
Bout = float(input('INGRESE CAMPO MAGNETICO EXTERIOR: '))
#Bin,Bout = 10,1
vAngle = 100 # en grados sexagesimales
vAngle= float(input('INGRESE ANGULO INICIAL (EN SEXAGESIMALES):'))
##########################

Rin,Rout = 1/Bin,1/Bout
x,y = 0.5 , 0.0 #ubicación inicial
P = np.array([x,y])

vx,vy = np.cos(np.deg2rad(vAngle)),np.sin(np.deg2rad(vAngle)) #velocidad inicial
v = np.array([vx,vy])
print('====== DATOS INGRESADOS =====')
print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial(angulo):',vAngle)
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.plot(x,y,'go')
plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
print('==============================')
file1 = open('sdata.dat',"w")
#file2 = open('unfolded.dat',"w")

for i in range(10000):
		#INTERIOR
        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin)
        v = veloOut(P,centro)
        plotArc(A1,P,centro,Rin,'r')
        #EXTERIOR
        A1 = P
        centro = centroCirc(P,v,Bout)
        P = pointOut(centro,P,Rout)
        v = veloOut(P,centro)
        plotArc(A1,P,centro,Rout,'r')
        ##### GUARDAR DATA S Y UNFOLDED
        file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")

print('SE MUESTRA EL GRÁFICO DE LA TRAYECTORIA')

plt.show()
