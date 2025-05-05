class SandBox {
    // original
    static String original(final int repeat, final String string) {
        String[] arr = new String[repeat];
        for (int i = 0; i < repeat; i++) {
            arr[i] = string;
        }
        return String.join("", arr);
    }

    // optimized_1
    static String optimized_1(final int repeat, final String string) {
        StringBuilder arr = new StringBuilder();
        for (int i = 0; i < repeat; i++) {
            arr.append(string);
        }
        return arr.toString();
    }

    // optimized_2
    static String optimized_2(int repeat, String string) {
        return string.repeat(repeat);
    }

    public static void main(String[] args) {
        int repeat = 1000;
        String string = "hello";

        long start1 = System.nanoTime();
        String result1 = original(repeat, string);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        String result2 = optimized_1(repeat, string);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2);
        System.out.println("Opt_1 ver.: " + duration2 / 1_000_000.0 + " ms");

        long start3 = System.nanoTime();
        String result3 = optimized_2(repeat, string);
        long end3 = System.nanoTime();
        long duration3 = (end3 - start3);
        System.out.println("Opt_2 ver.: " + duration3 / 1_000_000.0 + " ms");
    }
}
