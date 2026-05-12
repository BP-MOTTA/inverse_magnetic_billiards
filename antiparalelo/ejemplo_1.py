'''
EL SIGUIENTE CÓDIGO PERMITE GRAFICAR UNA TRAYECTORIA PARA CAMPOS MAGNÉTICOS INVERSOS.
PROPORCIONA COMO RESULTADO LOS DATOS DE S Y THETA PARA EL ESPACIO DE FASES
Y EL GRÁFICO DE LA TRAYECTORIA
'''
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPOS ANTIPARALELOS')
Bin,Bout = 2,1
Rin,Rout = 1/Bin,1/Bout

x,y = 0.13 , 0 #ubicación inicial
xi,yi=x,y
P = np.array([x,y])
vx,vy = np.cos(np.deg2rad(45.0)),np.sin(np.deg2rad(45.0)) #velocidad inicial
vxi,vyi=vx,vy
v = np.array([vx,vy])

print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial:',v)
#plt.title('Billar Magnético')
plt.grid()
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.plot(x,y,'go')
plt.arrow(xi,yi,vx/10,vy/10,width=0.01)

plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
file1 = open('sdata.dat',"w")

for i in range(10000):
		### INTERIOR ###
        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin)
        v = veloOut(P,centro)
        plotArc(A1,P,centro,Rin,'b')
        ###############################
        ### EXTERIOR ###
        A1 = P
        centro = centroCircOut(P,v,Bout)
        P = pointOut(centro,P,Rout) 
        v = -1*veloOut(P,centro) 
        plotArc(P,A1,centro,Rout,'b')
        ##### GUARDAR DATA
        file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
           
#plt.show()
