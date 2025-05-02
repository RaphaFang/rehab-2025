class Solution_1 {
    static String removeExclamationMarks(String s) {
        return s.replace("!", "");
    }
}

class Solution_2 {
    static String removeExclamationMarks(String s) {
        return s.replaceAll("!", "");
    }
}
// replace 依照第一元件是尋找目標，替代成第二元件
// replaceAll 接受 regular expression，第一元件填寫RE，替代成第二元件

