import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n-1; j++) {
                for (int k = j; k < n-2; k ++){
                    int num = arr[i] + arr[j] + arr[k];
                    hashMap.put(num, hashMap.getOrDefault(num,0) + 1);
                }
            }
        }

        System.out.println(hashMap.get(m));
    }
}