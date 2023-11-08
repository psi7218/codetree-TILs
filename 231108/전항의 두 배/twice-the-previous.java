import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        System.out.print(a + " ");
        System.out.print(b + " ");
        for (int i=0; i<8; i++) {
        	int c = a*2+b;
        	System.out.print(c + " ");
        	a = b;
        	b = c;
        	
        }
        
        
    }
}