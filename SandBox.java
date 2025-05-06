import java.util.Arrays;
import java.util.List;

class SandBox {
    // original
    static String original(String str) {
        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E',
                'I', 'O', 'U');
        StringBuilder result = new StringBuilder();
        for (char c : str.toCharArray()) {
            if (!vowels.contains(c)) {
                result.append(c);
            }
        }
        return result.toString();
    }

    // optimized_1
    static String optimized_1(String str) {
        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        for (char c : vowels) {
            str = str.replace(String.valueOf(c), "");
        }
        return str;
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
        String str = "No offense but,\nYour writing is among the worst I've ever read".repeat(100);

        long start1 = System.nanoTime();
        String result1 = original(str);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        String result2 = optimized_1(str);
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
