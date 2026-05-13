'''
MAGNETIC ANTIPARALELO
'''

import numpy as np
import matplotlib.pyplot as plt


def modulo(X):
	return (X[0]**2 + X[1]**2)**0.5
	
def unitary(X):
	modulo = (X[0]**2 + X[1]**2)**0.5 
	return X/modulo

def centroCirc(P,v,B):
	'''
	P = (x,y) particle position
	r = (rx,ry) vector from particle to circunference center
	c = (h,k) position of the circunference center 
	
	c = r + P
	'''
	r = (1/B)*unitary( np.array([-v[1]*B,v[0]*B]) )
	c = P + r
	return c

def centroCircOut(P,v,B):
	'''
	P = (x,y) particle position
	r = (rx,ry) vector from particle to circunference center
	c = (h,k) position of the circunference center 
	
	c = r + P
	'''
	r = (1/B)*unitary( np.array([v[1]*B,-v[0]*B]) )
	c = P + r
	return c


def rotar(v,angle):
	'''
	ROTAR UN VECTOR V UN ANGULO EN SENTIDO ANTI-HORARIO
	'''
	R = np.array([
		[np.cos(angle),-np.sin(angle)],
		[np.sin(angle),np.cos(angle)]
	])
	
	return np.dot(R,v)



def thetaAngle(hat):
	'''
	Scaling the theta angle (horizontal axis of phase space)
	'''
	theta = np.arctan(hat[1]/hat[0])
	if hat[0]<0:
		if hat[1]>0:
			theta = np.pi - np.arctan(-hat[1]/hat[0])
		elif hat[1]<0:
			theta = np.pi + np.arctan(np.abs(hat[1]/hat[0]))	
	if hat[0]>0 and hat[1]<0:
		theta = 3*np.pi/2 + np.arctan(np.abs(hat[0]/hat[1]))
	return theta

	
def verticalLineCircunference(R,c,x):
        '''
        Intersection between vertical line x=constante
        and a circunference
        '''
        h,k = c[0],c[1]
        #hallando discriminante
        Adiscr = 1
        Bdiscr = -2*k
        Cdiscr = k**2 + (x-h)**2 - R**2
	
        discr = Bdiscr**2 - 4*Adiscr*Cdiscr
	
        if discr >= 0:
                #print('Si hay solucion')
                y1 = (-Bdiscr + np.sqrt(discr))/(2*Adiscr)
                y2 = (-Bdiscr - np.sqrt(discr))/(2*Adiscr)	
                sol1 = np.array([x,y1])
                sol2 = np.array([x,y2])

        elif discr < 0:
                #print('No hay solucion')
                sol1 = np.array([None,None])
                sol2 = np.array([None,None])

        else:
                print('PROBLEMAS CON LA DISCRIMINANTE')	
	
	#sol1 = np.array([x,y1])
	#sol2 = np.array([x,y2])
	
        return [sol1,sol2]

def horizontalLineCircunference(R,c,y):
        '''
        Interesction between horizontal line y=constante
        '''
        h,k = c[0],c[1]
        Adiscr = 1
        Bdiscr = -2*h
        Cdiscr = h**2 + (y-k)**2 - R**2

        discr = Bdiscr**2 - 4*Adiscr*Cdiscr
	
        if discr >= 0:
                #print('Si hay solucion')
                x1 = (-Bdiscr + np.sqrt(discr))/(2*Adiscr)
                x2 = (-Bdiscr - np.sqrt(discr))/(2*Adiscr)
                sol1 = np.array([x1,y])
                sol2 = np.array([x2,y])
                
        elif discr < 0:
                #print('No hay solución')
                sol1 = np.array([None,None])
                sol2 = np.array([None,None])
        else:
                print('PROBLEMAS CON LA DISCRIMINANTE')

	#sol1 = np.array([x1,y])
	#sol2 = np.array([x2,y])
	
        return [sol1,sol2]

def validarPoints(punto):
        """
        Dado un conjunto de puntos se valida las intersecciones
        """
        if punto[0] is None:
                #print('Punto no valida')
                val = np.array([None,None])
        else:
                #verificar si los puntos estan dentro de las fronteras
                if punto[0] >= 0 and punto[0] <= 1:
                        #print('VALIDO')
                        if punto[1] >= 0 and punto[1] <= 1:
                                #print('CONFIRMADO, VALIDO')
                                val = punto
                        else:
                                #print('lo siento, no valido')
                                val = np.array([None,None])
                else:
                        #print('No valido')
                        val = np.array([None,None])
        return val

def sDistance(P):
        '''
        Hallando la distancia s
        '''
        if P[1] == 0:
                s = P[0]
        elif P[0] == 1:
                s = P[0] + P[1]
        elif P[1] == 1:
                s = 2 + (1 - P[0])
        elif P[0] == 0:
                s = 4 - P[1]
        else:
                print(10*'·','PROBLEMAS')
		 
        return s

def sThetaAngle(P,v):
        '''
        Hallar angulo theta entre pared y velocidad
        '''
        if P[1] == 0: #Down
                T = np.array([1,0])
                if v[0] > 0: #apuntar a la derecha
                        #menor de 90
                        angle = np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))	
                elif v[0] < 0: #apuntar a la izquierdaa
			#mayor de 90
                        #angle = np.pi - np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))
                        angle = np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))
        elif P[0] == 1 : #Right
                T = np.array([0,1])
                if v[1] > 0: #apuntar arriba
                        #menor de 90
                        #angle = np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                        angle = np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                elif v[1] < 0: #apuntar abajo
                        #mayor de 90
                        #angle = np.pi - np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                        angle = np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
        elif P[1] == 1: # Up
                T = np.array([-1,0])
                if v[0] > 0: #apuntar a la derecha
                        #mayor de 90
                        #angle = np.pi - np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))
                        angle = np.pi - np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))
                elif v[0] < 0: #apuntar a la izquierda
                        #menor de 90
                        angle = np.pi - np.arccos(v[0]/np.sqrt(v[0]**2 + v[1]**2))
        elif P[0] == 0 : #Left
                T = np.array([0,-1])
                if v[1] > 0: #apuntar arriba
                        #mayor de 90
                        angle = np.pi - np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                        #angle = np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                elif v[1] < 0: #apuntar abajo
                        #menor de 90
                        #angle = np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
                        angle = np.pi - np.arccos(v[1]/np.sqrt(v[0]**2 + v[1]**2))
        else:
                print('PROBLEMAS')
	
	
        return angle

def pointOut(centro,P,R):
        '''
        Return the point of the square where the particle scapes
        '''
        h,k = centro[0],centro[1]
        x,y = P[0],P[1]
        hits = [] #lista que guarda todos los puntos de choque
        right1,right2 = verticalLineCircunference(R,centro,1)
        valright1 = validarPoints(right1)
        valright2 = validarPoints(right2)
        if valright1[0] is not None:
                hits.append(right1)
        if valright2[0] is not None:
                hits.append(right2)
        left1,left2 = verticalLineCircunference(R,centro,0)
        valleft1 = validarPoints(left1)
        valleft2 = validarPoints(left2)
        if valleft1[0] is not None:
                hits.append(left1)
        if valleft2[0] is not None:
                hits.append(left2)
        up1,up2 = horizontalLineCircunference(R,centro,1)
        valup1 = validarPoints(up1)
        valup2 = validarPoints(up2)
        if valup1[0] is not None:
                hits.append(up1)
        if valup2[0] is not None:
                hits.append(up2)
        down1,down2 = horizontalLineCircunference(R,centro,0)
        valdown1 = validarPoints(down1)
        valdown2 = validarPoints(down2)
        if valdown1[0] is not None:
                hits.append(down1)
        if valdown2[0] is not None:
                hits.append(down2)
        ###
        #Detectar puntos
        ###
        punto_partida = thetaAngle(np.array([P[0]-centro[0],P[1]-centro[1]]))
        points_list = []
        resta_list = []
        #hallar el punto de partida
        for point in hits:
                resta = np.abs(punto_partida - thetaAngle(np.array([point[0]-centro[0],point[1]-centro[1]])))
                if resta < 10e-8:
			#print('partida',point)
                        pass
                else:
                        points_list.append(point)
                        resta_list.append(resta)

        vPartida = np.array([P[0]-centro[0],P[1]-centro[1]]) 
        anguloPoint_list = []
        for hit in points_list:
                vhit = np.array([	hit[0]-centro[0],hit[1]-centro[1]	])
                cos = (vPartida[0]*vhit[0] + vPartida[1]*vhit[1])/(modulo(vPartida)*modulo(vhit))
                arccos = np.arccos(cos)
                cruz = np.cross([vPartida[0],vPartida[1],0],[vhit[0],vhit[1],0])

                if cruz[2] < 0:
				#mayor de 180
                        if cos > 0:
                                anguloPoint = 2*np.pi - np.abs(np.arccos(cos))
                        else:
                                anguloPoint = 2*np.pi - np.abs(np.arccos(cos)) 
                else:
			#menor de 180
                        anguloPoint = np.arccos(cos)
                        if anguloPoint < 0:
                                anguloPoint = np.pi + anguloPoint
                anguloPoint_list.append(anguloPoint)


        choque = points_list[np.argmin(anguloPoint_list)]
        hit = choque
        P = choque
        #print('Punto salida',P)        

        return P

def veloOut(P,centro):
        '''
        Velocity of the particle when it scapes from the square
        '''
        if P[1] == 1:
                d = P - centro
                vOut = rotar(d,np.pi/2)
        elif P[0] == 0:
		#print('choque pared izquierda')
                d = P - centro
                vOut = rotar(d,np.pi/2)
        elif P[1] == 0:
		#print('choque base')
                d = P - centro
                vOut = rotar(d,np.pi/2)
		
        elif P[0] == 1:
		#print('choque pared derecha')
                d = P - centro
                vOut = rotar(d,np.pi/2)

        else:
                print('problemas!!')
		
        #print('velo salida',vOut) ### velo de salida
        return vOut

def plotArc(A1,A2,centro,R,cline):
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
                thetaList = np.linspace(thetaA1,thetaA2,num=100)
        else: #thetaA > thetaB
                thetaList = np.linspace(thetaA1,thetaA2+2*np.pi,num=100)  
	#theta = np.linspace(0,thetaB-thetaA,num=10)
	#print(np.rad2deg(thetaList))
	#R = np.matrix([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
        curveX = R*np.cos(thetaList)+centro[0]
        curveY = R*np.sin(thetaList)+centro[1]
        plt.plot(curveX,curveY,color = cline, linewidth=0.5)

        
