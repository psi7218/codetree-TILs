import java.util.*;
import java.io.*;

public class Main {
	

	public static void func(int m) {
		StringBuilder sb = new StringBuilder();
		int count = 1;
		for (int i = 0; i < m; i++) {
			int[] arr = new int[4];
			for (int j = 0; j < m; j++) {
				
				sb.append(count + " ");
				count += 1;
				if (count == 10) {
					count = 1;
				}
			}
			sb.append("\n");
		}
		
		System.out.print(sb);
	}
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        func(n);
        
     
    }
}