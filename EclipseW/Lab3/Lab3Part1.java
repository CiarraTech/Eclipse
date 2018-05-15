
public class Lab3Part1 
	{
	public static void main(String[] args) {
	double radius, area;
	final double PI;
	
	// Assign a radius
	radius = 20;
	
	//Assign Pi
	PI = 3.14159;
		
	// Compute area
	area = radius * radius * PI;
	
	// Display results
	System.out.println("The area for the circle of radius " + radius + " is " + area);
	
	//Assign second radius
	radius = 50;
	
	// Compute area
	area = radius * radius * PI;
		 
	//Display second results
	System.out.println("The area for the second circle of radius " + radius + " is " + area);
	
	}	
	
}