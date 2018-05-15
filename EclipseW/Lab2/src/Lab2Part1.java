
import java.util.Scanner;
public class Lab2Part1 {
	public static void main(String[] args) {
		Scanner myInput = new Scanner(System.in);
		
		System.out.print("Enter num1: ");
		int num1 = myInput.nextInt();
		
		System.out.print("Enter num2: ");
		int num2 = myInput.nextInt();
		
		int temp = 0;
		
		temp = num1;
		num1=num2;
		num2=temp;		
		
		if(num1>num2)
		{
			temp = num1;
			num1=num2;
			num2=temp;	
		
		}
		
		System.out.println( "\nThe sorted numbers are: " + num1+", "+num2);	
			
	}

} 