import java.util.*;
import java.io.*;


public class Main {




    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        int n = Integer.parseInt(br.readLine());

        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            C[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            D[i] = Integer.parseInt(st.nextToken());
        }

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
                    answer += 1;
                }
            }
        }

        System.out.println(answer);

    }
}