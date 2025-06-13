// package leetcode_75.dp_1d;

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int top = cost.length + 1;
        int[] dp = new int[top];

        for (int i = 2; i < top; i++) {
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[top - 1];
    }
}