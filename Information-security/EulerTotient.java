import java.util.Scanner;

public class EulerTotient {

    public static int eulerTotient(int n) {
        int result = n;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                while (n % i == 0) n /= i;
                result -= result / i;
            }
        }
        if (n > 1) result -= result / n;
        return result;
    }

    public static void main(String[] args) {
        System.out.println("Enter the number to find euler's totient of");
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        System.out.println(
            "Euler's Totient Function φ(" +
            number +
            ") = " +
            eulerTotient(number)
        );
    }
}
