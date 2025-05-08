class Kata {
    public static String getMiddle(String word) {
        int ll = word.length();
        if ((ll & 1) != 0) {
            int index = (ll - 1) / 2;
            return String.valueOf(word.charAt(index));
            // Character result = word.charAt(index);
            // return result.toString();
        } else {
            int index = ll / 2 - 1;
            return word.substring(index, index + 2);
        }
    }

    public static String op(String word) {
        int ll = word.length();
        return word.substring((ll - 1) / 2, ll / 2 + 1);
    }
}