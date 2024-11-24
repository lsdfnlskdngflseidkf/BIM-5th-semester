public class ExtendedEuclidean {

    public static int[] extendedGCD(int a, int b) {
        if (b == 0) {
            return new int[] { a, 1, 0 };
        }

        int[] result = extendedGCD(b, a % b);
        int gcd = result[0];
        int x1 = result[1];
        int y1 = result[2];

        int x = y1;
        int y = x1 - (a / b) * y1;

        return new int[] { gcd, x, y };
    }

    public static void main(String[] args) {
        int a = 82;
        int b = 34;

        int[] result = extendedGCD(a, b);
        int gcd = result[0];
        int x = result[1];
        int y = result[2];

        System.out.println("GCD: " + gcd);
        System.out.println("x: " + x + ", y: " + y);
        System.out.println(
            "Verification: " +
            a +
            " * " +
            x +
            " + " +
            b +
            " * " +
            y +
            " = " +
            gcd
        );
    }
}
