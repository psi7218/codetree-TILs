import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        String a = st.nextToken();
        String b = st.nextToken();
        
        if (a.length() > b.length()) {
        	System.out.println(a + " " + a.length());
        } 
        else if (a.length() < b.length()) {
        	System.out.println(b + " " + b.length());
        }
        else {
        	System.out.print("same");
        }
        
     
        
        
        
        
    }
}