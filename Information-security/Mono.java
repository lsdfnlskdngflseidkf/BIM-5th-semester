import java.util.Scanner;

public class Mono {
    private String alphabets;
    private String key;

    public Mono(String userkey) {
        this.alphabets = "abcdefghijklmnopqrstuvwxyz ";
        this.key = userkey;
    }

    String encrypt(String plain) {
        StringBuilder cipher = new StringBuilder();
        for (int i = 0; i < plain.length(); i++) {
            char currentChar = plain.charAt(i);
            int index = this.alphabets.indexOf(currentChar);
            if (index != -1) {
                cipher.append(this.key.charAt(index));
            } else {
                // if the character is not available in the alphabets then append it as it is
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
            // plain = plain.replaceAll("\\s", "");

            String key = "zxcvbnmlkjhgfdsaq wertyuiop"; // Ensure space is included if it's in alphabets
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
