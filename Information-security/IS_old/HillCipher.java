public class HillCipher {
    public static void main(String[] args) {
        String PlainText = "HI";
        int[][] key = {
            {3, 3}, 
            {2, 5}
        };
        int[] PlainNum = new int[2];
        PlainNum[0] = PlainText.charAt(0) - 'A';
        PlainNum[1] = PlainText.charAt(1) - 'A';
        char[] C = new char[2];
        C[0] = (char) (((key[0][0] * PlainNum[0] + key[0][1] * PlainNum[1]) % 26) + 'A'); // First letter
        C[1] = (char) (((key[1][0] * PlainNum[0] + key[1][1] * PlainNum[1]) % 26) + 'A'); // Second letter
        System.out.println("Ciphertext: " + new String(C));
    }
}
