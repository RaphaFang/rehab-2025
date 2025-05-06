import java.util.Arrays;
import java.util.List;

class Troll {
    public static String disemvowel_2(String str) {
        List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        // StringBuilder result = new StringBuilder();
        for (char c : vowels) {
            str = str.replace(String.valueOf(c), "");
        }
        return str;
    }
    // public static String disemvowel(String str) {
    // List<Character> vowels = Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E',
    // 'I', 'O', 'U');
    // StringBuilder result = new StringBuilder();
    // for (char c : str.toCharArray()) {
    // if (!vowels.contains(c)) {
    // result.append(c);
    // }
    // }
    // return result.toString();
    // }
}
// ---------------------------------------------------------------
// 換成replace，Ori
// 10000
// Ori ver.: 27.730347 ms
// Opt_1 ver.: 39.371619 ms

// 1000
// Ori ver.: 10.497815 ms
// Opt_1 ver.: 6.994207 ms

// 100
// Ori ver.: 2.469973 ms
// Opt_1 ver.: 1.447031 ms

// ! hashtable
// java9之後可以這樣寫： Set<Character> vowels = Set.of('a', 'e', 'i', 'o', 'u', 'A',
// 'E', 'I', 'O','U');
// ---------------------------------------------------------------

// 下面是寫錯的，搞不好之後可以練習改錯
// class Troll {
// public static String disemvowel(String str) {
// List<Character> vowels = Arrays.asList("a", "e", "i", "o", "u", "A", "E",
// "I", "O", "U");
// for (char c : str.toCharArray()){
// str = c in vowels ? str.replace(c,""): None;
// }
// }

// return str;
// }}
// ---------------------------------------------------------------
