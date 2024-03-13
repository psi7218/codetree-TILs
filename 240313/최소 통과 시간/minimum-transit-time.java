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

        int left = 1;
        int right = 1000000000;
        int answer = 1000000000;
        arr = new int[m];
        for ( int i = 0; i < m; i++ ) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        while ( left <= right ) {
            int mid = ( left + right ) / 2;

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

    static boolean func(int time) {
        int cnt = 0;

        for (int j = 0; j < m; j++) {
            cnt += time / arr[j] ;
        }

        return cnt >= n;
    }
}