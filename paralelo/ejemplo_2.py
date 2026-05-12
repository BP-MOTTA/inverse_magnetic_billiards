'''
EJEMPLO DE DOS TRAYECTORIAS LIGERAMENTE DIFERENTES
'''
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPOS PARALELOS')
Bin,Bout = 10,1
Rin,Rout = 1/Bin,1/Bout

#PARTICULA 1
x1,y1 = 0.13 , 0 #ubicación inicial
xi1,yi1=x1,y1
P1 = np.array([x1,y1])
vx1,vy1 = np.cos(np.deg2rad(45.0)),np.sin(np.deg2rad(45.0)) #velocidad inicial
vxi1,vyi1=vx1,vy1
v1 = np.array([vx1,vy1])

#PARTICULA 2
x2,y2 = 0.13 , 0 #ubicación inicial
xi2,yi2=x2,y2
P2 = np.array([x2,y2])
vx2,vy2 = np.cos(np.deg2rad(40.0)),np.sin(np.deg2rad(40.0)) #velocidad inicial
vxi2,vyi2=vx2,vy2
v2 = np.array([vx2,vy2])


print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial 1:',P1)
print('Velocidad inicial 1:',v1)
print('Posición inicial 1:',P2)
print('Velocidad inicial 1:',v2)
#plt.title('Billar Magnético')
plt.grid()
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.plot(x1,y1,'go')
plt.arrow(xi1,yi1,vx1/10,vy1/10,width=0.01)
plt.plot(x2,y2,'go')
plt.arrow(xi2,yi2,vx2/10,vy2/10,width=0.01)

plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
file1 = open('sdata.dat',"w")

for i in range(3):
		### INTERIOR ###
        A11 = P1
        centro1 = centroCirc(P1,v1,Bin)
        P1 = pointOut(centro1,P1,Rin)
        v1 = veloOut(P1,centro1)
        plotArc(A11,P1,centro1,Rin,'b')
        
        A12 = P2
        centro2 = centroCirc(P2,v2,Bin)
        P2 = pointOut(centro2,P2,Rin)
        v2 = veloOut(P2,centro2)
        plotArc(A12,P2,centro2,Rin,'r')
        
        ###############################
        ### EXTERIOR ###

        A11 = P1
        centro1 = centroCircOut(P1,v1,Bout)
        P1 = pointOut(centro1,P1,Rout) 
        v1 = 1*veloOut(P1,centro1) 
        plotArc(P1,A11,centro1,Rout,'b')
        
        A12 = P2
        centro2 = centroCircOut(P2,v2,Bout)
        P2 = pointOut(centro2,P2,Rout) 
        v2 = 1*veloOut(P2,centro2) 
        plotArc(P2,A12,centro2,Rout,'r')
        ##### GUARDAR DATA
        #file1.write(str(sDistance(P1))+"\t"+str(np.rad2deg(sThetaAngle(P1,v1)))+"\n")
           
plt.show()
