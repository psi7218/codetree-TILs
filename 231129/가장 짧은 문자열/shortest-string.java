import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String a = br.readLine();
        String b = br.readLine();
        String c = br.readLine();
        
        int a_length = a.length();
        int b_length = b.length();
        int c_length = c.length();
        
        int max_val = Math.max(Math.max(a_length, b_length), c_length);
        int min_val = Math.min(Math.min(a_length, b_length), c_length);
        
        System.out.print(max_val - min_val);
        
        
        
        
    }
}