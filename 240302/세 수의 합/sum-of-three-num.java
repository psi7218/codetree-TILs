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
        }
        func(0,n,0,0,arr);
        System.out.println(hashMap.get(m));
    }

    static void func(int x, int n, int count,int sum, int[] arr) {
        if (count == 3) {
            hashMap.put(sum, hashMap.getOrDefault(sum, 0) +1);
            return;
        }
        for (int i = x; i < n-2+count; i++) {
            func(i+1, n, count + 1, sum + arr[i], arr);
        }
    }

}