import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class SandBox {
    // original
    static int original(String str) {
        int counter = 0;
        Set<Character> vowelsArrHash = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for (char c : str.toCharArray()) {
            counter += vowelsArrHash.contains(c) ? 1 : 0;
        }
        return counter;
    }

    // optimized_1
    static int opt_1(String str) {
        int counter = 0;
        List<Character> vowelsRegularArr = Arrays.asList('a', 'e', 'i', 'o', 'u');
        for (char c : str.toCharArray()) {
            counter += vowelsRegularArr.contains(c) ? 1 : 0;
        }
        return counter;
    }

    // optimized_2
    static int opt_2(String str) {
        return str.replaceAll("[^aeiou]", "").length();
    }

    public static void main(String[] args) {
        // int repeat = 1000;
        String str = "hello";

        long start1 = System.nanoTime();
        int result1 = original(str);
        long end1 = System.nanoTime();
        long duration1 = (end1 - start1);
        System.out.println("Ori ver.: " + duration1 / 1_000_000.0 + " ms");

        long start2 = System.nanoTime();
        int result2 = opt_1(str);
        long end2 = System.nanoTime();
        long duration2 = (end2 - start2);
        System.out.println("Opt_1 ver.: " + duration2 / 1_000_000.0 + " ms");

        long start3 = System.nanoTime();
        int result3 = opt_2(str);
        long end3 = System.nanoTime();
        long duration3 = (end3 - start3);
        System.out.println("Opt_2 ver.: " + duration3 / 1_000_000.0 + " ms");
    }
}
