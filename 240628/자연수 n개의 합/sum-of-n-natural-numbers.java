import java.util.*;
import java.io.*;

public class Main {
    static long s;
    public static void main(String[] args) throws IOException{
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        s = Long.parseLong(st.nextToken());

        long start = 1;
        long end = 2000000000;
        long answer = 0;
        while (start <= end) {
            long mid = (start + end) / 2;
            if (sum(mid) <= s) {
                start = mid + 1;
                answer = Math.max(answer, mid);
            } else {
                end = mid - 1;
            }
        }
        System.out.println(answer);
    }

    public static long sum(long num) {
        long val = (num) * (num + 1) / 2;
        return val;
    }
}