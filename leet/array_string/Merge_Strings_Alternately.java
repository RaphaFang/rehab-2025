class Merge_Strings_Alternately {
    public String mergeAlternately(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        int maxLen = Math.max(len1, len2);
        StringBuilder sb = new StringBuilder(len1 + len2);

        for (int i = 0; i < maxLen; i++) {
            if (i < len1)
                sb.append(word1.charAt((i)));
            if (i < len2)
                sb.append(word2.charAt((i)));
        }
        return sb.toString();
    }
}
// ! 1ms Beats 82.15%

// public static String mergeAlternately(String w1, String w2) {
// int maxLen = Math.max(w1.length(), w2.length());
// return IntStream.range(0, maxLen)
// .mapToObj(i -> {
// String a = i < w1.length() ? String.valueOf(w1.charAt(i)) : "";
// String b = i < w2.length() ? String.valueOf(w2.charAt(i)) : "";
// return a + b;
// })
// .collect(Collectors.joining());
// }
// ! 4ms Beats 22.42%