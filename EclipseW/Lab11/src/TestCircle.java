
import java.util.Scanner;
public class TestCircle {

	public static void main(String[] args) {
		System.out.println("Enter the center coordinates and radii of two circles");
		
		
		System.out.println("Circle 1: Enter coordinates in this order: (x1 y1 rate) ");
		Scanner input = new Scanner (System.in);
		double x1 = input.nextDouble();
		double y1 = input.nextDouble();
		double r1 = input.nextDouble();
		
		System.out.println("Circle 2: Enter coordinates in this order: (x2 y2 r2) ");
		double x2 = input.nextDouble();
		double y2 = input.nextDouble();
		double r2 = input.nextDouble();
		
		Circle c1 = new Circle (r1, x1, y1);
		Circle c2 = new Circle (r2, x2, y2);
		
		System.out.println(("The distance between circle 1 with a radius of "+c1.getRadius()+" and circle 2 with a radius of "+c2.getRadius()+" is "+c1.distance(c2)));

	}

}

//-------------------------------------------------------------------------------------------------------------------

class Circle {
	private double radius, centerX, centerY;
	//private double distance;
	
	public Circle(double radius, double centerX, double centerY) {
		this.radius = radius;
		this.centerX = centerX;
		this.centerY = centerY;
	}
	public double getRadius(){
		return radius;
	}
	public double getcenterX(){
		return centerX;
	}
	public double getcenterY(){
		return centerY;
	}
	public double distance(Circle c1){
		double distance=Math.sqrt((centerX-c1.centerX)*(centerX-c1.centerX)+(centerY-c1.centerY)*(centerY-c1.centerY));
		return distance;
	}
}