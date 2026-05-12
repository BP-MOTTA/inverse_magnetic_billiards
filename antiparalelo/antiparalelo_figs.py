'''
EL SIGUIENTE CÓDIGO PERMITE GRAFICAR UNA TRAYECTORIA PARA CAMPOS MAGNÉTICOS INVERSOS.
PROPORCIONA COMO RESULTADO LOS DATOS DE S Y THETA PARA EL ESPACIO DE FASES
Y EL GRÁFICO DE LA TRAYECTORIA
'''
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt

# TAMAÑO DE LA LETRA
plt.rcParams.update({'font.size': 16})
plt.figure(figsize=(7,7)) #figura 600x600 pixeles


########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPOS ANTIPARALELOS')
Bin,Bout = 1,10
Rin,Rout = 1/Bin,1/Bout

x,y = 0.1 , 0 #ubicación inicial
xi,yi=x,y
P = np.array([x,y])
vAngle = 45
vx,vy = np.cos(np.deg2rad(vAngle)),np.sin(np.deg2rad(vAngle)) #velocidad inicial
vxi,vyi=vx,vy
v = np.array([vx,vy])

print('Campo Magnetico interior:',Bin)
print('Campo Magnetico exterior:',Bout)
print('Posición inicial:',P)
print('Velocidad inicial:',v)
#plt.title('Billar Magnético')
plt.grid()
plt.xlim(-0.2,1.2)
plt.ylim(-0.2,1.2)
plt.plot(x,y,'go')
plt.arrow(xi,yi,vx/10,vy/10,width=0.01)

#plt.title(r'$B_{in}=$'+str(Bin)+' '+r'$B_{out}=$'+str(Bout)+' '+r'$\theta_{o}$='+str(vAngle)+r'$ ^{o}$')

plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])
file1 = open('sdata.dat',"w")

for i in range(2):
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
      
          
print('Plot de la trayectoria guardado en trajectory_plot.png')
plt.savefig('trajectory_plot.png')
plt.show()
