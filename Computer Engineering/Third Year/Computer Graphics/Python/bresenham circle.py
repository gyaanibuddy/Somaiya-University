### Drawing circle using Bresenham's Circle Drawing Algorithm in Computer Graphics.


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 200,200

def drawbl(x1,y1,r): 
    x = 0
    y = r
    d = 3 - 2*r
    while(x <= y):
        a = x
        b = y
        if (d<0): 
            x=x+1
            y = y
            d = d + 4*x + 6
        else: 
            x=x+1
            y = y - 1
            d = d + 4*(x - y) + 10
        # 1st Quadrant
        Line(a+100,b+100,x+100,y+100)
        Line(b+100,a+100,y+100,x+100)
        # 2nd Quadrant
        Line(-a+100,b+100,-x+100,y+100)
        Line(-b+100,a+100,-y+100,x+100)
        # 3rd Quadrant
        Line(-a+100,-b+100,-x+100,-y+100)
        Line(-b+100,-a+100,-y+100,-x+100)
        # 4th Quadrant
        Line(a+100,-b+100,x+100,-y+100)
        Line(b+100,-a+100,y+100,-x+100)

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
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    #Color3f function takes the relative values of given rgb values
    glColor3f(0.0, 0.0, 1.0) # Set the color to blue
    # m=0
    # a1,b1,a2,b2= map(int, input().split())
    drawbl(50,50,50)
    # drawbl(a1,b1,a2,b2)
    glutSwapBuffers()

#---Section 3---
glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
# x,y,r= map(float, input().split())
wind = glutCreateWindow("Bresenham's Circle Drawing Algorithm") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
