import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        String[] arr = new String[10];
        for (int i = 0 ; i < 10; i++) {
        	arr[i] = st.nextToken();
        	if ((i+1)%2 == 1) {
        		System.out.println(arr[i]);
        	}
        	
        }
        
    }
}