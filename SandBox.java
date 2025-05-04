import static java.lang.Math.abs;

public class SandBox {
    // original
    public static int original(final int x) {
        return (x > 0) ? 0 - x : x;
    }

    public static int optimized(final int x) {
        return -abs(x);
    }

    public static void main(String[] args) {
        int x = 1_000_000;

        long start1 = System.nanoTime();
        int result1 = original(x);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        int result2 = optimized(x);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2);
        System.out.println("Opt ver.: " + duration2 / 1_000_000.0 + " ms");
    }
}
