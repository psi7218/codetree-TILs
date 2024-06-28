import java.util.*;
import java.io.*;

public class Main {
    static int n,m;
    static int[] lst;
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        lst = new int[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            lst[i] = Integer.parseInt(st.nextToken());
        }

        int start = 1;
        int end = 100000;
        int answer = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (binary(mid) >= m) {
                start = mid + 1;
                answer = Math.max(answer, mid);
            } else {
                end = mid - 1;
            }
        }
        System.out.println(answer);
    }
    public static int binary(int num) {
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            tmp += lst[i] / num;
        }
        return tmp;
    }

}