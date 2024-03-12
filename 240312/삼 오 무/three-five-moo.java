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
        int answer = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            int val = mid - mid/3 - mid / 5 ;

            if (val == n) {
                answer = mid;
                break;
            } else if (val < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(answer);





    }



}