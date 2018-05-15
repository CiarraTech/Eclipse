package HW4;
import java.util.Date;

public class Account {
	private int id=0;
	private double balance=0.0;
	private double annualInterestRate=0.0;
	Date dateCreated; 
	
	Account(){
		}
	Account(int newId, double newBalance){
		id= newId;
		balance=newBalance;
		dateCreated= new Date();
	}
	Account(int newId, double newBalance, double newAnnualInterestRate){
		id = newId;
		balance = newBalance;
		annualInterestRate = newAnnualInterestRate;
	}
	public int getId(){
		return id;
		}
	
	public double getBalance(){
		return balance;
		}
	
	public double getAnnualInterestRate(){
		return annualInterestRate;
		}
    public void setId(int newId){
		id= newId;
	}
	public void setBalance(double newBalance){
		balance= newBalance;
	}
	public void setAnnualInterestRate(double newAnnualInterestRate){
		annualInterestRate= newAnnualInterestRate;
	}
	public Date getDateCreated(){
		return dateCreated ;
	}
	double getMonthlyInterestRate(){
		return (annualInterestRate/12); 
	}
	double withdraw(int amount){
		return balance= balance- amount;
	}
	double deposit(int amount){
		return balance=balance+amount;
	}
	
	
}


 class Test {
  public static void main (String[] args) {
    Account account = new Account(1122, 20000);
    account.setAnnualInterestRate(4.5);
    
    account.withdraw(2500);
    account.deposit(3000);
    System.out.println("Balance is " + account.getBalance());
    System.out.println("Monthly interest is " +
      account.getMonthlyInterestRate());
    System.out.println("This account was created at " +
      account.getDateCreated());
  }
}


	