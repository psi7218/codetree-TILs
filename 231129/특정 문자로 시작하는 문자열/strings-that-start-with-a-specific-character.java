import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] arr = new String[n];
        
        for (int i = 0; i < n; i++) {
        	arr[i] = br.readLine();
        }
        char str = br.readLine().charAt(0);
        
        int length = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
        	if (arr[i].charAt(0) == str) {
        		length += arr[i].length();
        		count += 1;
        	}
        }
        double result = (float)length/(float)count;
        String result1 = String.format("%.2f", result);
        System.out.println(count + " " + result1);
    }
}