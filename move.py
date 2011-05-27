import math
import decor

positionOeil = (0.0,1.6,5.0)
directionVisee = -math.pi/2.0

def changeParametreCamera(newPositionOeil,newDirectionVisee)
	global directionVisee
	global positionOeil
	positionOeil=newPositionOeil
	directionVisee=newDirectionVisee
	
def deg2rad(d):
	return math.pi*d/180.0

def parametresCamera():
	ex, ey,ez = positionOeil
	dx, dy, dz = math.cos(directionVisee), 0.0, math.sin(directionVisee)
	
	pointVise = ex + dx, ey+dy, ez+dz

	return positionOeil, pointVise, (0.0,1.0,0.0)

def rotationCamera(angleDegre):
	global directionVisee
	angleRadian = deg2rad(angleDegre)
	directionVisee += angleRadian

def deplacementCamera(deplacement):
	global positionOeil
	ex, ey, ez = positionOeil
	dx, dy, dz = math.cos(directionVisee), 0.0, math.sin(directionVisee)
	l = math.sqrt(dx*dx + dy*dy + dz*dz)
	d1x, d1y,d1z = dx/l, dy/l, dz/l
	flagx = True
	flagy = True
	flagz = True
	for element in getListeDecor :
		if ex + deplacement*d1x in range [element.positionDepart[0], element.positionFin[0]:
			flagx = False
		if ey + deplacement*d1y in range [element.positionDepart[1], element.positionFin[1]:
			flagy = False
		if ez + deplacement*d1z in range [element.positionDepart[2], element.positionFin[2]:
			flagz = False
	if flagx :
		nex =  ex + deplacement*d1x
	else :
		nex = ex
	if flagy :
		ney = ey + deplacement*d1y
	else :
		ney = ey
	if flagz :
		nez = ez + deplacement*d1z
	else :
		nez = ez
			
	positionOeil = nex, ney, nez