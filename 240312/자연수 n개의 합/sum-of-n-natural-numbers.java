import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Long s = Long.parseLong(br.readLine());

        long left = 1;
        long right = 2000000000;
        long answer = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            long val = mid * (mid + 1) / 2;
            if (val <= s) {
                answer = Math.max(mid,answer);
                left = mid + 1;
            } else {
                right = mid - 1;
            }

        }
        System.out.println(answer);

    }



}