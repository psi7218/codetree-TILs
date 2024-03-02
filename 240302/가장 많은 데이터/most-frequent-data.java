import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<String, Integer> hashMap = new HashMap<>();
        int max_val = 0;
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            int currentValue = hashMap.getOrDefault(word, 0);
            hashMap.put(word, currentValue +1);
            if (currentValue +1 > max_val) {
                max_val = currentValue + 1;
            }
        }
        System.out.println(max_val);


    }
}