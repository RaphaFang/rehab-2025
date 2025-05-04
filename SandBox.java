public class SandBox {
    // original
    public static int original(int[] arr) {
        int rn = 0;
        for (int s : arr) {
            if (s > 0) {
                rn += s;
            }
        }
        return rn;
    }

    // optimized
    public static int optimized(int[] arr) {
        int sum = 0;
        for (int num : arr)
            sum += num > 0 ? num : 0;
        return sum;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        long start1 = System.nanoTime();
        int result1 = original(arr);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        int result2 = optimized(arr);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2);
        System.out.println("Opt ver.: " + duration2 / 1_000_000.0 + " ms");
    }
}
