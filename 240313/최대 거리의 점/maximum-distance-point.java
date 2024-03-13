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

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr,0,n);

        int left = 0;
        int right = 1000000000;
        int answer = 0;

        while ( left <= right ) {
            int mid = (left + right) / 2;
            if ( func(mid) ) {
                left = mid + 1;
                answer = Math.max(answer, mid);
            }
            else {
                right = mid - 1;
            }

        }


    }
    static boolean func(int dist) {
        int cnt = 1;
        int currentIdx = 0;

        for (int i = 1; i < n; i++) {
            if (arr[i] - arr[currentIdx] >= dist) {
                cnt ++;
                currentIdx = i;
            }
        }
        return cnt >= m;
    }
}