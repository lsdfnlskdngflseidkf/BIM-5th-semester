import java.util.Scanner;

public class HillCipher {

    // Function to multiply matrices and return the resulting vector
    public static int[] matrixMultiply(int[][] keyMatrix, int[] vector) {
        int[] result = new int[2];
        for (int i = 0; i < 2; i++) {
            result[i] = (keyMatrix[i][0] * vector[0] + keyMatrix[i][1] * vector[1]) % 26;
        }
        return result;
    }

    // Function to find the modular inverse of a number under modulo 26
    public static int modInverse(int a, int m) {
        a = a % m;
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1) {
                return x;
            }
        }
        return 1; // If no modular inverse exists
    }

    // Function to find the determinant of a 2x2 matrix
    public static int determinant(int[][] matrix) {
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26;
    }

    // Function to find the inverse of a 2x2 matrix under modulo 26
    public static int[][] inverseMatrix(int[][] matrix) {
        int det = determinant(matrix);
        int detInverse = modInverse(det, 26);

        int[][] adjugateMatrix = {
            { matrix[1][1], -matrix[0][1] },
            { -matrix[1][0], matrix[0][0] }
        };

        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                adjugateMatrix[i][j] = (adjugateMatrix[i][j] * detInverse) % 26;
                if (adjugateMatrix[i][j] < 0) {
                    adjugateMatrix[i][j] += 26;
                }
            }
        }

        return adjugateMatrix;
    }

    // Function to encrypt the message
    public static String encrypt(String message, int[][] keyMatrix) {
        message = message.toLowerCase().replaceAll("[^a-z]", ""); // Standardize to lowercase and remove non-alphabetic characters
        int length = message.length();
        if (length % 2 != 0) {
            message += "x"; // Padding with 'x' if the length of the message is odd
        }

        StringBuilder cipherText = new StringBuilder();

        for (int i = 0; i < length; i += 2) {
            int[] messageVector = { message.charAt(i) - 'a', message.charAt(i + 1) - 'a' };
            int[] resultVector = matrixMultiply(keyMatrix, messageVector);
            cipherText.append((char) (resultVector[0] + 'a')).append((char) (resultVector[1] + 'a'));
        }

        return cipherText.toString();
    }

    // Function to decrypt the message
    public static String decrypt(String cipherText, int[][] keyMatrix) {
        int[][] inverseKeyMatrix = inverseMatrix(keyMatrix);

        StringBuilder message = new StringBuilder();

        for (int i = 0; i < cipherText.length(); i += 2) {
            int[] cipherVector = { cipherText.charAt(i) - 'a', cipherText.charAt(i + 1) - 'a' };
            int[] resultVector = matrixMultiply(inverseKeyMatrix, cipherVector);
            message.append((char) (resultVector[0] + 'a')).append((char) (resultVector[1] + 'a'));
        }

        return message.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the 2x2 key matrix (4 integers): ");
        int[][] keyMatrix = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                keyMatrix[i][j] = scanner.nextInt();
            }
        }

        scanner.nextLine(); // Consume newline left-over

        System.out.println("Enter the message to be encrypted: ");
        String message = scanner.nextLine();

        String encryptedMessage = encrypt(message, keyMatrix);
        System.out.println("Encrypted Message: " + encryptedMessage);

        String decryptedMessage = decrypt(encryptedMessage, keyMatrix);
        System.out.println("Decrypted Message: " + decryptedMessage);

        scanner.close();
    }
}
