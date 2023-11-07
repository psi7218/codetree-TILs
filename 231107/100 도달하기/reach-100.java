import java.util.*;
import java.io.*;


public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException{
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int first = 1;
        int second = n;
        System.out.print(first + " ");
        System.out.print(second + " ");
        while (true) {
            int temp = first + second;
            System.out.print(temp + " ");
            first = second;
            second = temp;
            if (second > 100) {
                break;
            }
        }
        

    }
}