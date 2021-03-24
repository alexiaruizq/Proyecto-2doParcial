from OpenGL.GL import *
from glew_wish import *
import glfw 
from math import *
import random
from enum import Enum

class Marco:
    def dibujar(Self):
    #izq
        glColor3f(0.788,0.596,0.364)
        glBegin(GL_QUADS)
        glVertex3f(-1.0,1.0,0) #izqArr
        glVertex3f(-0.95,1.0,0) #derArr
        glVertex3f(-0.95,-1.0,0) #derAba
        glVertex3f(-1.0,-1.0,0) #izqAba
        glEnd()

        #der
        glColor3f(0.788,0.596,0.364)
        glBegin(GL_QUADS)
        glVertex3f(0.95,1.0,0) #izqArr
        glVertex3f(1.0,1.0,0) #derArr
        glVertex3f(1.0,-1.0,0) #derAba
        glVertex3f(0.95,-1.0,0) #izqAba
        glEnd()

        #arriba
        glColor3f(0.788,0.596,0.364)
        glBegin(GL_QUADS)
        glVertex3f(-1.0,1.0,0) #izqArr
        glVertex3f(1.0,1.0,0) #derArr
        glVertex3f(1.0,0.95,0) #derAba
        glVertex3f(-1.0,0.95,0) #izqAba
        glEnd()

        #abajo
        glColor3f(0.788,0.596,0.364)
        glBegin(GL_QUADS)
        glVertex3f(-1.0,-0.95,0) #izqArr
        glVertex3f(1.0,-0.95,0) #derArr
        glVertex3f(1.0,0.-1.0,0) #derAba
        glVertex3f(-1.0,-1.0,0) #izqAba
        glEnd()

        glColor3f(0.913,0.588,0.478)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.2 - 1.0, sin(angulo) * 0.2 + 1.0 ,0.0)
        glEnd()

        glColor3f(0.913,0.588,0.478)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.2 + 1.0, sin(angulo) * 0.2 + 1.0 ,0.0)
        glEnd()

        glColor3f(0.913,0.588,0.478)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.2 - 1.0, sin(angulo) * 0.2 - 1.0 ,0.0)
        glEnd()

        glColor3f(0.913,0.588,0.478)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.2 + 1.0, sin(angulo) * 0.2 - 1.0 ,0.0)
        glEnd()