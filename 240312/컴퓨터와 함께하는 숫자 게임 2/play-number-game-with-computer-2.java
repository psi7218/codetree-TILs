import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    static int m;
    static int[] arr;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        m = Integer.parseInt(br.readLine());
        arr = new int[m];
        for (int i = 0; i < m; i++) {
            arr[i] = i + 1;
        }
        int min = m;
        int max = -1;
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        for (int k = a; k <= b; k++) {
            int value = binary(k);
            min = Math.min(min, value);
            max = Math.max(max, value);
        }
        System.out.println(min + " " +  max);


    }
    static int binary(int k) {
        int left = 0;
        int right = m - 1;

        int cnt = 0;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (arr[mid] == k) {
                cnt += 1;
                break;
            }
            if (arr[mid] < k) {
                left = mid + 1;
                cnt++;
            } else {
                right = mid - 1;
                cnt++;
            }
        }
        return cnt;
    }
}