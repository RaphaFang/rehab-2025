class Solution {
    public static String repeatStr(final int repeat, final String string) {
        // StringBuilder arr = new StringBuilder();
        String[] arr = new String[repeat];
        for (int i = 0; i < repeat; i++) {
            arr[i] = string;
        }
        return String.join("", arr);
    }
}
// class Solution {
//     public static String repeatStr(final int repeat, final String string) {
//         StringBuilder arr = new StringBuilder();
//         for (int i = 0; i < repeat; i++) {
//             arr.append(string);
//         }
//         return arr.toString();
//     }
// }

// class Solution {
// static String repeatStr(int repeat, String string) {
// return string.repeat(repeat);
// }
// }

// Ori ver.: 0.029546 ms
// Ori ver.: 0.03547 ms
// Opt ver.: 0.007087 ms

// !最快還是 .repeat()