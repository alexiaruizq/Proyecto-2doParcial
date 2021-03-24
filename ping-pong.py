from OpenGL.GL import *
from glew_wish import *
import glfw 
from math import *
import random
from enum import Enum
from Marco import *
from Pelota import *
from Jugador1 import *
from Jugador2 import *

# El desfase es debido a que en 0 grados se voltea hacia arriba y no hacia la derecha

tiempo_anterior = 0

marco=Marco()
pelota=Pelota()
jugador1=Jugador1()
jugador2=Jugador2()

def actualizar(window):
    global tiempo_anterior

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior

    pelota.checar_colisiones(jugador1, jugador2)
    pelota.actualizar(tiempo_delta)
    jugador1.actualizar(window, tiempo_delta, pelota)
    jugador2.actualizar(window, tiempo_delta, pelota)
    tiempo_anterior = tiempo_actual


def dibujar():
    # Rutinas de dibujo
    jugador1.dibujar()
    jugador2.dibujar()
    pelota.dibujar(jugador1, jugador2)
    marco.dibujar()

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.destroy_window(window)
        glfw.terminate()

def main():
    # Inicia glfw
    if not glfw.init():
        return

    # Crea la ventana, independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    # Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    # Establecemos el contexto
    glfw.make_context_current(window)

    # Activamos la validación de funciones modernas de OpenGL
    glewExperimental = True

    # Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        # Establece regiond e dibujo
        glViewport(0, 0, 800, 800)
        # Establece color de borrado
        glClearColor(0.0, 0.5, 1.0, 1)
        # Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        actualizar(window)
        dibujar()

        # Preguntar si hubo entradas de perifericos (Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        # Intercambia los buffers
        glfw.swap_buffers(window)

    # Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    # Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()
