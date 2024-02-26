import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class Node {
    String data;
    Node prev, next;

    public Node(String data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }

    public void insertPrev(String word, Node cNode) {
        Node newNode = new Node(word);
        newNode.next = cNode;
        newNode.prev = cNode.prev;

        if (newNode.prev != null) {
            newNode.prev.next = newNode;
        }
        cNode.prev = newNode;

    }
    public void insertNext(String word, Node cNode) {
        Node newNode = new Node(word);
        newNode.prev = cNode;
        newNode.next = cNode.next;

        if (newNode.next != null) {
            newNode.next.prev = newNode;
        }
        cNode.next = newNode;
    }

    public void print(Node node) {
        if (node.prev != null) {
            System.out.print(node.prev.data);
        } else {
            System.out.print("(Null)");
        }
        System.out.print(" " + node.data + " ");
        if (node.next != null) {
            System.out.println(node.next.data);
        } else {
            System.out.println("(Null)");
        }

    }
}

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String S_init = br.readLine();

        Node node = new Node(S_init);

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            switch (num) {
                case 1:
                    String word = st.nextToken();
                    node.insertPrev(word, node);
                    node.print(node);
                    break;
                case 2:
                    String word1 = st.nextToken();
                    node.insertNext(word1, node);
                    node.print(node);
                    break;
                case 3:
                    if (node.prev != null) {
                        node = node.prev;
                    }
                    node.print(node);
                    break;
                case 4:
                    if (node.next != null) {
                        node = node.next;
                    }
                    node.print(node);
                    break;
            }

        }



    }
}