import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

public class Mono {
    private final String alphabets;
    private final String key;

    public Mono(String userkey) {
        this.alphabets = "abcdefghijklmnopqrstuvwxyz ";
        this.key = userkey;
    }

    public static String getValidKey() {
        Scanner scanner = new Scanner(System.in);
        try {
            String key;

            while (true) {
                System.out.println("Enter a key for the monoalphabetic cipher (26 unique letters):");
                key = scanner.nextLine().toUpperCase();

                if (isValidKey(key)) {
                    break;
                }
                System.out.println("Invalid key. Please try again.");
            }
            return key;
        } finally {
            scanner.close();
        }
    }

    private static boolean isValidKey(String key) {
        if (key.length() != 26) {
            return false;
        }

        Set<Character> uniqueChars = new HashSet<>();
        for (char c : key.toCharArray()) {
            if (!Character.isLetter(c) || !uniqueChars.add(c)) {
                return false;
            }
        }

        return true;
    }

    String encrypt(String plain) {
        StringBuilder cipher = new StringBuilder();
        for (int i = 0; i < plain.length(); i++) {
            char currentChar = plain.charAt(i);
            int index = this.alphabets.indexOf(currentChar);
            if (index != -1) {
                cipher.append(this.key.charAt(index));
            } else {
                cipher.append(currentChar);
            }
        }
        return cipher.toString();
    }

    String decrypt(String cipher) {
        StringBuilder plain = new StringBuilder();
        for (int i = 0; i < cipher.length(); i++) {
            char currentChar = cipher.charAt(i);
            int index = this.key.indexOf(currentChar);
            if (index != -1) {
                plain.append(this.alphabets.charAt(index));
            } else {
                plain.append(currentChar); // Append as is, if not found in the key or alphabets
            }
        }
        return plain.toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try {
            System.out.println("Enter the Plain text:");
            String plain = in.nextLine().toLowerCase();
            plain = plain.replaceAll("\\s", "");
            String key = getValidKey();
            Mono mon = new Mono(key);

            String cipher = mon.encrypt(plain);
            System.out.println("Encrypted text: " + cipher);

            String decryptedText = mon.decrypt(cipher);
            System.out.println("Decrypted text: " + decryptedText);
        } finally {
            in.close(); // Ensure the Scanner is closed to prevent resource leaks
        }
    }
}
