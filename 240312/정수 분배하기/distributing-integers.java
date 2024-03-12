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
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        int max_val = 0;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[i] = num;
            if (arr[i] > max_val) {
                max_val = arr[i];
            }
        }

        int low = 1;
        int high = max_val;
        int answer = 0;
        while (low <= high) {
            int mid = (low + high) / 2;
            int total = 0;
            for (int j = 0; j < n; j++) {
                int cnt = arr[j] / mid;
                total += cnt;
            }
            if (total >= m) {
                answer = Math.max(answer, mid);
                low = mid + 1;
            } else {
                high = mid -1 ;
            }
        }

        System.out.println(answer);


    }



}