from OpenGL.GL import *
from glew_wish import *
import glfw 
from math import *
import random
from enum import Enum

class Jugador1:
    xposicion = -0.9
    yposicion = 0
    puntos = 0
    colisionando = False

    def dibujar(self):

        glPushMatrix()
        glTranslate(self.xposicion, self.yposicion, 0.0)
        glBegin(GL_QUADS)
        if self.colisionando == True:
            glColor3f(0.0, 0.0, 0.0)
        else:
            glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.025, 0.2, 0.0)
        glVertex3f(0.025, -0.2, 0.0)
        glVertex3f(-0.025, -0.2, 0.0)
        glVertex3f(-0.025, 0.2, 0.0)
        glEnd()
        glPopMatrix()

    def actualizar(self, window, tiempo_delta, pelota):

        # Player 1
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)

        if estadoArriba == glfw.PRESS:
            if self.yposicion < 0.8:
                self.yposicion = self.yposicion + (sin((0 + pelota.desfase) * 3.14159 / 180) * pelota.velocidad * tiempo_delta)

        if estadoAbajo == glfw.PRESS:
            if self.yposicion > -0.8:
                self.yposicion = self.yposicion + (sin((180 + pelota.desfase) * 3.14159 / 180) * pelota.velocidad * tiempo_delta)
