import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Long n = Long.parseLong(br.readLine());

        long left = 1;
        long right = n;
        long answer = n;
        while (left <= right) {
            long mid = (left + right) / 2;
            long val = mid * (mid + 1) / 2;
            if (val > n) {
                answer = Math.min(mid,answer) - 1;
                right = mid - 1;
            } else {

                left = mid + 1;
            }

        }
        System.out.println(answer);

    }



}