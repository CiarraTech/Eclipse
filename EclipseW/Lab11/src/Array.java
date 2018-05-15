import java.util.Scanner;


public class Array {

	public static void main(String[] args) {

		Scanner input= new Scanner(System.in);
		
		System.out.println("Enter 5 numbers: ");
		
		 int[] arr1 = new int[5];
		 arr1[0] = input.nextInt();
		 arr1[1] = input.nextInt();
		 arr1[2] = input.nextInt();
		 arr1[3] = input.nextInt();
		 arr1[4] = input.nextInt();
	     int[] arr2 = new int[5];
	     for(int i=0; i<=4; i++){
		    arr2[i] = arr1[i];
		    System.out.println(arr2[i]);
		 }
  }
}

	