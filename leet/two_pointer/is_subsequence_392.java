class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;

        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++; // 這邊不是用else銜接，因為無論如何t都要到下一個 index，兩者相同也要往下一個
        }
        return i == s.length();
    }
}