import static java.util.Arrays.stream;

class Kata {
    // public static String highAndLow(String numbers) {
    // String[] strNum = numbers.split(" ");

    // int max = Integer.MIN_VALUE;
    // int min = Integer.MAX_VALUE;
    // for (String n : strNum) {
    // int nn = Integer.parseInt(n);
    // max = (nn > max) ? nn : max;
    // min = (nn < min) ? nn : min;
    // }
    // return max + " " + min;
    // }
    static String highAndLow(String numbers) {
        var stats = stream(numbers.split(" "))
                .mapToInt(Integer::parseInt)
                .summaryStatistics();
        return stats.getMax() + " " + stats.getMin();
    }
}

// --------------------------------------------------------------------
// Ori ver.: 24.53313 ms
// Opt_1 ver.: 12.499859 ms

// !透過stream才是最快的，即便字串長度不是百倍，也能高速

// 之前在猴子，用IntStream效率反而差，可能之後都要測試傳統，以及現代java