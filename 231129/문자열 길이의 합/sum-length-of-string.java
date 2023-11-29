import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        
        int count = 0;
        int a_count = 0;
        for (int i = 0; i < n; i++) {
        	arr[i] = br.readLine();
        	count += arr[i].length();
        	
        	if (arr[i].charAt(0) == 'a' ) {
        		a_count += 1;
        	}
        	
        }
        System.out.print(count + " " + a_count);
        
    }
}