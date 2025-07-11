import java.util.*;

// ! 這是一個java表達法，可以直接減掉字母
// 'a' - 'a' ➜ 0
// 'b' - 'a' ➜ 1
// 'z' - 'a' ➜ 25

// 下面的更快，
// ---------------------------------------------------------------
class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] arr1 = new int[26];
        int[] arr2 = new int[26];

        for (int i = 0; i < word1.length(); i++) {
            arr1[word1.charAt(i) - 'a']++;
        }

        for (int i = 0; i < word2.length(); i++) {
            arr2[word2.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if ((arr1[i] == 0 && arr2[i] != 0) || (arr2[i] == 0 && arr1[i] != 0)) {
                // 這邊的第一重辨別，檢查一邊為 0 但另一邊不是，並且兩邊檢查
                // 不能直接雙邊等價的檢查，因為我們還需要置換數字，不是單純判斷等價
                return false;
            }
        }

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);
    }
}

// ---------------------------------------------------------------v
class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length())
            return false;

        // 建立兩個 Counter
        Map<Character, Integer> map1 = countChars(word1);
        Map<Character, Integer> map2 = countChars(word2);

        // 1. 比較 key 的集合是否相同
        if (!map1.keySet().equals(map2.keySet()))
            return false;

        // 2. 比較 value 的頻率（不在乎哪個字母對應哪個數量）
        List<Integer> freq1 = new ArrayList<>(map1.values());
        List<Integer> freq2 = new ArrayList<>(map2.values());
        Collections.sort(freq1);
        Collections.sort(freq2);

        return freq1.equals(freq2);
    }

    // 模擬 Counter 的方法
    private Map<Character, Integer> countChars(String word) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : word.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        return map;
    }
}
