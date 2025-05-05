import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Vowels {
    public static int getCount(String str) {
        int counter = 0;
        Set<Character> vowelsArrHash = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        for (char c : str.toCharArray()) {
            counter += vowelsArrHash.contains(c) ? 1 : 0;
        }
        return counter;
    }

    public static int opt_1(String str) {
        int counter = 0;
        List<Character> vowelsRegularArr = Arrays.asList('a', 'e', 'i', 'o', 'u');
        for (char c : str.toCharArray()) {
            counter += vowelsRegularArr.contains(c) ? 1 : 0;
        }
        return counter;
    }

    public static int opt_2(String str) {
        return str.replaceAll("[^aeiou]", "").length();
    }
}

// ---------------------------------------------------------------
// ! Set 是一種 集合資料結構，不允許重複元素
// ! 先前測試，將定義hashtable 放到函數內，初始化的時間比查找多
// Ori ver.: 0.25904 ms
// Opt_1 ver.: 0.173982 ms
// Opt_2 ver.: 4.918275 ms

// ! 將ARR拉出後，用 hashtable 最快
// Ori ver.: 0.014031 ms
// Opt_1 ver.: 0.209513 ms
// Opt_2 ver.: 6.417474 ms