/*
•Create a Class StringManipulation with following member functions.
–FindFrequencyCount() :
the function will accept any word and will display the total number of appearances of the given word in the String.
(Using string class)
–ReplaceCharacter() :
the function will replace the first character of the string by its equivalent upper case. (using stringBuffer class).
*/
import java.util.Scanner;
class Main
{
	public static void main(String[] args) {
	    
	    Scanner sc = new Scanner(System.in);
	    int choice = 0;
	    String str = "",word;
	    StringManipulation sm = new StringManipulation();
	    
	    while(choice!=3) {
	        //sc.nextLine();
	        
	        System.out.println("1. To count the appearances of the word in the string");
	        System.out.println("2. To convert the first character of each word in string to uppercase");
	        System.out.println("3. Quit");
	        System.out.println("Enter choice: ");
	        choice = sc.nextInt();
	        System.out.println("Enter the String:   ");
	        sc.nextLine();
	        switch(choice){
	            case 1:
	                //sc.nextLine();
	                word = sc.nextLine();
	                sm.FindFrequencyCount(word, str);
	                break;
	            case 2:
	                sm.ReplaceCharacter(str);       
	        }
	    }
	}
}

class StringManipulation {
    
    void FindFrequencyCount(String word, String str){
        int count = 0, len = word.length();
        
        for (int i = 0; i < str.length(); i++) 
            if(word.equals(str.substring(i, i + len)))
                count++;
        System.out.println("Count of " + word + " in given string: " + str + " = " + count);    
    }
    
    void ReplaceCharacter(String str) {
        StringBuffer new_str = new StringBuffer(""), temp;
        String str_arr[] = str.split("\\s+");
        for (int i = 0; i < str_arr.length; i++) {
            temp = new StringBuffer(str_arr[i]);
            temp.replace(0,1,str_arr[i].substring(0,1).toUpperCase());
            new_str.append(temp);
            new_str.append(" ");
        } 
        
        System.out.println("New string: " + new_str.toString());
    }
}

