import java.util.Scanner;

public class DiffieHellman {

    public static int modExponentiation(int base, int exp, int mod) {
        int result = 1;
        base = base % mod;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            exp = exp >> 1;
            base = (base * base) % mod;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int p = 23;
        int g = 5;

        System.out.println("Public parameters:");
        System.out.println("Prime number p: " + p);
        System.out.println("Primitive root g: " + g);
        System.out.print("Enter private key for Alice (a): ");
        int a = in.nextInt();
        System.out.print("Enter private key for Bob (b): ");
        int b = in.nextInt();
        int A = modExponentiation(g, a, p);
        int B = modExponentiation(g, b, p);

        System.out.println("Public key for Alice (A): " + A);
        System.out.println("Public key for Bob (B): " + B);
        int sharedKeyAlice = modExponentiation(B, a, p);
        int sharedKeyBob = modExponentiation(A, b, p);

        System.out.println(
            "Shared secret key computed by Alice: " + sharedKeyAlice
        );
        System.out.println(
            "Shared secret key computed by Bob: " + sharedKeyBob
        );

        in.close();
    }
}
