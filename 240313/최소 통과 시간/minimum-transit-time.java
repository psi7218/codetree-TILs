import java.io.*;
import java.util.*;



public class Main {

    static int n, m;
    static int[] arr;
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        long left = 1;
        long right = 100000000000000L;
        long answer = 100000000000000L;
        arr = new int[m];
        for ( int i = 0; i < m; i++ ) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        while ( left <= right ) {
            long mid = ( left + right ) / 2;

            if (func(mid)) {
                right = mid - 1;
                answer = Math.min(answer, mid);
            }
            else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    static boolean func(long time) {
        long cnt = 0;

        for (int j = 0; j < m; j++) {
            cnt += time / arr[j] ;
        }

        return cnt >= n;
    }
}