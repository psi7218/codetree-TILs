import java.util.*;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String str = br.readLine().replaceAll(" ","");
        String str1 = br.readLine().replaceAll(" ","");
        
        System.out.print(str+str1);
        
        
        
    }
}