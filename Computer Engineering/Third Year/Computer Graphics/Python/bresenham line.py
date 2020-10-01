### Drawing of line using - Bresenham's Line Drawing Algorithm Computer Graphics.

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 25,25

def drawbl(x1,y1,x2,y2): 
    dy = (y2 - y1)
    dx = (x2 - x1) 
    m_new = 2 * dy - dx 
    x = x1
    y = y1 
    # m=m+1
    while(x<=x2 and y<=y2):
        if(m_new>=0):
            # if(m<=1):
            print(x,y)
            a = x
            b = y
            x=x+1
            y=y+1
            m_new=m_new+2*dy-2*dx  
            Line(a,b,x,y)
          
        else:
            # if(m<=1):
            print(x,y)
            a = x
            b = y
            m_new=m_new+2*dy
            x=x+1 
            Line(a,b,x,y)
		
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

# ---Section 2---
def showScreen(a1,b1,a2,b2):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    #Color3f function takes the relative values of given rgb values
    glColor3f(0.0, 0.0, 1.0) # Set the color to blue
    # m=0
    # a1,b1,a2,b2= map(int, input().split())
    # drawbl(9,18,14,21)
    drawbl(a1,b1,a2,b2)
    glutSwapBuffers()

#---Section 3---
glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
a1,b1,a2,b2= map(float, input().split())
wind = glutCreateWindow("Bresenham's Line Drawing Algorithm") # Set a window title
glutDisplayFunc(showScreen(a1,b1,a2,b2))
glutIdleFunc(showScreen(a1,b1,a2,b2)) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
