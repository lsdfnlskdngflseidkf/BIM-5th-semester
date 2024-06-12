import java.util.Scanner;

public class Caesarcipher {
    public String alphabets;

    public Caesarcipher() {
        this.alphabets = "abcdefghijklmnopqrstuvwxyz";
    }

    public String encrypt(String plaintext, int key) {
        StringBuilder cipher = new StringBuilder();
        plaintext = plaintext.toLowerCase();
        for (int i = 0; i < plaintext.length(); i++) {
            char currentChar = plaintext.charAt(i);
            if (this.alphabets.indexOf(currentChar) != -1) {
                int pindex = this.alphabets.indexOf(currentChar);
                int cindex = (pindex + key) % 26;
                cipher.append(this.alphabets.charAt(cindex));
            } else {
                cipher.append(currentChar);
            }
        }
        return cipher.toString();
    }

    public String decrypt(String ciphertext, int key) {
        StringBuilder plain = new StringBuilder();
        ciphertext = ciphertext.toLowerCase();
        for (int i = 0; i < ciphertext.length(); i++) {
            char currentChar = ciphertext.charAt(i);
            if (this.alphabets.indexOf(currentChar) != -1) {
                int cindex = this.alphabets.indexOf(currentChar);
                int pindex = (cindex - key + 26) % 26;
                plain.append(this.alphabets.charAt(pindex));
            } else {
                plain.append(currentChar);
            }
        }
        return plain.toString();
    }

    public static void main(String[] args) {
        Caesar caesar = new Caesarcipher();
        Scanner sc = new Scanner(System.in);
        int key = 0;
        String plain = "";
        int choice = 0;
        while (choice < 5) {
            System.out.println(
                    "Enter what you would like to do\n1.Enter the plaintext \n2.Enter the Key\n3.Encrypt the text and display it\n4.Decrypt the text and display it");
            switch (choice) {
                case 1:
                    System.out.println("Enter the text that you would like to encrypt");
                    plain = sc.nextLine();
                    break;
                case 2:
                    System.out.println("Enter the key");
                    key = sc.nextInt();
                    break;
                case 3:
                    plain = plain.replaceAll("\\s+", "");
                    String encrypted = caesar.encrypt(plain, key);
                    System.out.println("Encrypted: " + encrypted);
                    break;
                case 4:
                    String decrypted = caesar.decrypt(encrypted, key);
                    System.out.println("Decrypted: " + decrypted);
                    break;

                default:
                    break;
            }
        }
        // plain = plain.replaceAll("\\s+", "");
        // String encrypted = caesar.encrypt(plain, key);
        // System.out.println("Encrypted: " + encrypted);

        // String decrypted = caesar.decrypt(encrypted, key);
        // System.out.println("Decrypted: " + decrypted);
    }
}
