/* 
Write a java program which creates class Student with attributes Rollno , Name, Number of subjects, Marks of each subject.
Write a parameterized constructor which initializes roll no, name & Number of subjects and create the array of marks dynamically.
Display the details of all students with   percentage and class obtained. Use Array of object.
*/

import java.util.Scanner;

public class DynamicInitialization
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int n_st;
	    String name;
	    int roll,num;
	    
	    System.out.print("How many students data would be entered :  ");
	    n_st = sc.nextInt();
	    
	    Student st[] = new Student[n_st];
	    
	    for (int i = 0; i < n_st; i++) {
	        System.out.println("Enter Details of " + " student" + (i + 1));
	        sc.nextLine();
	        System.out.print("Enter Name: ");
	        name = sc.nextLine();
	        System.out.print("Enter Rollno: ");
	        roll = sc.nextInt();
	        System.out.print("number of subjects : ");
	        num = sc.nextInt();
	        st[i] = new Student(name,roll,num);
	    }
	    
	    System.out.println("\n\nDisplay all students\n");
	    for (int i =0; i < n_st; i++) {
	        System.out.println("Details of student " + (i + 1));
	        st[i].display();
	    } 
	    
	}
}

class Student {
    private String name;
    int roll;
    private int num, marks[];
    private double per = 0;
    
    Student(String name, int roll, int num){
        this.name = name;
        this.roll = roll;
        this.num = num;
        marks = new int[num];
        acceptMarks();
    }
    
    void display() {
        System.out.println("Name: " + name);
        System.out.println("Rollno: " + roll);
        System.out.println("Number of subjects: " + num);
        for (int i = 0; i < num; i++) {
            System.out.println("Marks of subject " + (i + 1) + " : " + marks[i]);
        } 
        percentage();
        System.out.println("percentage: " + per);
    }
    
    void percentage() {
        for(int mark : marks) {
            per += (double) mark;
        }
        per = per / num ;
    }
    
    void acceptMarks() {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < num; i++) {
            System.out.print("Marks of subject " + (i+1) + " = ");
            marks[i] = sc.nextInt();
        } 
    
    }
}



