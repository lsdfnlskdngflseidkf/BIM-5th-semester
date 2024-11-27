public class Hillcipher {

    public static int charToInt(char c) {
        return c - 'A';
    }

    public static char intToChar(int num) {
        return (char) (num + 'A');
    }

    public static int modInverse(int a, int m) {
        for (int x = 1; x < m; x++) if ((a * x) % m == 1) return x;
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

        int[][] inverse = {
            {
                (keyMatrix[1][1] * detInverse) % 26,
                (-keyMatrix[0][1] * detInverse) % 26,
            },
            {
                (-keyMatrix[1][0] * detInverse) % 26,
                (keyMatrix[0][0] * detInverse) % 26,
            },
        };

        for (int[] row : inverse) for (int j = 0; j < 2; j++) if (
            row[j] < 0
        ) row[j] += 26;

        return inverse;
    }

    public static String processText(String text, int[][] matrix) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < text.length(); i += 2) {
            int[] digraph = {
                charToInt(text.charAt(i)),
                charToInt(text.charAt(i + 1)),
            };
            for (int row = 0; row < 2; row++) {
                int val =
                    (matrix[row][0] * digraph[0] +
                        matrix[row][1] * digraph[1]) %
                    26;
                sb.append(intToChar(val < 0 ? val + 26 : val));
            }
        }
        return sb.toString();
    }

    public static String encrypt(String plaintext, int[][] keyMatrix) {
        return processText(plaintext, keyMatrix);
    }

    public static String decrypt(String ciphertext, int[][] keyMatrix) {
        int[][] inverseMatrix = matrixInverse(keyMatrix);
        return (inverseMatrix == null)
            ? "Decryption not possible"
            : processText(ciphertext, inverseMatrix);
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
