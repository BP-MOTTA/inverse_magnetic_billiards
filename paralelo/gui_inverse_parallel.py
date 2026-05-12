import numpy as np
import math 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox
from matplotlib.patches import Rectangle
from magnetic import *

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25,bottom=0.25)

Bin,Bout = 10,1
Rin,Rout = 1/Bin,1/Bout

x,y = 0.6 , 0.0 #ubicación inicial
P = np.array([x,y])

theta_i = 152
theta = np.deg2rad(theta_i)

vx,vy = np.cos(theta),np.sin(theta)
v = np.array([vx,vy])
plt.plot(x,y,'go')
ax.set_xlim(-2,3)
ax.set_ylim(-2,3)

plt.plot([0,1,1,1,0,0],[0,0,1,1,1,0])

for i in range(100):
	A1 = P
	centro = centroCirc(P,v,Bin)
	P = pointOut(centro,P,Rin) #punto salida
	v = veloOut(P,centro)
	#####################
	# script plotting inside
	#plotArc(A1,P,centro,Rin)
	thetaA1 = thetaAngle(np.array([A1[0]-centro[0],A1[1]-centro[1]]))
	thetaA2 = thetaAngle(np.array([P[0]-centro[0],P[1]-centro[1]]))
	if thetaA1 < thetaA2:
	#theta = np.linspace(0,thetaB-thetaA,num=10)	
		thetaList = np.linspace(thetaA1,thetaA2,num=20)
	else: #thetaA > thetaB
		thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=20)  

	curveXin = Rin*np.cos(thetaList)+centro[0]
	curveYin = Rin*np.sin(thetaList)+centro[1]
	lin, = plt.plot(curveXin,curveYin,color = 'b', linewidth=0.5)
	###############################
	A1 = P
	centro = centroCirc(P,v,Bout)
	P = pointOut(centro,P,Rout) #punto salida
	v = veloOut(P,centro)
	#script plotting outside
	#plotArc(A1,P,centro,Rout)
	thetaA1 = thetaAngle(np.array([A1[0]-centro[0],A1[1]-centro[1]]))
	thetaA2 = thetaAngle(np.array([P[0]-centro[0],P[1]-centro[1]]))
	if thetaA1 < thetaA2:
	#theta = np.linspace(0,thetaB-thetaA,num=10)	
		thetaList = np.linspace(thetaA1,thetaA2,num=20)
	else: #thetaA > thetaB
		thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=20)  

	curveXout = Rout*np.cos(thetaList)+centro[0]
	curveYout = Rout*np.sin(thetaList)+centro[1]
	lout, = plt.plot(curveXout,curveYout,color = 'b', linewidth=0.5)
	
	
	
axAngle = plt.axes([0.25,0.15,0.65,0.03],facecolor='green') #slider tiempo
AngleSlider = Slider(axAngle,'Angle: ',1,179,valinit=10,valstep=1) 

def update(val):
	AngleVar = AngleSlider.val
	print('ANGLE:',AngleVar)
	vxVar,vyVar = np.cos(AngleVar),np.sin(AngleVar)
	vVar = np.array([vxVar,vyVar])
	for i in range(100):
		A1Var = P
		centroVar = centroCirc(P,vVar,Bin)
		PVar = pointOut(centroVar,P,Rin) #punto salida
		vVar = veloOut(PVar,centroVar)
		#####################
		# script plotting inside
		#plotArc(A1,P,centro,Rin)
		thetaA1Var = thetaAngle(np.array([A1Var[0]-centroVar[0],A1Var[1]-centroVar[1]]))
		thetaA2Var = thetaAngle(np.array([PVar[0]-centroVar[0],PVar[1]-centroVar[1]]))
		if thetaA1Var < thetaA2Var:
		#theta = np.linspace(0,thetaB-thetaA,num=10)	
			thetaListVar = np.linspace(thetaA1Var,thetaA2Var,num=20)
		else: #thetaA > thetaB
			thetaListVar = np.linspace(thetaA1Var,thetaA2Var+2*np.pi,num=20)  

		curveXinVar = Rin*np.cos(thetaList)+centro[0]
		curveYinVar = Rin*np.sin(thetaList)+centro[1]
		#lin, = plt.plot(curveX,curveY,color = 'b', linewidth=0.5)
		lin.set_xdata(curveXinVar)
		###############################
		A1 = P
		centro = centroCirc(P,v,Bout)
		P = pointOut(centro,P,Rout) #punto salida
		v = veloOut(P,centro)
		#script plotting outside
		#plotArc(A1,P,centro,Rout)
		thetaA1 = thetaAngle(np.array([A1[0]-centro[0],A1[1]-centro[1]]))
		thetaA2 = thetaAngle(np.array([P[0]-centro[0],P[1]-centro[1]]))
		if thetaA1 < thetaA2:
		#theta = np.linspace(0,thetaB-thetaA,num=10)	
			thetaList = np.linspace(thetaA1,thetaA2,num=20)
		else: #thetaA > thetaB
			thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=20)  

		curveX = Rout*np.cos(thetaList)+centro[0]
		curveY = Rout*np.sin(thetaList)+centro[1]
		lout, = plt.plot(curveX,curveY,color = 'b', linewidth=0.5)
					

AngleSlider.on_changed(update)
plt.show()
