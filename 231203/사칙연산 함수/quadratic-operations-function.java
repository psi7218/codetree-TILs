import java.util.*;
import java.io.*;

public class Main {
	

	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        String word = st.nextToken();
        int m = Integer.parseInt(st.nextToken());
        
        
        if (word.equals("+")) {
        	System.out.print(n + " " + word + " " + m + " = " + (n+m));
        } else if (word.equals("-")) {
        	System.out.print(n + " " + word + " " + m + " = " + (n-m));
        } else if (word.equals("/")) {
        	System.out.print(n + " " + word + " " + m + " = " + (n/m));
        } else if (word.equals("*")) {
        	System.out.print(n + " " + word + " " + m + " = " + (n*m));
        } else {
        	System.out.print("False");
        }
        
    }
}