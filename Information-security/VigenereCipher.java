import java.util.Scanner;

public class VigenereCipher {

    public static String cleanInput(String input) {
        return input.toLowerCase().replaceAll("[^a-z]", "");
    }

    public static String extendKey(String key, int length) {
        StringBuilder extendedKey = new StringBuilder(key);
        while (extendedKey.length() < length) {
            extendedKey.append(key);
        }
        return extendedKey.toString().substring(0, length);
    }

    public static String encrypt(String plaintext, String key) {
        StringBuilder ciphertext = new StringBuilder();
        key = extendKey(key, plaintext.length());

        for (int i = 0; i < plaintext.length(); i++) {
            char p = plaintext.charAt(i);
            char k = key.charAt(i);
            char c = (char) (((p - 'a' + k - 'a') % 26) + 'a');
            ciphertext.append(c);
        }

        return ciphertext.toString();
    }

    public static String decrypt(String ciphertext, String key) {
        StringBuilder plaintext = new StringBuilder();
        key = extendKey(key, ciphertext.length());

        for (int i = 0; i < ciphertext.length(); i++) {
            char c = ciphertext.charAt(i);
            char k = key.charAt(i);
            char p = (char) (((c - 'a' - (k - 'a') + 26) % 26) + 'a');
            plaintext.append(p);
        }

        return plaintext.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the plaintext:");
        String plaintext = cleanInput(scanner.nextLine());

        System.out.println("Enter the key:");
        String key = cleanInput(scanner.nextLine());

        String encryptedText = encrypt(plaintext, key);
        String decryptedText = decrypt(encryptedText, key);

        System.out.println("Encrypted text: " + encryptedText);
        System.out.println("Decrypted text: " + decryptedText);

        scanner.close();
    }
}
