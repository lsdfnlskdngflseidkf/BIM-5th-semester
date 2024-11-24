public class RailFenceCipher {

    public static String encrypt(String plaintext, int rails) {
        char[] ciphertext = new char[plaintext.length()];
        char[][] rail = new char[rails][plaintext.length()];
        int direction = 1;
        int row = 0, col = 0;

        for (int i = 0; i < plaintext.length(); i++) {
            rail[row][col++] = plaintext.charAt(i);
            if (row == 0) {
                direction = 1;
            } else if (row == rails - 1) {
                direction = -1;
            }

            row += direction;
        }

        int index = 0;
        for (int i = 0; i < rails; i++) {
            for (int j = 0; j < plaintext.length(); j++) {
                if (rail[i][j] != 0) {
                    ciphertext[index++] = rail[i][j];
                }
            }
        }
        return new String(ciphertext);
    }

    public static String decrypt(String ciphertext, int rails) {
        char[] plaintext = new char[ciphertext.length()];
        char[][] rail = new char[rails][ciphertext.length()];

        int direction = 1;
        int row = 0, col = 0;
        for (int i = 0; i < ciphertext.length(); i++) {
            rail[row][col++] = '*';
            if (row == 0) {
                direction = 1;
            } else if (row == rails - 1) {
                direction = -1;
            }

            row += direction;
        }

        int index = 0;
        for (int i = 0; i < rails; i++) {
            for (int j = 0; j < ciphertext.length(); j++) {
                if (rail[i][j] == '*' && index < ciphertext.length()) {
                    rail[i][j] = ciphertext.charAt(index++);
                }
            }
        }
        row = 0;
        col = 0;
        direction = 1;
        index = 0;
        while (index < ciphertext.length()) {
            if (rail[row][col] != '*') {
                plaintext[index++] = rail[row][col];
            }

            col++;

            if (row == 0) {
                direction = 1;
            } else if (row == rails - 1) {
                direction = -1;
            }

            row += direction;
        }

        return new String(plaintext);
    }

    public static void main(String[] args) {
        String plaintext = "IDONTHATETOGAPARTY";
        int rails = 3;

        String encrypted = encrypt(plaintext, rails);
        String decrypted = decrypt(encrypted, rails);

        System.out.println("Plaintext: " + plaintext);
        System.out.println("Encrypted: " + encrypted);
        System.out.println("Decrypted: " + decrypted);
    }
}
