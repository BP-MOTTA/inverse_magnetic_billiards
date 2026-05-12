
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPOS ANTIPARALELOS')
Bin,Bout = 10,1
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
file2 = open('unfolded.dat',"w")
for i in range(10):
        #print('Iteracion',i)
        #print('==>SALIDA')
        A1 = P
        centro = centroCirc(P,v,Bin)
        #print('CENTRO SALIDA',centro[0],centro[1])
        #plt.plot(centro[0],centro[1],'r.')
        P = pointOut(centro,P,Rin) #punto salida
        #print('PUNTO SALIDA',P)
        v = veloOut(P,centro)
        #print('VELOCIDAD SALIDA',v)
        plotArc(A1,P,centro,Rin,'blue')
        ###############################
        #print('==>INGRESO')
        A1 = P
        centro = centroCircOut(P,v,Bout)
        #print('CENTRO INGRESO',centro[0],centro[1])
        #plt.plot(centro[0],centro[1],'r.')
        P = pointOut(centro,P,Rout) #punto salida
        #print('PUNTO INGRESO',P)
        v = -1*veloOut(P,centro) ### ---- GARANTIZAR GIRO HORARIO/ANTIHORARIO
        #print('VELOCIDAD INGRESO',v)
        plotArc(P,A1,centro,Rout,'blue')
        ##### GUARDAR DATA S Y UNFOLDED
        file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
        file2.write(str(i+P[0])+"\t"+str(i+P[1])+"\n")
        
#plt.arrow(xi,yi,vxi,vyi,head_width=0.05,width=0.03,color='black')
#plt.savefig('plot')
plt.show()
