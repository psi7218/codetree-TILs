import java.io.BufferedReader;
import java.io.*;
import java.nio.Buffer;
import java.sql.SQLOutput;
import java.util.*;

public class Main {



    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        TreeMap<String,Integer> tm = new TreeMap<>();

        for (int i = 0 ; i < n; i++) {
            String word = br.readLine();
            tm.put(word, tm.getOrDefault(word, 0) + 1);
        }

        Iterator<Map.Entry<String, Integer>> it = tm.entrySet().iterator();
        while(it.hasNext()) {
            Map.Entry<String, Integer> entry = it.next();
            System.out.print(entry.getKey() + " ");
            double num = (entry.getValue() * 100) / n;
            
            String answer = String.format("%.4f", num);

            System.out.println(answer);
        }


    }

}