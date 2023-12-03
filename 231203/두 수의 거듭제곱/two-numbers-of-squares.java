import java.util.*;
import java.io.*;

public class Main {
	

	public static double func(double a, double b) {
		return Math.pow(a, b);
		
		
	}
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        double n = Double.parseDouble(st.nextToken());
        double m = Double.parseDouble(st.nextToken());
        System.out.print((int)func(n , m));
     
    }
}