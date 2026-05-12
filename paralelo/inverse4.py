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
Bin,Bout = 10,1
vAngle = 100 # en grados sexagesimales
##########################

Rin,Rout = 1/Bin,1/Bout
x,y = 0.6 , 0.0 #ubicación inicial
P = np.array([x,y])

vx,vy = np.cos(np.deg2rad(vAngle)),np.sin(np.deg2rad(vAngle)) #velocidad inicial
v = np.array([vx,vy])
print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial(angulo):',vAngle)
plt.xlim(-2,3)
plt.ylim(-2,3)
plt.plot(x,y,'go')
plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
file1 = open('sdata.txt',"w")
#file2 = open('unfolded.dat',"w")

for i in range(10000):
        #print('Iteracion',i)
        #print('SALIDA')
        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin) #punto salida
        #print('PUNTO SALIDA',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD SALIDA',v)
        plotArc(A1,P,centro,Rin)
        ###############################
        #print('INGRESO')
        A1 = P
        centro = centroCirc(P,v,Bout)
        P = pointOut(centro,P,Rout) #punto salida
        #print('PUNTO INGRESO',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD INGRESO',v)
        #plt.arrow(P[0],P[1],v[0],v[1])
        plotArc(A1,P,centro,Rout)
        #print(sDistance(P),v,np.rad2deg(sThetaAngle(P,v)))
        ##### GUARDAR DATA S Y UNFOLDED
        file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
        #file2.write(str(i+P[0])+"\t"+str(i+P[1])+"\n")

print('Plot de la trayectoria guardado en trajectory_plot.png')
plt.savefig('trajectory_plot.png')
plt.clf()
file1.close()
phaseData = np.loadtxt('sdata.txt')
plt.plot(phaseData[:,0],phaseData[:,1],'r,')
plt.xlim(0,4)
plt.ylim(0,360)
plt.savefig('phase_space.png')
print('Data del espacio de fases guardado en sdata.txt')
print('Plot del espacio de fases guardado en phase_space.png')
#plt.show()

