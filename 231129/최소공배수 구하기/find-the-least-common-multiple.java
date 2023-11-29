import java.util.*;
import java.io.*;

public class Main {
	

	public static void func(int a, int b) {
		int result = 1;
		for (int i = 2; i <= a; i++) {
			while (true) {
				if (a%i == 0 && b%i ==0) {
					result *= i;
					a /= i;
					b /= i;
				}
				else {
					break;
				}
			}
		}
		System.out.print(result * a * b);
		
		
	}
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        if (n>m) {
        	func(m,n);
        }
        else {
        	func(n,m);
        }
     
    }
}