import java.util.*;
import java.io.*;



public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[100001];
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < n; i++) {
            int key = Integer.parseInt(st.nextToken());
            int currentValue = hashMap.getOrDefault(key,0);
            hashMap.put(key, currentValue+1);
        }
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int question = Integer.parseInt(st.nextToken());
            if (0 == hashMap.getOrDefault(question,0)) {
                System.out.print(0 + " ");
            } else {
                System.out.print(hashMap.get(question) + " ");
            }
        }




    }
}