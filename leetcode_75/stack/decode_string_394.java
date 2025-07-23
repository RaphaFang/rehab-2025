import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String decodeString(String s) {
        Deque<String> strStack = new ArrayDeque<>();
        Deque<Integer> numStack = new ArrayDeque<>();
        StringBuilder curStr = new StringBuilder();
        int num = 0;

        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
            } else if (ch == '[') {
                numStack.push(num);
                strStack.push(curStr.toString());
                curStr.setLength(0); // 規零
                num = 0;
            } else if (ch == ']') {
                int repeat = numStack.pop();
                String prevStr = strStack.pop();
                StringBuilder temp = new StringBuilder(prevStr);
                temp.append(curStr.toString().repeat(repeat)); // .repeat() 取代重複的 *
                curStr = temp;
            } else {
                curStr.append(ch);
            }
        }
        return curStr.toString();
    }
}
