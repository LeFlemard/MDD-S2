decor=None
def importationFichierVersVariable(carte):
	carte = open(carte,"r")
	map=[]
	for ligne in carte:
		map.append(ligne)
	carte.close()
	return map

def filtrerMap(map):
	mur=[]
	positionInitiale=None
	for ligne in map :
		ligne=str(ligne)
		ligne=ligne.strip("\n")
		ligne=ligne.split(":")
		print ligne[0],"\n",ligne[1]
		variable=ligne[0]
		valeur=ligne[1].split()
		print variable,"\n",valeur,valeur[0],valeur[0][1]
		valeur=eval(valeur)
		print variable,valeur
		if variable[0]=="mur":
			mur.append([valeur])
		if variable[0]=="positionInitiale":
			positionInitiale=[valeur]
		if variiable[0]="directionViseeInitiale":
			directionViseeInitiale=[valeur]
		
	return mur, positionInitiale, directionViseeInitiale

def placerDecor() :
	global decor
	map=importationFichierVersVariable("carte.txt")
	mur, positionInitiale, directionViseeInitiale=filtrerMap(map)
	decor=mur, positionInitiale, directionViseeInitiale
	
def	getDecor() :
	global decor
	return decor

directionViseeInitiale=0
positionInitiale=[0.0,0.0]
mur=[[10.0,0.0,10.0],[20.0,10.0,20.0]]


