### Drawing line using Digital Differential Analyzer Line Drawing Algorithm in Computer Graphics.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 25,25
m=0

def ROUND(a):
	return int(a + 0.5)

def drawDDA(x1,y1,x2,y2):
    x,y = x1,y1
    length = abs((x2-x1) if abs(x2-x1) > abs(y2-y1) else (y2-y1))
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    # print ('x = %s, y = %s' % (((ROUND(x),ROUND(y)))) )
    for i in range(length):
        a = x
        b = y
        x += dx
        y += dy
        # if(m==0):
        print ('x= %s, y = %s' % (((ROUND(x),ROUND(y)))) )
        Line(a,b,x,y)
    # m=m+1


# ---Section 1---
def Line(x1,y1,x2,y2):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    x1 = 2*x1 / w - 1
    y1 = 2*y1 / h - 1

    x2 = 2*x2 / w - 1
    y2 = 2*y2 / h - 1

    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# This alone isn't enough to draw our square

def iterate():
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


# ---Section 2---

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    # iterate()
    glColor3f(1.0, 0.0, 3.0) # Set the color to pink
    drawDDA(2,5,10,20)
    glutSwapBuffers()

#---Section 3---

glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("DDA Line Drawing Algorithm") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
