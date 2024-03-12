import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        TreeMap<Integer,Integer> tm = new TreeMap<>();

        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String word = st.nextToken();
            switch (word) {
                case "add":
                    int key = Integer.parseInt(st.nextToken());
                    int value = Integer.parseInt(st.nextToken());
                    tm.put(key, value);
                    break;
                case "find":
                    int key1 = Integer.parseInt(st.nextToken());
                    int check = tm.getOrDefault(key1, 0);
                    if (check == 0) {
                        System.out.println("None");
                    } else {
                        System.out.println(check);
                    }
                    break;
                case "remove":
                    int key2 = Integer.parseInt(st.nextToken());
                    tm.remove(key2);
                    break;
                case "print_list":
                    Iterator<Map.Entry<Integer,Integer>> it = tm.entrySet().iterator();
                    boolean check1 = false;
                    while(it.hasNext()) {
                        Map.Entry<Integer,Integer> entry = it.next();
                        System.out.print(entry.getValue() + " ");
                        check1 = true;
                    }
                    if (!check1) {
                        System.out.print("None");
                    }
                    System.out.println();
            }
        }

    }

}