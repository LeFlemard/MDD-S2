#Draw.py
import pyglet
from pyglet.gl import *


def loadTexture(nom):
	image = pyglet.image.load(nom)
	print "Texture ", nom, " loaded"
		
	texture = image.get_texture()
	
	glBindTexture(GL_TEXTURE_2D,texture.id)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)

	return texture

def drawSquare(position0,position1,texture=None,color=(1.0,0.0,0.0)):
	x0,y0,z0 = position0
	x1,y1,z1 = position1
	if texture == None :
		glDisable(GL_TEXTURE_2D)
		r,v,b = color
		glColor3f(r,v,b)
		glBegin(GL_QUADS)
		glVertex3f(x0,y0,z0)
		glVertex3f(x0,y1,z0)
		glVertex3f(x1,y1,z1)
		glVertex3f(x1,y0,z1)
		glEnd()
		glEnable(GL_TEXTURE_2D)
		
		pass
	
	else :
		glBindTexture(GL_TEXTURE_2D,texture.id)
		glBegin(GL_QUADS)
		glTexCoord2f(0.0,0.0)
		glVertex3f(x0,y0,z0)
		glTexCoord2f(1.0,0.0)
		glVertex3f(x0,y1,z0)
		glTexCoord2f(1.0,1.0)
		glVertex3f(x1,y1,z1)
		glTexCoord2f(0.0,1.0)
		glVertex3f(x1,y0,z1)
		glEnd()
