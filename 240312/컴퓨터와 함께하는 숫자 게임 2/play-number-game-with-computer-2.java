import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    static long m;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        m = Long.parseLong(br.readLine());


        long min = m;
        long max = -1;
        StringTokenizer st = new StringTokenizer(br.readLine());

        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        for (long k = a; k <= b; k++) {
            long value = binary(k);
            min = Math.min(min, value);
            max = Math.max(max, value);
        }
        System.out.println(min + " " +  max);


    }
    static long binary(long k) {
        long left = 1;
        long right = m;

        long cnt = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            if (mid == k ) {
                cnt++;
                break;
            }
            if (mid > k ) {
                right = mid - 1;
                cnt++;
            } else {
                left = mid + 1;
                cnt++;
            }

        }
        return cnt;
    }
}