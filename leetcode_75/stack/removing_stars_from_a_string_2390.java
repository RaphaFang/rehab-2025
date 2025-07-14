package leetcode_75.stack;

import java.util.ArrayDeque;
import java.util.Deque;

public class removing_stars_from_a_string_2390 {
    public String removeStars(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch != '*') {
                stack.push(ch);
            } else {
                stack.pop();
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.removeLast());
        }

        return sb.toString();
    }
}
