import java.util.*;
import java.io.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] arr = new int[]{0,0,0,0,0,0,0,0,0};
        
        for (int i=0; i<n; i++) {
        	int val = Integer.parseInt(st.nextToken());
        	
        	arr[val-1] += 1;
        	
        }
        for (int i=0; i<9; i++) {
        	System.out.println(arr[i]);
        }
    }
}