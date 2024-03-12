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

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1 ; i <= n; i++) {
            int num = Integer.parseInt(st.nextToken());

            tm.put(num, tm.getOrDefault(num, i));
        }

        Iterator<Map.Entry<Integer, Integer>> it = tm.entrySet().iterator();
        while(it.hasNext()) {
            Map.Entry<Integer, Integer> entry = it.next();
            System.out.println(entry.getKey() + " " + entry.getValue());;
        }


    }

}