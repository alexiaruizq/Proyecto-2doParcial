from OpenGL.GL import *
from glew_wish import *
import glfw 
from math import *
import random
from enum import Enum

class Pelota:
    xposicion = 0
    yposicion = 0
    angulo = random.randrange(30, 180)
    desfase = 90
    velocidad = 1

    def actualizar(self, tiempo_delta):
  
        self.yposicion = self.yposicion + (sin((self.angulo + self.desfase) * 3.14159 / 180) * 0.75 * tiempo_delta)
        self.xposicion = self.xposicion + (cos((self.angulo + self.desfase) * 3.14159 / 180) * 0.75 * tiempo_delta)

    def dibujar(self, jugador1, jugador2):
       
        glPushMatrix()
        glTranslate(self.xposicion, self.yposicion, 0.0)
        glBegin(GL_QUADS)
        if jugador1.colisionando == True and jugador2.colisionando:
            glColor3f(1.0, 1.0, 1.0)
        else:
            glColor3f(1.0, 1.0, 1.0)
        glVertex3f(0.05, 0.05, 0.0)
        glVertex3f(0.05, -0.05, 0.0)
        glVertex3f(-0.05, -0.05, 0.0)
        glVertex3f(-0.05, 0.05, 0.0)
        glEnd()
        glPopMatrix()
    
    def checar_colisiones(self, jugador1, jugador2):
    
        # Checar colision jugadores
        if  self.xposicion - 0.025 < jugador1.xposicion + 0.025 and self.xposicion + 0.025 > jugador1.xposicion - 0.0125 and self.yposicion - 0.1 < jugador1.yposicion + 0.025 and self.yposicion + 0.1 > jugador1.yposicion - 0.0125:
            self.angulo -= 90
        elif self.xposicion - 0.025 < jugador2.xposicion + 0.025 and self.xposicion + 0.025 > jugador2.xposicion - 0.0125 and self.yposicion - 0.1 < jugador2.yposicion + 0.025 and self.yposicion + 0.1 > jugador2.yposicion - 0.0125:
            self.angulo -= 90
        if self.xposicion - 0.025 <= -0.975 or self.xposicion + 0.025 >= 0.975:
            self.angulo -= 90
        if self.yposicion - 0.025 <= -0.975 or self.yposicion + 0.025 >= 0.975:
            self.angulo -= 90
