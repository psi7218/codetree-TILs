import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());

        long left = 1;
        long right = Integer.MAX_VALUE;
        long answer = Integer.MAX_VALUE;
        while (left <= right) {
            long mid = (left + right) / 2;
            long val = mid/ 3 + mid /5 - mid /15;

            if (mid - val >= n) {
                answer = Math.min(answer, mid);
                right = mid - 1;

            } else {
                left = mid + 1;
            }
        }
        System.out.println(answer);





    }



}