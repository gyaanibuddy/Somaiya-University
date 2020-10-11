/******************************************************************************

Write a program which stores information about n Students in a two dimensional array.
The array should contain number of rows equal to number of Students. Each row will have number
of columns equal to number of online courses completed by that Student which may vary from Student to Student.
The program should print Student number (index+1),  percentage obtained in all the online courses and average
percentage scored as output. (It is expected to assign columns to each row dynamically after getting value of
number of online courses from user. 
*******************************************************************************/
import java.util.Scanner;
public class JaggedArray
{
	public static void main(String[] args) {
		int students;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter number of students: ");
		students = sc.nextInt();
		
		int scores[][] = new int[students][];
		double avg[] = new double[students];
		
		for (int i = 0; i < scores.length; i++) {
		    System.out.println("Enter details of student " + (i+1));
		    System.out.print("No. of courses: ");
		    scores[i] = new int[sc.nextInt()];
		    avg[i] = 0;
		    for (int j = 0; j < scores[i].length; j++)  {
		        System.out.print("\tPercentage of course " + (j+1) + " : ");
		        scores[i][j] = sc.nextInt();
		        avg[i] += (double) scores[i][j];
		    }
		    avg[i] /= (double) scores[i].length;
		} 
		
		System.out.println("\nDisplaying Details of all students\n");
		
		for (int i = 0; i < scores.length; i++) {
		    System.out.println("Student " + (i+1) + " has completed " + 
		                        scores[i].length + " course" + ((scores[i].length > 1) ? "s":""));
		    for (int j = 0; j < scores[i].length; j++) {
		        System.out.println("\tPercentage of course " + (j+1) + " is " + scores[i][j] + " %");
		    } 
		    System.out.println("Averge percentage: " + avg[i] + " %");
		} 
	}
}


