import glfw
import numpy as numpy

from OpenGL.GL import *


def drawQuadrilateral():
    # initializing glfw
    glfw.init()
    width = 600
    height = 800

    # creating window
    window = glfw.create_window(height, width, "MOJO", None, None)
    glfw.set_window_pos(window, 400, 300)
    glfw.make_context_current(window)

    vertice = [-0.5, 0.5, 0.0,
               0.5, 0.5, 0.0,
               0.5, -0.5, 0.0,
               -0.5, -0.5, 0.0]

    v = numpy.array(vertice, dtype=numpy.float32)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, v)
    glClearColor(0, 0, 0, 0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glfw.swap_buffers(window)
    glfw.terminate()
