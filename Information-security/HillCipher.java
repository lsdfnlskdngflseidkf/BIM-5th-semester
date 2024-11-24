public class HillCipher {

    public static int charToInt(char c) {
        return c - 'A';
    }

    public static char intToChar(int num) {
        return (char) (num + 'A');
    }

    public static int modInverse(int a, int m) {
        a = a % m;
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1) {
                return x;
            }
        }
        return -1;
    }

    public static int[][] matrixInverse(int[][] keyMatrix) {
        int det =
            (keyMatrix[0][0] * keyMatrix[1][1] -
                keyMatrix[0][1] * keyMatrix[1][0]) %
            26;
        if (det < 0) det += 26;
        int detInverse = modInverse(det, 26);
        if (detInverse == -1) return null;

        int[][] inverse = new int[2][2];
        inverse[0][0] = (keyMatrix[1][1] * detInverse) % 26;
        inverse[0][1] = (-keyMatrix[0][1] * detInverse) % 26;
        inverse[1][0] = (-keyMatrix[1][0] * detInverse) % 26;
        inverse[1][1] = (keyMatrix[0][0] * detInverse) % 26;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                if (inverse[i][j] < 0) inverse[i][j] += 26;
            }
        }
        return inverse;
    }

    public static String encrypt(String plaintext, int[][] keyMatrix) {
        int[] digraph = new int[2];
        int[] result = new int[2];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < plaintext.length(); i += 2) {
            digraph[0] = charToInt(plaintext.charAt(i));
            digraph[1] = charToInt(plaintext.charAt(i + 1));

            for (int row = 0; row < 2; row++) {
                result[row] =
                    (keyMatrix[row][0] * digraph[0] +
                        keyMatrix[row][1] * digraph[1]) %
                    26;
            }

            sb.append(intToChar(result[0]));
            sb.append(intToChar(result[1]));
        }

        return sb.toString();
    }

    public static String decrypt(String ciphertext, int[][] keyMatrix) {
        int[][] inverseMatrix = matrixInverse(keyMatrix);
        if (inverseMatrix == null) {
            return "Decryption not possible";
        }

        int[] digraph = new int[2];
        int[] result = new int[2];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < ciphertext.length(); i += 2) {
            digraph[0] = charToInt(ciphertext.charAt(i));
            digraph[1] = charToInt(ciphertext.charAt(i + 1));

            for (int row = 0; row < 2; row++) {
                result[row] =
                    (inverseMatrix[row][0] * digraph[0] +
                        inverseMatrix[row][1] * digraph[1]) %
                    26;
                if (result[row] < 0) result[row] += 26;
            }

            sb.append(intToChar(result[0]));
            sb.append(intToChar(result[1]));
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        int[][] keyMatrix = { { 6, 5 }, { 1, 12 } };
        String plaintext = "ILOVETOGAPARTY";
        String encryptedText = encrypt(plaintext, keyMatrix);
        String decryptedText = decrypt(encryptedText, keyMatrix);
        System.out.println("Encrypted text: " + encryptedText);
        System.out.println("Decrypted text: " + decryptedText);
    }
}
