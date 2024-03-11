import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashMap<Integer, Integer> map = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
            map.put(num, i+1);
        }

        for (int j = 0; j < m; j++) {
            int k = Integer.parseInt(br.readLine());
            boolean flag = false;
            int left = 0;
            int right = n - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (arr[mid] == k) {
                    System.out.println(mid + 1);
                    flag = true;
                    break;
                }
                if (arr[mid] < k) {
                    left = mid + 1;
                } else if (arr[mid] > k) {
                    right = mid - 1;
                }
            }
            if (!flag) {
                System.out.println(-1);
            }
        }



    }
}