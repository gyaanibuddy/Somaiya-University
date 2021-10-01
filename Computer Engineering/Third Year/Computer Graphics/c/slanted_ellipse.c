// Problem Statement: Draw slanted ellipse filled with Orange colour.  

#include <GL/glut.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <conio.h>
#include "iostream"
using namespace std;
float a=0.5, b=0.25;
int h, k;
double angle = (2 * 3.14) / 1000;

void init() {
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glColor3f(0.0, 0.0, 0.0);
}


void display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 0.5, 0.0);
	glPushMatrix();
	glRotatef(60, 1.0, 1.0, 1.0);
	glBegin(GL_POLYGON);
	double ang = 0.0;
	
	for(int i = 0; i < 1000; i++)
	{

		glVertex2d(a * cos(ang), b * sin(ang));
		ang = ang + angle;
		//cout << ang << " " << a * cos(ang) << endl;
	}

	glEnd();
	glPopMatrix();
	glFlush();
}


int main(int argc, char** argv)
{
	/*printf("Enter the center of ellipse:\n");
	scanf_s("%d %d", &h, &k);*/
	/*printf("Enter the parameters a & b:\n");
	scanf_s("%f %f", &a, &b);*/
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(840, 680);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Ellipse : Polynomial Method ");
	glutDisplayFunc(display);
	init();
	glutMainLoop();
	return 0;
}
