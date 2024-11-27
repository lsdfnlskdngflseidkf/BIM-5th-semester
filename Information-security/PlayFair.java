import java.util.Scanner;

public class PlayFair {

    public char[][] key;

    public static String cleanInput(String input) {
        return input
            .toLowerCase()
            .replaceAll("[^a-z]", "")
            .replaceAll("j", "i");
    }

    public int[] findCharIndex(char target) {
        for (int i = 0; i < key.length; i++) {
            for (int j = 0; j < key[i].length; j++) {
                if (key[i][j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] { -1, -1 };
    }

    PlayFair(char[][] userkey) {
        this.key = userkey;
    }

    public String validate(String plain) {
        StringBuilder sb = new StringBuilder();
        int modcount = 0, i = 0;
        for (i = 0; i < plain.length() - 1; i += 2) {
            sb.append(plain.charAt(i));
            if (plain.charAt(i) == plain.charAt(i + 1) && modcount % 2 != 1) {
                sb.append('x');
                modcount++;
            }
            sb.append(plain.charAt(i + 1));
        }
        if (plain.length() % 2 == 1) {
            sb.append(plain.charAt(plain.length() - 1));
        }
        plain = sb.toString();
        if (plain.length() % 2 != 0) {
            sb.append('x');
            plain = sb.toString();
        }
        return plain;
    }

    public String processText(String text, boolean isEncrypt) {
        StringBuilder result = new StringBuilder();
        int shift;
        if (isEncrypt) {
            shift = 1;
        } else {
            shift = 4;
        }
        for (int i = 0; i < text.length(); i += 2) {
            int[] index1 = findCharIndex(text.charAt(i));
            int[] index2 = findCharIndex(text.charAt(i + 1));

            if (index1[0] == index2[0]) { // Same row
                index1[1] = (index1[1] + shift) % 5;
                index2[1] = (index2[1] + shift) % 5;
            } else if (index1[1] == index2[1]) { // Same column
                index1[0] = (index1[0] + shift) % 5;
                index2[0] = (index2[0] + shift) % 5;
            } else { // Rectangle rule
                int temp = index1[1];
                index1[1] = index2[1];
                index2[1] = temp;
            }
            result.append(this.key[index1[0]][index1[1]]);
            result.append(this.key[index2[0]][index2[1]]);
        }
        return result.toString();
    }

    public String encrypt(String plain) {
        return processText(plain, true);
    }

    public String decrypt(String cipher) {
        return processText(cipher, false);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter the plaintext");
        char[][] thekey = {
            { 'u', 'i', 'w', 'a', 'l' },
            { 'b', 'c', 'd', 'e', 'f' },
            { 'g', 'h', 'k', 'm', 'n' },
            { 'o', 'p', 'q', 'r', 's' },
            { 't', 'v', 'x', 'y', 'z' },
        };
        PlayFair pf = new PlayFair(thekey);
        String plaintext = cleanInput(in.nextLine());
        String validated = pf.validate(plaintext);
        String encrypted = pf.encrypt(validated);
        String decrypted = pf.decrypt(encrypted);
        System.out.println("Validated text: " + validated);
        System.out.println("Encrypted text: " + encrypted);
        System.out.println("Decrypted text: " + decrypted);
        in.close();
    }
}
