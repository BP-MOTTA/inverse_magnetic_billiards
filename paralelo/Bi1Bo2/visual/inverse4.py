import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPO MAGNETICO PARALELO')
Bin,Bout = 1,2
Rin,Rout = 1/Bin,1/Bout

x,y = 0.5 , 0.0 #ubicación inicial
P = np.array([x,y])
vx,vy = np.cos(np.deg2rad(10.0)),np.sin(np.deg2rad(10.0)) #velocidad inicial
v = np.array([vx,vy])
print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial:',v)
plt.grid()
plt.xlim(-0.4,1.4)
plt.ylim(-0.4,1.4)
plt.plot(x,y,'go')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0],'k',linewidth=3)
file1 = open('sdata.dat',"w")
#file2 = open('unfolded.dat',"w")

for i in range(1000):
        #print('Iteracion',i)
        #print('SALIDA')
        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin) #punto salida
        #print('PUNTO SALIDA',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD SALIDA',v)
        #plotArc(A1,P,centro,Rin)
        ###############################
        #print('INGRESO')
        A1 = P
        centro = centroCirc(P,v,Bout)
        P = pointOut(centro,P,Rout) #punto salida
        #print('PUNTO INGRESO',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD INGRESO',v)
        #plt.arrow(P[0],P[1],v[0],v[1])
        #plotArc(A1,P,centro,Rout)
        #print(sDistance(P),v,np.rad2deg(sThetaAngle(P,v)))
        ##### GUARDAR DATA S Y UNFOLDED
        file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
        #file2.write(str(i+P[0])+"\t"+str(i+P[1])+"\n")
        
#plt.savefig('plot.png')
#plt.show()

