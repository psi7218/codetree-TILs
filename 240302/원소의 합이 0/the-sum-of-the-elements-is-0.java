import java.util.*;
import java.io.*;


public class Main {




    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int n = Integer.parseInt(br.readLine());

        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];
        func(A, br.readLine(),n);
        func(B, br.readLine(),n);
        func(C, br.readLine(),n);
        func(D, br.readLine(),n);

        for (int i = 0; i < n; i++) {
            for ( int j = 0; j < n; j++) {
                int key = A[i] + B[j];
                hashMap.put(key, hashMap.getOrDefault(key, 0) +1);
            }
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for ( int j = 0; j < n; j++) {
                int value = - C[i] - D[j];
                if (hashMap.getOrDefault(value, 0) > 0) {
                    answer += hashMap.get(value);
                }
            }
        }

        System.out.println(answer);

    }

    static void func(int[] arr, String input, int n) {
        StringTokenizer st = new StringTokenizer(input);
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }
}