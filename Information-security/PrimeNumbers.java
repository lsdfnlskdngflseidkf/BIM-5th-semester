import java.lang.Math;
import java.util.Scanner;

public class PrimeNumbers {

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        if (number == 2) {
            return true;
        }
        if (number % 2 == 0) {
            return false;
        }

        for (int i = 3; i <= Math.sqrt(number) + 1; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(
            "Enter the number up to which prime numbers are to be listed:"
        );
        int n = in.nextInt();
        int size = n / 2;
        int[] primenumbers = new int[size];
        int arrayindex = 0;
        for (int i = 0; i <= n; i++) {
            if (isPrime(i)) {
                primenumbers[arrayindex] = i;
                arrayindex++;
            }
        }
        System.out.print("The prime numbers up to " + n + " are:");
        int i = 0;
        while (primenumbers[i] != 0) {
            System.out.print(primenumbers[i] + " ");
            i++;
        }
        in.close();
    }
}
