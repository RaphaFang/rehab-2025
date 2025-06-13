from types import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost) +1
        dp = [0]*top

        for i in range(2, top):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        print(dp)


# 這不會算是greed（會向後看），dp是向前看，
