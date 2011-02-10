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

def drawRectangle(position=(0.0,0.0,0.0),rotation=(0.0,0.0,0.0,0.0),size=(1.0,1.0),texture=None,color=(1.0,0.0,0.0)):

	x,y,z = position
	theta,thetax,thetay,thetaz = rotation
	width,length = size

	if texture == None :
		glDisable(GL_TEXTURE_2D)
		r,v,b = color

		glPushMatrix()
		glColor3f(r,v,b)
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,length,1.0)

		glBegin(GL_QUADS)
		glVertex3f(0.0,0.0,0.0)
		glVertex3f(1.0,0.0,0.0)
		glVertex3f(1.0,1.0,0.0)
		glVertex3f(0.0,1.0,0.0)
		glEnd()
		
		glPopMatrix()
		glEnable(GL_TEXTURE_2D)
		
		pass
	
	else :
		glBindTexture(GL_TEXTURE_2D,texture.id)
		
		glPushMatrix()
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,length,1.0)

		glBegin(GL_QUADS)
		glTexCoord2f(0.0,0.0)
		glVertex3f(0.0,0.0,0.0)
		glTexCoord2f(1.0,0.0)
		glVertex3f(1.0,0.0,0.0)
		glTexCoord2f(1.0,1.0)
		glVertex3f(1.0,0.0,1.0)
		glTexCoord2f(0.0,1.0)
		glVertex3f(0.0,0.0,1.0)
		glEnd()
		
		glPopMatrix()

def drawQuadrilateral(position=(0.0,0.0,0.0),rotation=(0.0,0.0,0.0,0.0),size=(1.0,1.0,1.0),texture=None,color=(1.0,0.0,0.0)):
	x,y,z = position
	theta,thetax,thetay,thetaz = rotation
	width, height,length = size

	if texture == None :
		glDisable(GL_TEXTURE_2D)
		
		if type(color[0]) is float :
			r1,g1,b1 = r2,g2,b2 = r3,g3,b3 = r4,g4,b4 = r5,g5,b5 = r6,g6,b6 = color
		else :
			color1, color2, color3, color4, color5, color6 = color
			r1,g1,b1 = color1
			r2,g2,b2 = color2
			r3,g3,b3 = color3
			r4,g4,b4 = color4
			r5,g5,b5 = color5
			r6,g6,b6 = color6
		
		glPushMatrix()
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,height,length)
		
		drawRectangle(position=(1.0,0.0,0.0),rotation=(-90.0,0.0,1.0,0.0),color=(r1,g1,b1))
		drawRectangle(position=(0.0,0.0,0.0),rotation=(90.0,0.0,1.0,0.0),color=(r2,g2,b2))
		drawRectangle(position=(0.0,0.0,1.0),rotation=(0.0,0.0,1.0,0.0),color=(r3,g3,b3))
		drawRectangle(position=(0.0,0.0,0.0),rotation=(180.0,0.0,1.0,0.0),color=(r4,g4,b4))
		drawRectangle(position=(0.0,1.0,0.0),rotation=(90.0,1.0,0.0,0.0),color=(r5,g5,b5))
		drawRectangle(position=(0.0,0.0,0.0),rotation=(-90.0,1.0,0.0,0.0),color=(r6,g6,b6))
		
		glPopMatrix()
		glEnable(GL_TEXTURE_2D)
		
		pass
	
	else :
		if type(texture) is list :
			texture1, texture2, texture3, texture4, texture5, texture6 = texture
		else :
			texture1 = texture2 = texture3 = texture4 = texture5 = texture6 = texture
		glPushMatrix()
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,length,1.0)

		drawRectangle(position=(1.0,0.0,0.0),rotation=(-90.0,0.0,1.0,0.0),texture=texture1)
		drawRectangle(position=(0.0,0.0,0.0),rotation=(90.0,0.0,1.0,0.0),texture=texture2)
		drawRectangle(position=(0.0,0.0,1.0),rotation=(0.0,0.0,1.0,0.0),texture=texture3)
		drawRectangle(position=(0.0,0.0,0.0),rotation=(180.0,0.0,1.0,0.0),texture=texture4)
		drawRectangle(position=(0.0,1.0,0.0),rotation=(90.0,1.0,0.0,0.0),texture=texture5)
		drawRectangle(position=(0.0,0.0,0.0),rotation=(-90.0,1.0,0.0,0.0),texture=texture6)
		
		glPopMatrix()

		pass

def drawWallWith1Door(position=(0.0,0.0,0.0),rotation=(0.0,0.0,0.0,0.0),size=(1.0,1.0,1.0),texture=None,color=(1.0,0.0,0.0)):
	x,y,z = position
	theta,thetax,thetay,thetaz = rotation

	width, height,length = size

	if texture == None :
		glDisable(GL_TEXTURE_2D)
		
		if type(color[0]) is float :
			r1,g1,b1 = r2,g2,b2 = r3,g3,b3 = r4,g4,b4 = r5,g5,b5 = r6,g6,b6 = color
		else :
			color1, color2, color3 = color
			r1,g1,b1 = color1
			r2,g2,b2 = color2
			r3,g3,b3 = color3
		
		glPushMatrix()
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,height,length)
		
		drawRectangle(position=(-1.0/3.0,     0.0,0.0),size=(1.0/3.0,2.0/3.0),color=color1)
		drawRectangle(position=(+1.0/3.0,     0.0,0.0),size=(1.0/3.0,2.0/3.0),color=color2)
		drawRectangle(position=(     0.0,+2.0/3.0,0.0),size=(    1.0,1.0/3.0),color=color3)
		
		glPopMatrix()
		glEnable(GL_TEXTURE_2D)
		
		pass
	
	else :
		if type(texture) is list :
			texture1, texture2, texture3, texture4, texture5, texture6 = texture
		else :
			texture1 = texture2 = texture3 = texture
		glPushMatrix()
		glTranslatef(x,y,z)
		glRotatef(theta,thetax,thetay,thetaz)
		glScalef(width,length,1.0)

		drawRectangle(position=(-1.0/3.0,     0.0,0.0),size=(1.0/3.0,2.0/3.0),texture=texture1)
		drawRectangle(position=(+1.0/3.0,     0.0,0.0),size=(1.0/3.0,2.0/3.0),texture=texture2)
		drawRectangle(position=(     0.0,+2.0/3.0,0.0),size=(    1.0,1.0/3.0),texture=texture3)
		
		glPopMatrix()

		pass

