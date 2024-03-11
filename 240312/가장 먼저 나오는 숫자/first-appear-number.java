import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[] arr;
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }
        st = new StringTokenizer(br.readLine());

        for (int j = 0; j < m; j++) {
            int k = Integer.parseInt(st.nextToken());
            int a = Lowerbound(k);
            int b = Upperbound(k);

            if (b - a == 0) {
                System.out.println(-1);
            } else {
                System.out.println(a + 1);
            }
        }



    }
    static int Lowerbound(int k) {
        int left = 0;
        int right = n -1;

        int minIdx = n;

        while ( left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= k) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            } else {
                left = mid + 1;
            }
        }
        return minIdx;
    }
    static int Upperbound(int k ) {
        int left = 0;
        int right = n - 1;

        int maxIdx = n;

        while ( left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] > k) {
                right = mid - 1;
                maxIdx = Math.min(maxIdx, mid);
            }
            else {
                left = mid + 1;
            }
        }
        return maxIdx;
    }
}