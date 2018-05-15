package HW4;

public class Rectangle {

	double width = 1;
	double height = 1;
	
	
	Rectangle(double newWidth, double newHeight){
		width=newWidth;
		height=newHeight;
		
	}
	public double getArea(){
		double area=width*height;
		return area;
	}
	public double getPerimeter(){
		double perimeter=2*width+2*height;
		return perimeter;
	
	}
} 

 class Test3{
	  public static void main(String[] args) {

	    Rectangle myRectangle = new Rectangle(4, 40);

	    System.out.println("The area of a rectangle with width " +
	      myRectangle.width + " and height " +
	      myRectangle.height + " is " +
	      myRectangle.getArea());

	    System.out.println("The perimeter of a rectangle is " +
	      myRectangle.getPerimeter());

	    Rectangle yourRectangle = new Rectangle(3.5, 35.9);

	    System.out.println("The area of a rectangle with width " +
	      yourRectangle.width + " and height " +
	      yourRectangle.height + " is " +
	      yourRectangle.getArea());

	    System.out.println("The perimeter of a rectangle is " +
	      yourRectangle.getPerimeter());
	  }
	} 
