'''
EJEMPLO 3: REALIZA UN SCRIPT PARA GENERAR MUCHAS IMAGENES PARA UNIRLAS
EN UN VIDEO PARA UNOS CAMPOS PARALELOS DADOS
'''
import numpy as np
from magnetic import *
import matplotlib.pyplot as plt
import os
#######
def plotArc(A1,A2,centro,R):
        '''
        Graficar arco de circunferencia
        '''
        #hit = P
        #A2 = hit
        #para A
        thetaA1 = thetaAngle(np.array([A1[0]-centro[0],A1[1]-centro[1]]))
	#print('angulo 1 punto A',np.rad2deg(thetaA1))
	#para B
        thetaA2 = thetaAngle(np.array([A2[0]-centro[0],A2[1]-centro[1]]))
	#print('angulo 2 punto B',np.rad2deg(thetaA2))
	
        if thetaA1 < thetaA2:
		#theta = np.linspace(0,thetaB-thetaA,num=10)	
                thetaList = np.linspace(thetaA1,thetaA2,num=20)
        else: #thetaA > thetaB
                thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=20)  
	#theta = np.linspace(0,thetaB-thetaA,num=10)
	#print(np.rad2deg(thetaList))
	#R = np.matrix([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
        curveX = R*np.cos(thetaList)+centro[0]
        curveY = R*np.sin(thetaList)+centro[1]
        #plt.plot(curveX,curveY,color = 'b', linewidth=0.5,alpha=0.6)
        curve = [curveX,curveY]
        return curve        

########################
#Parámetros de entrada #
#######################
print('BIENVENIDO AL BILLAR INVERSO CON CAMPO MAGNETICO INTERIOR')
print('CAMPO MAGNETICO PARALELO')
Bin,Bout = 1,2
Rin,Rout = 1/Bin,1/Bout

#file1 = open('sdata.dat',"a")
phase = np.loadtxt('sdata.dat')


fig, (ax1, ax2) = plt.subplots(1, 2)

ax2.plot(phase[:,0],phase[:,1],'r,')

for angle in np.arange(2,179,2):
	fig.suptitle(r'$B_{in}=1$'+' '+r'$B_{out}=2$'+' '+r'$\theta_{o}$='+str(angle)+'º')
	x,y = 0.8 , 0.0 #ubicación inicial
	P = np.array([x,y])

	
	vx,vy = np.cos(np.deg2rad(angle)),np.sin(np.deg2rad(angle)) #velocidad inicial
	v = np.array([vx,vy])
	P_init,v_init=P,v
	print('angle',angle)
	#print('Campo Magnetico interior:',Bin,Rin)
	#print('Campo Magnetico exterior:',Bout,Rout)
	#print('Posición inicial:',P)
	#print('Velocidad inicial:',v)
	#plt.title(r'$B_{in}=1$ $B_{out}=3$ $\theta=$'+str(angle))
	
	ax1.set_xlim(-2,3)
	ax1.set_ylim(-2,3)
	ax1.plot(x,y,'go')
	ax1.plot([0,1,1,1,0,0],[0,0,1,1,1,0],linewidth=2,color='red')
	ax1.arrow(P[0],P[1],vx/10,vy/10,color='r',width=0.05)
	#file1 = open('sdata.dat',"a")
	#file2 = open('unfolded.dat',"w")

	for i in range(200):
		#print('Iteracion',i)
		#print('SALIDA')
		A1 = P
		centro = centroCirc(P,v,Bin)
		P = pointOut(centro,P,Rin) #punto salida
		#print('PUNTO SALIDA',P)
		v = veloOut(P,centro)
		#print('VELOCIDAD SALIDA',v)
		#plotArc(A1,P,centro,Rin)
		curveResult = plotArc(A1,P,centro,Rin)
		ax1.plot(curveResult[0],curveResult[1],'b', linewidth=0.5,alpha=0.6)
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
		curveResult = plotArc(A1,P,centro,Rout)
		ax1.plot(curveResult[0],curveResult[1],'b', linewidth=0.5,alpha=0.2)
		#print(sDistance(P),v,np.rad2deg(sThetaAngle(P,v)))
		##### GUARDAR DATA S Y UNFOLDED
		#file1.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
		file_temp = open('temp.txt',"a")
		file_temp.write(str(sDistance(P))+"\t"+str(np.rad2deg(sThetaAngle(P,v)))+"\n")
		#file2.write(str(i+P[0])+"\t"+str(i+P[1])+"\n")
	ax1.arrow(P_init[0] ,P_init[1] ,v_init[0]/10,v_init[1]/10,color='k',width=0.05)
	phaseTemp = np.loadtxt('temp.txt')
	ax2.plot(phaseTemp[:,0],phaseTemp[:,1],'k.')
	
	fig.savefig('plot'+str(angle).zfill(3)+'.png')
	os.remove("temp.txt")
	ax1.cla()
	ax2.cla()
	ax2.plot(phase[:,0],phase[:,1],'r,')
	#fig.show()
	#plt.clf()

#EJECUTAR ffmpeg PARA HACER EL VIDEO.	
os.system("ffmpeg -framerate 2 -pattern_type glob -i '*.png'   -c:v libx264 -pix_fmt yuv420p out4.mp4")    

