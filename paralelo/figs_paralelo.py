import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

# TAMAÑO DE LA LETRA
plt.rcParams.update({'font.size': 16})
plt.figure(figsize=(7,7)) #figura 600x600 pixeles


########################
#Parámetros de entrada #
#######################
print(10*'=')
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPO MAGNETICO PARALELO')
print(10*'=')
Bin,Bout = 1,10
vAngle = 70 # en grados sexagesimales
##########################

Rin,Rout = 1/Bin,1/Bout
x,y = 0.7 , 0.0 #ubicación inicial
P = np.array([x,y])

vx,vy = np.cos(np.deg2rad(vAngle)),np.sin(np.deg2rad(vAngle)) #velocidad inicial
v = np.array([vx,vy])
print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial(angulo):',vAngle)
plt.grid()
plt.xlim(-0.2,1.2)
plt.ylim(-0.2,1.2)
plt.plot(x,y,'go')
plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
#file1 = open('sdata.txt',"w")
#file2 = open('unfolded.dat',"w")	

#plt.title(r'$B_{in}=$'+str(Bin)+' '+r'$B_{out}=$'+str(Bout)+' '+r'$\theta_{o}$='+str(vAngle)+r'$ ^{o}$')

plt.arrow(x,y,vx/5,vy/5,head_width=0.05,width=0.01,color='black')

for i in range(2):
        #print('Iteracion',i)
        #print('SALIDA')
        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin) #punto salida
        #print('PUNTO SALIDA',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD SALIDA',v)
        plotArc(A1,P,centro,Rin,cline='k')
        ###############################
        #print('INGRESO')
        A1 = P
        centro = centroCirc(P,v,Bout)
        P = pointOut(centro,P,Rout) #punto salida
        #print('PUNTO INGRESO',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD INGRESO',v)
        #plt.arrow(P[0],P[1],v[0],v[1])
        plotArc(A1,P,centro,Rout,cline='k')
        #print(sDistance(P),v,np.rad2deg(sThetaAngle(P,v)))
        ##### GUARDAR DATA S Y UNFOLDED
        #file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
        #file2.write(str(i+P[0])+"\t"+str(i+P[1])+"\n")

print('Plot de la trayectoria guardado en trajectory_plot.png')
plt.savefig('trajectory_plot.png')
#plt.clf()
#file1.close()
#phaseData = np.loadtxt('sdata.txt')
#plt.plot(phaseData[:,0],phaseData[:,1],'r,')
#plt.xlim(0,4)
#plt.ylim(0,360)
#plt.savefig('phase_space.png')
#print('Data del espacio de fases guardado en sdata.txt')
#print('Plot del espacio de fases guardado en phase_space.png')
plt.show()

