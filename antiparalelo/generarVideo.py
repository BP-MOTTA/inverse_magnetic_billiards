'''
EL SIGUIENTE EJEMPLO PERMITE GRAFICAR DOS SUBPLOT, UNO DONDE ESTA LA TRAYECTORIA DE LA PARTÍCULA
Y OTRO CON EL ESPACIO DE FASES. ADEMAS QUE EJECUTA UN COMANDO PARA REALIZAR UN VIDEO
OJO: REQUIERE EL ARCHIVO sdata.dat QUE CORRESPONDE AL ESPACIO DE FASES, PARA OBTENERLO PUEDE
USAR EL SCRIPT ejemplo_1.py QUE PROPORCIONA COMO SALIDA ESOS DATOS.
LA SALIDA DE ESTE EJEMPLO SON LAS IMAGENES DE LAS TRAYECTORIAS CON SU ESPACIO DE FASES Y CON EL VIDEO
CORRESPONDIENTE DE JUNTAR TODAS ESTAS IMAGENES.
'''

import numpy as np
from magnetic import *
import matplotlib.pyplot as plt
import os

def plotArc(A1,A2,centro,R):
        '''
        Graficar arco de circunferencia
        '''
        #para A
        thetaA1 = thetaAngle(np.array([A1[0]-centro[0],A1[1]-centro[1]]))

		#para B
        thetaA2 = thetaAngle(np.array([A2[0]-centro[0],A2[1]-centro[1]]))
	
        if thetaA1 < thetaA2:
                thetaList = np.linspace(thetaA1,thetaA2,num=20)
        else: 
                thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=20)  
	#theta = np.linspace(0,thetaB-thetaA,num=10)

        curveX = R*np.cos(thetaList)+centro[0]
        curveY = R*np.sin(thetaList)+centro[1]
        curve = [curveX,curveY]
        return curve

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPOS ANTIPARALELOS')
Bin,Bout = 2,1
Rin,Rout = 1/Bin,1/Bout

phase = np.loadtxt('sdata.dat')
fig,(ax1,ax2) = plt.subplots(1,2)
ax2.plot(phase[:,0],phase[:,1],'r,')

for angle in np.arange(2,179,2):
    fig.suptitle(r'$B_{in}=$'+str(Bin)+' '+r'$B_{out}=$'+str(Bout)+' '+r'$\theta_{o}=$'+str(angle)+'º')    
    x,y = 0.5 , 0 #ubicación inicial
    P = np.array([x,y])
    vx,vy = np.cos(np.deg2rad(angle)),np.sin(np.deg2rad(angle)) #velocidad inicial
    v = np.array([vx,vy])
    P_init,v_init=P,v
    print(angle)
    ax1.set_xlim(-2,3)
    ax1.set_ylim(-2,3)
    ax1.plot(x,y,'go')


    ax1.plot([0,1,1,1,0,0],[0,0,1,1,1,0])

    for i in range(200):

        A1 = P
        centro = centroCirc(P,v,Bin)
        P = pointOut(centro,P,Rin) #punto salida
        v = veloOut(P,centro)
        curveResult = plotArc(A1,P,centro,Rin)
        ax1.plot(curveResult[0],curveResult[1],'b',linewidth=0.5,alpha=0.6)
        ###############################
        
        A1 = P
        centro = centroCircOut(P,v,Bout)
        P = pointOut(centro,P,Rout) #punto salida
        v = -1*veloOut(P,centro)
        curveResult=plotArc(P,A1,centro,Rout)
        ax1.plot(curveResult[0],curveResult[1],'b',linewidth=0.5,alpha=0.6)
        ##### GUARDAR DATA
        file_temp = open("temp.txt","a")
        file_temp.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")

    ax1.arrow(P_init[0],P_init[1],v_init[0]/10,v_init[1]/10,width=0.05)
    phaseTemp = np.loadtxt('temp.txt')
    ax2.plot(phaseTemp[:,0],phaseTemp[:,1],'k.')
    fig.savefig('plot'+str(angle).zfill(3)+'.png')
    os.remove("temp.txt")
    ax1.cla()
    ax2.cla()
    ax2.plot(phase[:,0],phase[:,1],'r,')
	
#EJECUTAR ffmpeg PARA HACER EL VIDEO.	
os.system("ffmpeg -framerate 2 -pattern_type glob -i '*.png'   -c:v libx264 -pix_fmt yuv420p out4.mp4")    
