class Solution:
    def rob(self, nums: List[int]) -> int:
        ll = len(nums)

        if  ll == 0:
            return 0
        if  ll == 1:
            return nums[0]

        dp = [0] * ll
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, ll):
            
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[ll-1]