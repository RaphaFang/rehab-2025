import java.util.stream.IntStream;

public class SandBox {
    public static int[] monkeyCountOriginal(final int n) {
        int[] result = new int[n];
        for (int i = 1, j = 0; i <= n; i++, j++) {
            result[j] = i;
        }
        return result;
    }

    public static int[] monkeyCountOptimized(final int n) {
        return IntStream.rangeClosed(1, n).toArray();
    }

    public static void main(String[] args) {
        int n = 1_000_000;

        long start1 = System.nanoTime();
        int[] result1 = monkeyCountOriginal(n);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1) / 100_000;
        System.out.println("Ori ver.: " + duration1 + " ms");

        long start2 = System.nanoTime();
        int[] result2 = monkeyCountOptimized(n);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2) / 100_000;
        System.out.println("IntStream ver.: " + duration2 + " ms");
    }
}
