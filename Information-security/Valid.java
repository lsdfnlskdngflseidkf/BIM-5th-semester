import java.util.Set;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class Valid {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter the Keyword");
            String kw = sc.next().toLowerCase();
            kw = kw.replaceAll("\\s", "");
            kw = kw.replaceAll("j", "i");
            Set<Character> keyword = new LinkedHashSet<>();
            for (int i = 0; i < kw.length(); i++) {
                if (keyword.add(kw.charAt(i))) {
                }
            }
            kw = keyword.toString();
            String alphabets = "abcdefghiklmnopqrstuvwxyz";
            boolean[] ispresent = new boolean[26];
            Arrays.fill(ispresent, false);

            for (int i = 0; i < alphabets.length(); i++) {
                if (kw.indexOf(alphabets.charAt(i)) != -1) {
                    ispresent[i] = true;
                }
            }

            System.out.println(kw);
            int kwi = 0;
            // adding the keyword to the matrix
            char[][] key = new char[5][5];
            for (int i = 0; i < 5; i++) {

                for (int j = 0; j < 5; j++) {
                    if (kwi > kw.length()) {
                        key[i][j] = kw.charAt(kwi);
                        kwi++;
                    } else {
                        break;
                    }
                }
                if (!(kwi > kw.length())) {
                    break;
                }
            }
            // adding the remaining
            char next = ' ';
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (key[i][j] != '\u0000') {
                        continue;
                    } else {
                        for (int k = 0; k < alphabets.length(); k++) {
                            if (ispresent[k]) {
                                continue;
                            } else {
                                next = alphabets.charAt(k);
                                ispresent[k] = true;
                            }
                        }
                        key[i][j] = next;
                    }
                }
            }
            System.out.println(Arrays.deepToString(key));
        } finally {
            sc.close();
        }
    }
}
