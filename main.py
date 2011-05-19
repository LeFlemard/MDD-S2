#! /usr/bin/python

import pyglet
from pyglet.gl import *

import math
import move
import decor
# Variables globales
#  -----------------


horloge=0.0
liste_entities=[]
liste_environement=[]
positionOeil=None
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

window = pyglet.window.Window(resizable = False)
position_clic = None

def setup():
	global positionInitiale
	global directionVisee
	global decor 
	global window
	
	glEnable(GL_DEPTH_TEST)

	glEnable(GL_TEXTURE_2D)
	glAlphaFunc(GL_GREATER,0.4)
	glEnable(GL_ALPHA_TEST)



	# Chargement des textures

	print "general setup will now start"
	print '-|texture loading'
	decor.textureDecorSetup()
	print '-|texture loaded'
	print '-|map loading'
	decor.placerDecor()
	decor = decor.getDecor()
	print '-|map loaded'
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
	global decor
	#print "hello world on_draw"
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Placement de la camera
	oeil, pointVise, verticale = camera.parametresCamera()

	ex,ey,ez = oeil
	ax, ay, az = pointVise
	
	glLoadIdentity()
	gluLookAt(ex,ey,ez,  ax, ay, az,  0.0,1.0,0.0)
	for y in decor :
		if y.get_modele() == 'wall' :
			draw.draw_wall(y)
		elif y.get_modele() == 'wallWithDoor':
			prims.draw_wallWithDoor(y)
		else : print "bad_argument"

@window.event
def on_key_press(symbol,modifiers):
	global keyUp
	global keyDown
	global keyLeft
	global keyRight

	if symbol == pyglet.window.key.UP :
		keyUp = True
	if symbol == pyglet.window.key.DOWN :
		keyDown = True
	if symbol == pyglet.window.key.LEFT :
		keyLeft = True
	if symbol == pyglet.window.key.RIGHT :
		keyRight = True


@window.event
def on_key_release(symbol, modifiers):
	global keyUp
	global keyDown
	global keyLeft
	global keyRight
	
	if symbol == pyglet.window.key.UP :
		keyUp = False
	if symbol == pyglet.window.key.DOWN :
		keyDown = False
	if symbol == pyglet.window.key.LEFT :
		keyLeft = False
	if symbol == pyglet.window.key.RIGHT :
		keyRight = False	

def update(dt):
	global horloge
	global keyUp
	global keyLeft
	global keyDown
	global keyRight

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

