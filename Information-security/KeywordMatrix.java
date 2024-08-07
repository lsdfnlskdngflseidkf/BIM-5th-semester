import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;
import java.util.Set;

public class KeywordMatrix {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter the Keyword");
            String kw = sc.next().toLowerCase();
            kw = kw.replaceAll("\\s", "");
            kw = kw.replaceAll("j", "i");
            Set<Character> keyword = new LinkedHashSet<>();
            for (int i = 0; i < kw.length(); i++) {
                keyword.add(kw.charAt(i));
            }
            StringBuilder sb = new StringBuilder();
            for (Character ch : keyword) {
                sb.append(ch);
            }
            kw = sb.toString();

            String alphabets = "abcdefghiklmnopqrstuvwxyz";
            boolean[] ispresent = new boolean[26];
            Arrays.fill(ispresent, false);

            for (int i = 0; i < kw.length(); i++) {
                char ch = kw.charAt(i);
                ispresent[alphabets.indexOf(ch)] = true;
            }
            StringBuilder s = new StringBuilder();

            for (int i=0;i<alphabets.length();i++){
                if(!ispresent[i]){
                    s.append(alphabets.charAt(i));
                }
            }
            alphabets=s.toString();
            // adding the keyword to the matrix
            char[][] key = new char[5][5];
            int kwi = 0;
            outerloop: for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (kwi < kw.length()) {
                        key[i][j] = kw.charAt(kwi);
                        ispresent[alphabets.indexOf(kw.charAt(kwi))] = true;
                        kwi++;
                    } else {
                        break outerloop; // Break out of both loops when all keyword chars are inserted
                    }
                }
            }

            // adding the remaining characters from alphabets
            int alphIndex = 0;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (key[i][j] == '\u0000') {
                        key[i][j] = alphabets.charAt(alphIndex++);
                    }
                }
            }

            // Print the key matrix
            for (int i = 0; i < 5; i++) {
                System.out.println(Arrays.toString(key[i]));
            }
        } finally {
            sc.close();
        }
    }
}
