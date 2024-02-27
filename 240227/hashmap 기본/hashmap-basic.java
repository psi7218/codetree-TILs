import java.util.*;
import java.io.*;



public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            int k = Integer.parseInt(st.nextToken());

            switch (cmd) {
                case "add":
                    int val = Integer.parseInt(st.nextToken());
                    hashMap.put(k, val);
                    break;
                case "find":
                    if (hashMap.containsKey(k)) {
                        System.out.println(hashMap.get(k));
                    } else {
                        System.out.println("None");
                    }
                    break;
                case "remove":
                    hashMap.remove(k);
                    break;

            }
        }

    }
}