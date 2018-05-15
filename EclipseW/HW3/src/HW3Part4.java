
public class HW3Part4 {
	 public static void main(String[] args) {
		 int i = 7; 
	 	Hw3Part4(i-1);
	 }
	 	// n is i | i is j | j is c
		
	public static void Hw3Part4 (int i){
		for(int j = 1; j <= i; j++){
		   
			for (int c = i; c > 0; c--){
				if (c <=j)
		
		        System.out.print(c);
				else
		        System.out.printf(" ");
		    }
		    System.out.print("\n");
		    
		   
		}
	}
}
 

