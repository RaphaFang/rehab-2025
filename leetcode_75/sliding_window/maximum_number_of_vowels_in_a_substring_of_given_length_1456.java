package leetcode_75.sliding_window;

import java.util.Set;

class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowel = Set.of('a', 'e', 'i', 'o', 'u');

        int left = 0, right = k - 1, temp = 0;

        for (int i = left; i <= right; i++) {
            if (vowel.contains(s.charAt(i))) {
                temp++;
            }
        }

        int m_vowel = temp;

        while (right < s.length() - 1) {
            if (vowel.contains(s.charAt(left))) {
                temp--;
            }
            left++;
            right++;
            if (vowel.contains(s.charAt(right))) {
                temp++;
            }
            m_vowel = Math.max(m_vowel, temp);
        }
        return m_vowel;
    }
}
