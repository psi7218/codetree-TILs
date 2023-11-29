import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str = br.readLine();
        String a = br.readLine();
        char alpha = a.charAt(0);
        int length = str.length();
        int count = 0;
        
        for (int i = 0; i< length; i++) {
        	if (str.charAt(i) == alpha) {
        		count += 1;
        	}
        }
        System.out.print(count);
        
    }
}