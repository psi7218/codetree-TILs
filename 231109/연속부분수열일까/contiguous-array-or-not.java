import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n1 = Integer.parseInt(st.nextToken());
        int n2 = Integer.parseInt(st.nextToken());
        int[] arr1 = new int[n1];
        int[] arr2 = new int[n2];
        
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i< n1; i++) {
        	arr1[i] = Integer.parseInt(st1.nextToken());       	
        }
        for (int i = 0; i< n2; i++) {
        	arr2[i] = Integer.parseInt(st2.nextToken());       	
        }
        boolean check = false;
        int temp = 0;
        while (temp < n1-n2+1) {
        	boolean flag = true;
        	if (arr1[temp] == arr2[0]) {
        		for (int j = 1; j<n2; j++) {
        			if (arr1[temp+j] == arr2[0+j]) {
        				continue;
        			} else {
        				temp += j+1;
        				flag = false;
        				break;
        			}   			
        			
        		}
        		if (flag) {
        			check = true;
        			break;
        		}
        		
        		
        	} 
        	else {
        		temp += 1;
        	}
        	
        }
        
        if (check) {
        	System.out.print("Yes");
        } else {
        	System.out.print("No");
        }
    }
}