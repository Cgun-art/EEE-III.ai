import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import time
import threading

def draw_cube():
    """
    Draws a red cube with vertices and colors.
    """
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    # RGB color for red
    colors = (
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0),
        (1, 0, 0)
    )

    glBegin(GL_QUADS)
    for i, vertex in enumerate(vertices):
        glColor3fv(colors[i])  # Set the color for each vertex
        glVertex3fv(vertex)
    glEnd()

def main():
    """
    Initializes Pygame, sets up the display, and runs the main loop
    to continuously spin, disappear, and reappear the cube.
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Spinning Red Cube") # set the window title

    glEnable(GL_DEPTH_TEST)  # Enable depth testing for proper 3D rendering
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Set perspective
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)  # Translate the scene back a bit

    angle = 0
    cube_visible = True #make the cube visible

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear color and depth buffers
        glRotatef(angle, 1, 1, 1)  # Rotate the cube

        if cube_visible:
            draw_cube()  # Draw the cube
        pygame.display.flip()  # Update the display

        angle += 1
        time.sleep(0.001)  # Control the speed of rotation and blinking.

        cube_visible = not cube_visible #toggle visibility
        # The time.sleep(0.001) already provides a very fast blinking effect.
        # No need for a separate thread or very small sleep.

if __name__ == "__main__":
    main()

