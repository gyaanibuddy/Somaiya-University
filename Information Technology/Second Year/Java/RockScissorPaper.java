/*
Write a program that simulates a game Rock-Scissor-Paper. Assume that input given by user is correct.
Consider following  conditions 
a. Rock breaks Scissors(Rock wins)
b.Paper covers Rock(Paper wins)
c. Scissor cuts Paper(Scissors wins)
*/

import java.util.Scanner;
import java.util.Random;

public class RockScissorPaper
{
    static int user_sc = 0, pc_sc = 0;
	static String[] arr = {"rock","paper","scissor"};
    
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String name;
		char con;
		int choice, ran;
		Random r = new Random();

		System.out.println("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n");
		
		System.out.println("Enter user name: ");
		name = sc.nextLine();
		
		while(true) {
		    System.out.println("Enter choice \n 0. Rock \n 1. paper \n 2. scissor \n");
		    
		    System.out.println(name + " turn: ");
		    choice = sc.nextInt();
		    System.out.println(name + " choice is: " + arr[choice]);
		    ran =r.nextInt(3);
		    System.out.println("Computer choice is: "+ ran +" " + arr[ran]);
		    compare(choice, ran, name);
		    
		    System.out.println("do you want to play again? (Y/N)");
		    sc.nextLine();
		    con = sc.next().charAt(0);
		    if(con == 'n' || con == 'N') {
				System.out.println("Final score \n" + name + " : " + user_sc + "\t Computer : " + pc_sc);
		        break;
			}    
		    
		}
	}
	
	static void compare(int u,int p,String name) {
	    String user = arr[u], pc = arr[p];
	    if(user == pc) {
	        System.out.println("It's a tie");
	    }else if(user == "rock") {
	        if(pc == "paper"){
	            System.out.println("Computer wins");
	            pc_sc++;
	        }else{
	            System.out.println(name + " wins");
	            user_sc++;
	        }
	    }else if(user == "paper"){
	        if(pc == "rock"){
	            System.out.println(name + " wins");
	            user_sc++;
	        }else{
	            System.out.println("Computer wins");
	            pc_sc++;
	        }
	    }else {
	        if(pc == "rock"){
	            System.out.println("Computer wins");
	            pc_sc++;
	        }
	        else{
	            System.out.println(name + " wins");
	            user_sc++;
	        }
	    }
	}
}



