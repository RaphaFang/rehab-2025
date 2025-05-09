class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (!(str1 + str2).equals(str2 + str1))
            return "";
        int a = str1.length(), b = str2.length();
        int result = 0;
        int temp = 0;
        while (b > 0) {
            temp = b;
            b = a % b;
            a = temp;
            result = a;
        }
        return str1.substring(0, result);

    }
}

// if (str1 + str2 != str2 + str1) return "";
// 這會比較到Java 中使用 == 或 != 比較字串，會比的是記憶體位址（reference equality），不是字串內容。
