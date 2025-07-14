package leetcode_75.stack;

import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();

        for (int asteroid : asteroids) {
            boolean alive = true;
            while (alive && !stack.isEmpty() && stack.peekLast() > 0 && asteroid < 0) {
                if (stack.peekLast() + asteroid < 0) {
                    stack.pollLast(); // 當前右邊小行星比左邊還弱，被吃掉
                } else if (stack.peekLast() + asteroid == 0) {
                    stack.pollLast(); // 兩者抵銷
                    alive = false;
                } else {
                    alive = false;
                }
            }
            if (alive) {
                stack.addLast(asteroid);
            }
        }

        int[] result = new int[stack.size()];
        int i = 0;
        for (int val : stack) {
            result[i++] = val;
        }
        return result;
    }
}
