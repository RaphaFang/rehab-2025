from typing import List
class Solution:
    # ----------------------------------------------------------------
    # 63ms
    # 要使用滑動窗
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[0:k])
        max_n = temp

        for n in range(k,len(nums)):
            temp = temp - nums[n-k] + nums[n]
            max_n = max(max_n,temp)
        return max_n/k
    
    # ----------------------------------------------------------------
    # 要避免在loop 中使用sum，他也會掃描選定的區段
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     ll = len(nums)

    #     max_n = float('-inf')
    #     for n in range(ll-k+1):
    #         temp = sum(nums[n:n+k])
    #         if temp>=max_n:
    #             max_n = temp
    #     return max_n/k


aa = Solution()
aa.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)