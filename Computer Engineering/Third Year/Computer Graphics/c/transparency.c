// Problem Statement: Write a program in OpenGL to Implement Transparency

// Algorithm/ Pseudocode for each process:

// We draw the two objects one by one and see to it that they overlap each other. We have predefined transparency for both the objects, once we press the ‘t’ button, we see that the objects flip their position, and hence the effect of transparency is observed.
// draw objects in a certain way
// if (pressed ‘t’)
//     swap the objects one above the other

// Implementation details:

#include <GL/glut.h>
#include <stdlib.h>
#include <conio.h>
static int leftfig = GL_TRUE;

static void init(void)
{
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glShadeModel(GL_FLAT);
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

static void drawLeftfigure(void)
{
    glBegin(GL_POLYGON);
    glColor4f(0.0, 1.0, 0.0, 0.5);
    glVertex3f(0.1, 0.1, 0.0);
    glVertex3f(0.6, 0.1, 0.0);
    glVertex3f(0.6, 0.6, 0.0);
    glVertex3f(0.1, 0.6, 0.0);
    glEnd();
}

static void drawRightfigure(void)
{

    glBegin(GL_POLYGON);
    glColor4f(1.0, 0.0, 0.0, 0.5);
    glVertex3f(0.9, 0.9, 0.0);
    glVertex3f(0.4, 0.9, 0.0);
    glVertex3f(0.4, 0.4, 0.0);
    glVertex3f(0.9, 0.4, 0.0);
    glEnd();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    if (leftfig)
    {
        drawLeftfigure();
        drawRightfigure();
    }
    else
    {
        drawRightfigure();
        drawLeftfigure();
    }
    glFlush();
}

void reshape(int w, int h)
{
    glViewport(0, 0, (GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
        gluOrtho2D(0.0, 1.0, 0.0, 1.0 * (GLfloat)h / (GLfloat)w);
    else
        gluOrtho2D(0.0, 1.0 * (GLfloat)w / (GLfloat)h, 0.0, 1.0);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 't':
    case 'T':
        leftfig = !leftfig;
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
        break;
    default:
        break;
    }
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(720, 640);
    glutCreateWindow("Transparency");
    init();
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
