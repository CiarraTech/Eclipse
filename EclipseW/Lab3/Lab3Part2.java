import java.util.Scanner;
public class Lab3Part2 {
	public static void main(String[] args)	{ 
	
	int num=0;
	Scanner myInput = new Scanner(System.in);
		
	System.out.print("Enter an interger: ");
	num=myInput.nextInt();
				
	if (num%5==0)
		if (num%6==0)
			System.out.println (num+" is divisible by 5 and 6.");
		else
			System.out.println(num+" is divisible only by 5.");
		else if (num%6==0)
			System.out.println(num+" is divisible only by 6.");
	else 
		System.out.println(num+" is divisible by neither 5 or 6.");
	}
}
