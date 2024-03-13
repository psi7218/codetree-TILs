import java.io.*;
import java.util.*;



public class Main {
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Long n = Long.parseLong(br.readLine());
        Long k = Long.parseLong(br.readLine());

        long left = 1;
        long right = n * n ;
        long answer = n * n;
        while (left <= right) {
            long mid = (left + right) / 2;

            long cnt = 0;
            for (int i = 1; i <= n; i++) {
                cnt += Math.min(n, mid / i) ;
            }
            if (cnt >= k) {
                right = mid - 1;
                answer = Math.min(answer, cnt);
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);

    }
}