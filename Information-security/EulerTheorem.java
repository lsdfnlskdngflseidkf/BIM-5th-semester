import java.util.Scanner;

public class EulerTheorem {

    public static int phi(int n) {
        int result = n;
        for (int p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                while (n % p == 0) {
                    n /= p;
                }
                result -= result / p;
            }
        }
        if (n > 1) {
            result -= result / n;
        }
        return result;
    }

    public static boolean areRelativelyPrime(int a, int n) {
        int powe = phi(n);
        if ((int) (Math.pow(a, powe)) % n == 1) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number a: ");
        int a = sc.nextInt();

        System.out.println("Enter number n: ");
        int n = sc.nextInt();

        if (areRelativelyPrime(a, n)) {
            System.out.println(a + " and " + n + " are relatively prime.");
        } else {
            System.out.println(a + " and " + n + " are NOT relatively prime.");
        }

        sc.close();
    }
}
