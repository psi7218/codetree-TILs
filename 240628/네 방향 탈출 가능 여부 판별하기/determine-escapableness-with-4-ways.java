java.io.*;
java.util.*;

public class Main {
    static int n, m;
    static int[][] arr;
    static boolean[][] visited;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        visited = new boolean[n][m];

        for (int i=0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }



    }

    public static void bfs() {
        Deque<int[]> q = new ArrayDeque<>();
    }

}