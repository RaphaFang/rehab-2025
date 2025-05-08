import java.util.ArrayList;
import java.util.List;

class SandBox {
    // original
    public static int original(int n) {
        char[] digits = String.valueOf(n).toCharArray();
        String[] arr = new String[digits.length];
        for (int i = 0; i < digits.length; i++) {
            int num = digits[i] - '0';
            arr[i] = String.valueOf(num * num);
        }
        // String result = ;
        return Integer.parseInt(String.join("", arr));
    }

    // optimized_1

    public static int optimized_1(int n) {
        if (n == 0)
            return 0;
        List<String> list = new ArrayList<>();

        while (n > 0) {
            int num = n % 10;
            list.add(0, String.valueOf(num * num)); // 倒著，加到最前面
            n /= 10; // 這是砍掉一個位數
        }
        return Integer.parseInt(String.join("", list));
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
        int n = 9999;
        // String numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4".repeat(100);

        long start1 = System.nanoTime();
        int result1 = original(n);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        int result2 = optimized_1(n);
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
