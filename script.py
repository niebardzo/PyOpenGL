import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math



def Figure(R1, R2, n, z1, z2):
    alfa = 0
    dalfa = 2 * math.pi / n
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n+1):
        glColor3fv((math.cos(alfa), math.sin(alfa) ,1))
        glVertex3fv((R1 * math.cos(alfa), R1 * math.sin(alfa), z1))
        glVertex3fv((R2 * math.cos(alfa), R2 * math.sin(alfa), z2))
        alfa += dalfa

    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -6)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,2,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-2,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)

        glRotatef(1, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        Figure(3, 2, 6, 0, 0)
        Figure(3, 2, 6, 8, 8)
        Figure(3, 3, 6, 8, 0)
        Figure(2, 2, 6, 8, 0)
        glPushMatrix()
        glRotatef(90,1,0,0)
        glTranslatef(0,4,0)
        Figure(0.3, 0.3, 40, 10, -10)
        glPopMatrix()
        glPushMatrix()
        glRotatef(90,0,1,0)
        glTranslatef(-4,0,0)
        Figure(0.3, 0.3, 40, 10, -10)
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


main()
