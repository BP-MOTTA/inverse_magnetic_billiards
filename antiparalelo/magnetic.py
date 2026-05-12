'''
MAGNETIC ANTIPARALELO
'''

import numpy as np
import matplotlib.pyplot as plt

def solve2eq(A,B,C):
	'''
	Solve second-degree equation of the form
	A*x**2 + B*x + C = 0
	Input: A,B,C coefficients
	Output: Two roots x1 and x2
	Note: If there is no solutios
	it returns an array [None,None]
	'''
	#Discriminant
	d = B**2 - 4*A*C 
	if d<0:
		#No real solutions
		print('PROBLEMAS EN FUNCION solve2eq. d < 0')
		return np.array([None,None])
	else:	
		#Solving
		x1 = (-B+np.sqrt(d))/(2*A)
		x2 = (-B-np.sqrt(d))/(2*A)
		sol = np.float128([x1,x2])
		return sol
		


def normalVect(v):
	'''
	VECTOR NORMAL A LA VELOCIDAD
	'''
	return np.array([-v[1],v[0]])
	
def circunference(h,k,r):
	'''
	COORDENADAS (X,Y) PARA GRAFICAR LA TRAYECTORIA CIRCULAR	
	'''
	angle = np.linspace(0,2*np.pi)
	x = r*np.cos(angle)+h
	y = r*np.sin(angle)+k
	return np.array([x,y])

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


def centroCirc2(P,v,R):
	'''
	HALLAR EL CENTRO DE CIRCUNFERENCIA
	SI LA ENTRADA ES EL PUNTO Y LA VELOCIDAD
	'''
	normal_v = normalVect(v)
	w = np.arctan(normal_v[0]/normal_v[1])
	h = P[0]+R*np.sin(w)	
	k = P[1]+R*np.cos(w)	 
	return np.array([h,k])

def rotar(v,angle):
	'''
	ROTAR UN VECTOR V UN ANGULO EN SENTIDO ANTI-HORARIO
	'''
	R = np.array([
		[np.cos(angle),-np.sin(angle)],
		[np.sin(angle),np.cos(angle)]
	])
	
	return np.dot(R,v)

def intersection(h,k,r):
	'''
	INTERSECCION CON PARED VERTICAL x=0
	'''
	#y = np.sqrt(r**2 - h**2) + k
	return np.sqrt(r**2 - h**2) + k

def intersection_base(centro,R):
	'''
	INTERSECCION CON EL PISO
	'''
	h,k = centro[0],centro[1]
	if R**2 - k**2 < 0:
		#print('intersection_base: no base intersection')
		P1 = np.array([None,None])
		P2 = np.array([None,None])
	
	else:
		s1 = np.sqrt(R**2 - k**2) + h
		s2 = -np.sqrt(R**2 - k**2)+ h
		#retornar datos de menor a mayor
		if s1<s2:
			x1 = s1
			x2 = s2
		else:
			x1 = s2
			x2 = s1
		P1 = np.array([x1,0])
		P2 = np.array([x2,0])
	return np.array([P1,P2])

#def hatIntersection(centro,R):
#	'''
#	IS THERE HAT INTERSECTION?
#	RETURN: TRUE OR FALSE
#	'''
#	gamma = R**2 - np.power(centro[0],2) - np.power(centro[1],2) - 1
#	A = centro[0]**2 + centro[1]**2
#	B1 = gamma*centro[0]
#	C = (gamma**2 / 4)-centro[1]**2
#	discriminante = B1**2 - 4*A*C
#	if discriminante >= 0 :
#		val = True
#	else:
#		val = False
#	return val	


def circ_x_intersection(centro,R):
	'''
	INTERSECCION ENTRE DOS CIRCUNFERENCIAS
	'''
	gamma = R**2 - np.power(centro[0],2) - np.power(centro[1],2) - 1
	A = centro[0]**2 + centro[1]**2
	B1 = gamma*centro[0]
	C = (gamma**2 / 4)-centro[1]**2
	
	discriminante = B1**2 - 4*A*C
	#print('discriminante:',discriminante)
	if discriminante > 0:
		xhit = solve2eq(A,B1,C)
		#ordenar de menor a mayor
		if xhit[0]<xhit[1]:
			x1 = xhit[0]
			x2 = xhit[1]
		else:
			x1 = xhit[1]	
			x2 = xhit[0]	
		return np.array([x1,x2])
	
	elif discriminante == 0:
		xhit = solve2eq(A,B1,C)
		return np.array([xhit[0],xhit[1]])
	else:
		#print('No hat intersection')
		return np.array([None,None])

def circ_y_intersection(xhit,centro,R):

	if xhit[0] == None or xhit[1] == None:
		return np.array([None,None])
	
	elif xhit[0] == xhit[1]:
		if 1-xhit[0]**2 < 0:
			return np.array([None,None])
		else:
			y1,y2 = np.sqrt(1-xhit[0]**2),-np.sqrt(1-xhit[0]**2)
			return np.array([y1,y2])
	
	else:

		y1A,y1B = np.sqrt(1-xhit[0]**2), -np.sqrt(1-xhit[0]**2)
		y2A,y2B = np.sqrt(1-xhit[1]**2), -np.sqrt(1-xhit[1]**2)
		
		d1A = (centro[0]-xhit[0])**2 + (centro[1]-y1A)**2 - R**2
		d1B = (centro[0]-xhit[0])**2 + (centro[1]-y1B)**2 - R**2
		
		if np.abs(d1A) < np.abs(d1B):
			y1 = y1A
		else:
			y1 = y1B
		
		d2A = (centro[0]-xhit[1])**2 + (centro[1]-y2A)**2 - R**2
		d2B = (centro[0]-xhit[1])**2 + (centro[1]-y2B)**2 - R**2
		if np.abs(d2A) < np.abs(d2B):
			y2 = y2A
		else:
			y2 = y2B
		
		return np.array([y1,y2])	

def unitary_vector(v):
	'''
	RETURNS UNITARY VECTOR
	Input:
	> v: two dimensional vector
	Output:
	Unitary vector of v
	'''
	return v/np.sqrt(v[0]**2 + v[1]**2)


def reflexVelocityHat(hit,velocity):
	'''
	If ball collides with mushroom hat, this functions returns the reflex velocity
	JUST FOR THE MUSHROOM (FOR THE MOMENT)
	'''
	normal = unitary_vector(-hit) #vector normal
	reflex = np.float128(velocity - (np.dot(2*velocity,normal))*normal) #vector velocidad reflexion
	return reflex	

def arcPlot(c):
	'''
	plot arc inside table
	'''
	cx = c[0]
	cy = c[1]
	arcx = np.array([])
	arcy = np.array([])
	for i in range(len(cx)):
		if cx[i]**2 + cy[i]**2 <= 1 and cy[i]>=0:
			plt.plot(cx[i],cy[i],'k.')
			#arcx=np.append(arcx,cx[i])
			#arcy=np.append(arcy,cy[i])
	
def trajectory(pos,vel):
    '''
    Trajectory of particle
    Input:
    > pos: initial position
    > vel: initial velocity
    Output: Line equation of the trajectory of the ball y=m*x+b
    > m: slope
    > b: y-axis intersection
    '''
    m = vel[1]/vel[0]
    b = pos[1] - m*pos[0]
    trajectory = np.array([m,b]) #m y b trajectory
    return trajectory	

def tangent(hit):
    '''
    Tangent line on hat's point
    Input:
    > hit: collision point on hat
    Output: equation of tangent line on a given hat point
    yT = mT*x + bT
    >mT : slope of tangent Tline
    >bT : y-axis intersection 
    '''
    mT = -hit[0]/hit[1]
    bT = hit[1] - mT*hit[0]
    tangent = np.array([mT,bT]) # m and b of tangent line
    return tangent

def angleVectors(m1,m2):
    '''
    Angle between two vectors given the slopes
    Input:
    > m1,m2: slope of the two vectors
    Output:
    > alpha: Angle between 2 vectors
    '''
    alpha = np.arctan(np.abs((m1-m2)/(1+m1*m2)))
    return alpha


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

def phiAngle(theta,hat):
	'''
	Determining phi angle
	'''
	phi = np.pi/2 + theta
		
	if hat[0]>0 and hat[1]<0:
		phi = np.pi/2 - np.arctan(np.abs(hat[1]/hat[0]))
	return phi		

def alphaAngle(hat,veloReflex,phi):
	'''
	Alpha Angle
	'''
	#trajectoryLine = trajectory(ri,vi)
	tangentLine = tangent(hat)
	alpha = angleVectors(tangentLine[0],veloReflex[1]/veloReflex[0])
	if hat[0]>0:
		if hat[1]>0:
			if veloReflex[0]<0 and veloReflex[1]<0:
				alpha = np.pi - phi + np.arctan(np.abs(veloReflex[1])/np.abs(veloReflex[0]))
			if veloReflex[0]>0 and veloReflex[1]<0:
				alpha = np.pi - alpha
		if hat[1]<0:
			if veloReflex[0]<0 and veloReflex[1]>0:
				alpha = np.pi/2 - phi + np.arctan(np.abs(veloReflex[0]/veloReflex[1]))
			if veloReflex[0]<0 and veloReflex[1]<0:
				alpha = np.pi - alpha
	
	if hat[0]<0:
		if hat[1]>0:
			if veloReflex[0]>0 and veloReflex[1]<0:
				alpha = (3*np.pi/2 - phi) + np.arctan(np.abs(veloReflex[0])/np.abs(veloReflex[1]))
			if veloReflex[0]>0 and veloReflex[1]>0:
				alpha = np.pi - alpha
		if hat[1]<0:
			if veloReflex[0]>0 and veloReflex[1]>0:
				alpha = 2*np.pi - phi + np.arctan(np.abs(veloReflex[1]/veloReflex[0]))
			if veloReflex[0]<0 and veloReflex[1]>0:
				alpha = np.pi - alpha
	
	return alpha

def hatCollision(pos,vel):
    '''
    This function detects the collision points on the mushroom hat
    Expected two poins because it solves the intersection
    of a circunference and a line
    Input:
    > pos : initial position of the ball
    > vel : initial velocity of the ball 
    Output:
    > posChoque: Collision points P1 and P2
    '''
    xout = pos[0]
    yout = pos[1]
    m = vel[1]/vel[0]
    b = pos[1] - m*pos[0]
    A = m**2 + 1
    B = 2*m*b
    C = b**2 - 1
    xsol = solve2eq(A,B,C)
    x1,x2 = xsol[0],xsol[1]
    if np.absolute(x1-xout) < np.absolute(x2-xout):
        xchoque = x1
    else:
        xchoque = x2
    ychoque = m*xchoque + b
    posChoque = np.float64([xchoque,ychoque])
    return posChoque


    
def hatLineIntersection(gamma_left,gamma_right,B):
    '''
    Function for plotting the mushroom hat.
    Intersection between hat and tilted line for plotting
    Input:
    > gamma_left,gamma_right : angles
    > B: base
    Output: Left and right points of intersection of tilted lines and mushroom hat
    '''
    Pleft =  hatCollision([-B/2,0],[-np.cos(gamma_left),np.sin(gamma_left)])
    Pright = hatCollision([B/2,0],[np.cos(gamma_right),np.sin(gamma_right)])
    return [Pleft,Pright]

def arcHatPlot(gamma_left,gamma_right,B):
    '''
    Draw the hat
    Input: gamma_left,gamma_right,B
    Output: Mushroom hat plot
    '''
    Pleft,Pright = hatLineIntersection(gamma_left,gamma_right,B)
    alphaO = np.arctan(Pright[1]/Pright[0])
    alphaF = np.pi +np.arctan(Pleft[1]/Pleft[0])
    alpha=np.linspace(alphaO,alphaF,50000)
    x = np.cos(alpha)
    y = np.sin(alpha)
    
    plt.plot(x,y,'r')

def mushroomPlot(gamma_left,gamma_right,B,H):
    '''
    Draw all the mushroom
    Input:
    > Gamma Left and gamma right angle
    > B: base
    > H: height
    Output:
    Mushroom Plot
    '''
    Pleft,Pright = hatLineIntersection(gamma_left,gamma_right,B)
    arcHatPlot(gamma_left,gamma_right,B)
    plt.plot([-B/2,-B/2],[0,-H],'r')
    plt.plot([-B/2,B/2],[-H,-H],'r')
    plt.plot([B/2,B/2],[-H,0],'r')
    plt.plot([Pleft[0],-B/2],[Pleft[1],0],'r')
    plt.plot([Pright[0],B/2],[Pright[1],0],'r')

def wallCircleIntersection(wall,centro,radio):
	'''
	Intersección entre la pared inclinada y la trayectoria circunferencial
	ordenado de izquierda a derecha
	'''
	m = wall[0]
	b = wall[1]
	A = 1 + m**2 
	B = 2*(-centro[0]+m*b-m*centro[1])
	C = centro[0]**2 + b**2 - 2*b*centro[1] + centro[1]**2 - radio**2
	
	
	if B**2 - 4*A*C < 0:
		P1 = np.array([None,None])
		P2 = np.array([None,None])
	else:
		x = solve2eq(A,B,C)
		if x[0] < x[1]:
			x1 = x[0]
			x2 = x[1]
		else:
			x1 = x[1] 
			x2 = x[0]
		y1 = m*x1 + b
		y2 = m*x2 + b
		P1 = np.array([x1,y1])
		P2 = np.array([x2,y2])
	return [P1,P2]
	
def reflexVelocityWall(normal,velocity):
	'''
	Reflexion velocity for a ball colliding on a wall
	'''
	reflex = np.float64(velocity - (2*np.dot(velocity,normal))*normal)				
	return reflex
	
def hatCircleIntersection(centro,R):
	'''
	COLLISION WITH HAT
	'''
	gamma = R**2 - np.power(centro[0],2) - np.power(centro[1],2) - 1
	A = centro[0]**2 + centro[1]**2
	B1 = gamma*centro[0]
	C = (gamma**2 / 4)-centro[1]**2
	discriminante = B1**2 - 4*A*C

	if discriminante >= 0:
		xhit = circ_x_intersection(centro,R)
		yhit = circ_y_intersection(xhit,centro,R)
		P1 = np.array([xhit[0],yhit[0]])
		P2 = np.array([xhit[1],yhit[1]])
	else:
		P1 = np.array([None,None])
		P2 = np.array([None,None])
	return np.array([P1,P2])
	
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
        Retorna el punto de salida
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
        Velocidad de salida
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

        
