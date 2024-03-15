import java.io.BufferedReader;
import java.io.*;
import java.util.*;

public class Main {

    static int n,T_max;
    static int[] arr;
    static Deque<Integer> dq;
    static PriorityQueue<Integer> pq;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());




        n = Integer.parseInt(st.nextToken());
        T_max = Integer.parseInt(st.nextToken());

        arr = new int[n];

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
        }



        int low = 1;
        int high = n;
        int answer = n;
        while (low <= high) {
            int mid  = ( low + high ) / 2;
            if (func(mid)) {
                high = mid - 1;
                answer = Math.min(answer,mid);
            } else {
                low = mid + 1;
            }
        }
        System.out.println(answer);
        

    }
    static boolean func(int mid) {
        pq = new PriorityQueue<>();

        for (int i = 0; i < mid; i++) {
            pq.add(arr[i]);
        }
        for (int j = mid; j < n; j++) {
            int time = pq.poll();

            pq.add(arr[j] + time);
        }
        int check = 0;
        while (!pq.isEmpty()) {
            check = Math.max(check, pq.poll() );
        }

        return check <= T_max;
    }

}