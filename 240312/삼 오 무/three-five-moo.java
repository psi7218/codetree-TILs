import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());

        int left = 1;
        int right = 1000000000;
        int answer = 1000000000;
        while (left <= right) {
            int mid = (left + right) / 2;
            int val = mid/ 3 + mid /5 - mid /15;

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