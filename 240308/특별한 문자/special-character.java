import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException, NumberFormatException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        HashMap<Character, Integer> map = new HashMap<>();
        ArrayList<Character> arr = new ArrayList<>();
        for (int i = 0; i < word.length(); i++) {
            char key = word.charAt(i);
            map.put(key, map.getOrDefault(key,0) + 1);
            if (map.get(key) == 1) {
                arr.add(key);
            }
        }
        boolean flag = false;
        for (Character ch : arr) {
            if (map.get(ch) == 1) {
                System.out.println(ch);
                flag = true;
                break;
            }
        }
        if (!flag) {
            System.out.println("None");
        }
    }
}