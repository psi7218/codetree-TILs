import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
       
        String[] arr = new String[10];
        for (int i = 0 ; i < 10; i++) {
        	arr[i] = br.readLine();
        }
        String word = br.readLine();
        char a = word.charAt(0);
        int count = 0;
        for (int i=0; i < 10; i++) {
        	if (arr[i].charAt(arr[i].length()-1) == a) {
        		System.out.println(arr[i]);
        		count += 1;
        	}
        }
        if (count == 0) {
        	System.out.print("None");
        }
    }
}