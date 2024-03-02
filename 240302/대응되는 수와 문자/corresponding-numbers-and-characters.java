import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        HashMap<Integer, String> hashMap = new HashMap<>();
        HashMap<String, Integer> hashMap1 = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            String word = br.readLine();
            hashMap1.put(word, i);
            hashMap.put(i, word);
        }

        for (int j = 0; j < m; j ++) {
            String input = br.readLine();
            try {
                int number = Integer.parseInt(input);
                System.out.println(hashMap.get(number));
            } catch (NumberFormatException e){
                System.out.println(hashMap1.get(input));
            }
        }


    }
}