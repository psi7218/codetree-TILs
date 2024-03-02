import java.util.*;
import java.io.*;


public class Main {

    static HashMap<Integer, Integer> hashMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            hashMap.put(arr[i], hashMap.getOrDefault(arr[i], 0) +1);
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if(!hashMap.containsKey(arr[i])) {
                hashMap.put(arr[i], -1);
            } else {
                hashMap.put(arr[i], hashMap.get(arr[i]) -1);
            }

            for (int j = 0; j < i; j++) {
                if (hashMap.containsKey(m - arr[i] - arr[j])) {
                    answer += hashMap.get(m - arr[i] - arr[j]);
                }
            }

        }
        System.out.println(answer);


    }
}