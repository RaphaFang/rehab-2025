class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        jumps = 0
        end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

        return jumps

            



# ============================================================
ss = Solution()
print(ss.jump([2,3,0,0,1,4]))