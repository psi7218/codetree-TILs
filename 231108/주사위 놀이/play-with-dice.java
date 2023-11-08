import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] arr = new int[]{0,0,0,0,0,0};
        
        for (int i=0; i<10; i++) {
        	int val = Integer.parseInt(st.nextToken());
        	
        	arr[val-1] += 1;
        	
        }
        for (int i=0; i<6; i++) {
        	System.out.println(i+1 + " - " + arr[i]);
        }
    }
}