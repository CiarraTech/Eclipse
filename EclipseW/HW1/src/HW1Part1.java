import java.util.Scanner;
public class HW1Part1 {

	public static void main(String[] args) {
		Scanner myInput = new Scanner(System.in);
		
	//Enter investment amount
		System.out.print("Enter investment amount: ");
		double investmentAmount=myInput.nextDouble();
		
	//Enter annual interest rate 
		System.out.println("Enter annual interest rate percentage (in decimal form): ");
		double annualInterestRate = myInput.nextDouble();

	//Obtain monthly interest rate
		double monthlyInterestRate = annualInterestRate/12; 
		
	//Enter year
		System.out.println("Enter the number of years: ");
		int year=myInput.nextInt();
	
	//Calculate payment
		double futureInvestmentValue = investmentAmount*(1+ Math.pow(1 + monthlyInterestRate, year*12 )-1); 
	 
	//Display results
	System.out.println("The future investment is "+futureInvestmentValue);
	
	}

}
