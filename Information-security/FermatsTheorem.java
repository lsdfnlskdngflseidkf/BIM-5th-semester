import java.util.Scanner;

public class FermatsTheorem {

    public static long modExponentiation(long a, long b, long mod) {
        long result = 1;
        a = a % mod;
        while (b > 0) {
            if (b % 2 == 1) {
                result = (result * a) % mod;
            }
            a = (a * a) % mod;
            b = b / 2;
        }
        return result;
    }

    public static boolean isPrime(long p) {
        if (p <= 1) return false;
        for (long a = 2; a < Math.min(p, 20); a++) {
            if (modExponentiation(a, p - 1, p) != 1) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number 'p': ");
        long p = sc.nextLong();

        if (isPrime(p)) {
            System.out.println(p + " is probably prime.");
        } else {
            System.out.println(p + " is not prime.");
        }

        sc.close();
    }
}
