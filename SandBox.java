import static java.util.Arrays.stream;

class SandBox {
    // original
    public static String original(String numbers) {
        String[] strNum = numbers.split(" ");

        int max = Integer.MIN_VALUE; // 這可以給出系統能計算的最小數字
        int min = Integer.MAX_VALUE;
        for (String n : strNum) {
            int nn = Integer.parseInt(n);
            max = (nn > max) ? nn : max;
            min = (nn < min) ? nn : min;
        }
        return max + " " + min;
    }

    // optimized_1

    static String optimized_1(String numbers) {
        var stats = stream(numbers.split(" "))
                .mapToInt(Integer::parseInt)
                .summaryStatistics();
        return stats.getMax() + " " + stats.getMin();
    }

    // optimized_2
    // static String optimized_2(String str) {
    // List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E',
    // 'I', 'O', 'U');
    // StringBuilder result = new StringBuilder();
    // for (char c : vowels) {
    // if (!str.contains(String.valueOf(c))) {
    // result.append(c);
    // }
    // }
    // return result.toString();
    // }

    public static void main(String[] args) {
        // int repeat = 1000;
        String numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4".repeat(100);

        long start1 = System.nanoTime();
        String result1 = original(numbers);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        String result2 = optimized_1(numbers);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2);
        System.out.println("Opt_1 ver.: " + duration2 / 1_000_000.0 + " ms");

        // long start3 = System.nanoTime();
        // String result3 = optimized_2(str);
        // long end3 = System.nanoTime();
        // long duration3 = (end3 - start3);
        // System.out.println("Opt_2 ver.: " + duration3 / 1_000_000.0 + " ms");
    }
}
