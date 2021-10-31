import glfw
import numpy as np

from OpenGL.GL import *


def handleQuad():
    glfw.init()
    width = 600
    height = 800

    # creating window
    window = glfw.create_window(height, width, "QUAD", None, None)
    glfw.set_window_pos(window, 400, 300)
    glfw.make_context_current(window)

    vertice = [-0.5, 0.5, 0.0,
               0.5, 0.5, 0.0,
               0.5, -0.5, 0.0,
               -0.5, -0.5, 0.0]

    v = np.array(vertice, dtype=np.float32)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, v)
    glClearColor(0, 0, 0, 0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_QUADS, 0, 4)
        glfw.swap_buffers(window)
    glfw.terminate()


    #global window
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_QUADS, 0, 4)
        glfw.swap_buffers(window)
    glfw.terminate()


def handleRotate():
    print('Rotating')


def handleTranslation():
    print('Translation')


def handleScale():
    print('Appling scale of 1.25 for every vertice')

