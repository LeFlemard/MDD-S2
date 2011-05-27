#! /usr/bin/python

import pyglet
from pyglet.gl import *

import math
import move
import decor
# Variables globales
#  -----------------



listeQuizz=[]
listeDecor=[]
listeTexture={}
listeZone={}
positionOeil=None
keyUp = False
keyDown = False
keyLeft = False
keyRight = False
keyEnter = False
key_1 = False
key_2 = False
key_3 = False
key_4 = False

window = pyglet.window.Window(resizable = False)

def setup():
	global positionInitiale
	global directionVisee
	global listeDecor 
	global window
	global listeQuizz
	global listeTexture
	global listeZone
	
	glEnable(GL_DEPTH_TEST)

	glEnable(GL_TEXTURE_2D)
	glAlphaFunc(GL_GREATER,0.4)
	glEnable(GL_ALPHA_TEST)



	# Chargement des textures

	print "general setup will now start"
	decor.placerDecor()	
	listeDecor=decor.getListeDecor()
	listeQuizz=decor.getListeQuizz()
	listeTexture=decor.getListeTexture()
	listeZone=decor.getListeZone()
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_TEXTURE_2D)
	glAlphaFunc(GL_GREATER,0.4)
	glEnable(GL_ALPHA_TEST)	
	print "general setup ends"
	
	window.set_fullscreen(True)
	

@window.event
def on_resize(width, height):
    # Override the default on_resize handler to create a 3D projection
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / float(height), .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    return pyglet.event.EVENT_HANDLED


@window.event
def on_draw():
	global positionInitiale
	global directionVisee
	global listeDecor 
	global window
	global listeQuizz
	global listeTexture
	global listeZone
	#print "hello world on_draw"
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Placement de la camera
	oeil, pointVise, verticale = camera.parametresCamera()

	ex,ey,ez = oeil
	ax, ay, az = pointVise
	
	glLoadIdentity()
	gluLookAt(ex,ey,ez,  ax, ay, az,  0.0,1.0,0.0)
	decor.drawAlldecor()

@window.event
def on_key_press(symbol,modifiers):
	global keyUp
	global keyDown
	global keyLeft
	global keyRight
	global keyEnter
	global key_1
	global key_2
	global key_3
	global key_4
	global keyEnter

	if symbol == pyglet.window.key.UP :
		keyUp = True
	if symbol == pyglet.window.key.DOWN :
		keyDown = True
	if symbol == pyglet.window.key.LEFT :
		keyLeft = True
	if symbol == pyglet.window.key.RIGHT :
		keyRight = True
	if symbol == pyglet.window.key._1 :
		key_1 = True
	if symbol == pyglet.window.key._2 :
		key_2 = True
	if symbol == pyglet.window.key._3 :
		key_3 = True
	if symbol == pyglet.window.key._4 :
		key_4 = True
	if symbol == pyglet.window.key.ENTER :	
		keyEnter = True

@window.event
def on_key_release(symbol, modifiers):
	global keyUp
	global keyDown
	global keyLeft
	global keyRight
	global key_1
	global key_2
	global key_3
	global key_4
	global keyEnter
	
	if symbol == pyglet.window.key.UP :
		keyUp = False
	if symbol == pyglet.window.key.DOWN :
		keyDown = False
	if symbol == pyglet.window.key.LEFT :
		keyLeft = False
	if symbol == pyglet.window.key.RIGHT :
		keyRight = False	
	if symbol == pyglet.window.key._1 :
		key_1 = False
	if symbol == pyglet.window.key._2 :
		key_2 = False
	if symbol == pyglet.window.key._3 :
		key_3 = False
	if symbol == pyglet.window.key._4 :
		key_4 = False
	if symbol == pyglet.window.key.ENTER :
		keyEnter = False

def update(dt):
	global horloge
	global keyUp
	global keyLeft
	global keyDown
	global keyRight
	global key_1
	global key_2
	global key_3
	global key_4
	global keyEnter

	listeDecor=decor.getListeDecor()
	listeQuizz=decor.getListeQuizz()
	listeTexture=decor.getListeTexture()
	listeZone=decor.getListeZone()
	
	if decor.testQuizz():
		if key_1 :
			decor.repondreQuizz("1")
		if key_2 :
			decor.repondreQuizz("2")
		if key_3 :
			decor.repondreQuizz("3")
		if key_4 :
			decor.repondreQuizz("4")
	else : 
		if  not 
		if keyLeft :
			move.rotationCamera(-2.0)
		if keyRight :
			move.rotationCamera(2.0)
		if keyUp :
			camera.deplacementCamera(0.5)
		if keyDown :
			camera.deplacementCamera(-0.5)
	horloge = horloge + dt
	
def main():
	
	print "Hello World"
	setup()
	
	# La fonction update sera appelee toutes les 30eme de seconde
	pyglet.clock.schedule_interval(update, 1.0/30.0)
	pyglet.app.run()
	
if __name__ == "__main__" :
	main()
	pass

