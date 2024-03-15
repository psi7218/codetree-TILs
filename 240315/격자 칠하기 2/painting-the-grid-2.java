import java.io.BufferedReader;
import java.io.*;
import java.util.*;

public class Main {

    static int n,T_max;
    static int[][] arr, visited;
    static Deque<Integer> dq;
    static PriorityQueue<Integer> pq;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        StringTokenizer st;
        int left = 0;
        int right = 0;
        int answer = 0;
        for (int i = 0; i< n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int num = Integer.parseInt(st.nextToken());

                arr[i][j] = num;
                right = Math.max(right, num);
                answer = Math.max(answer, num);
            }
        }
        while (left <= right) {
            int mid = ( left + right ) / 2;
            if (func(mid)) {
                right = mid - 1;
                answer = Math.min(answer, mid);
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
    static boolean func(int mid) {
        visited = new int[n][n];
        int max_val = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] != 1) {
                    max_val = Math.max(max_val,bfs(i,j, mid));
                }
            }
        }
        return max_val >= n * n / 2;
    }

    static int bfs(int i , int j, int mid) {
        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[]{i,j});
        int cnt = 1;
        visited[i][j] = 1;
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        while (!dq.isEmpty()) {
            int[] node = dq.poll();
            int x = node[0];
            int y = node[1];

            for (int k = 0; k <4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[nx][ny] == 1) {
                    continue;
                }
                if (Math.abs(arr[nx][ny] - arr[x][y]) <= mid) {
                    dq.add(new int[]{nx,ny});
                    visited[nx][ny] = 1;
                    cnt ++;
                }
            }
        }
        return cnt;
    }
}