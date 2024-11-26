public class CaesarCipher {

    public static String encrypt(String text, int shift) {
        StringBuilder encryptedText = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char currentChar = text.charAt(i);
            if (currentChar >= 'a' && currentChar <= 'z') {
                char encryptedChar = (char) (((currentChar - 'a' + shift) %
                        26) +
                    'a');
                if (encryptedChar < 'a') {
                    encryptedChar += 26;
                }
                encryptedText.append(encryptedChar);
            } else {
                encryptedText.append(currentChar);
            }
        }
        return encryptedText.toString();
    }

    public static String decrypt(String text, int shift) {
        return encrypt(text, -shift);
    }

    public static void main(String[] args) {
        String originalText = "Hello World!".toLowerCase();
        int shift = 3;

        String encryptedText = encrypt(originalText, shift);
        System.out.println("Encrypted: " + encryptedText);

        String decryptedText = decrypt(encryptedText, shift);
        System.out.println("Decrypted: " + decryptedText);
    }
}
