from typing import List

class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         left = sum(nums[:i])
    #         right = sum(nums[i+1:])
            
    #         if left == right:
    #             return i
    #     return -1
    # --------------------------------------------------------------
    # ! cleaver 只要一次sum()就解決
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            left += nums[i-1] if i != 0 else 0
            right -= nums[i]
            if left == right:
                return i
        return -1

aa = Solution()
print(aa.pivotIndex([0,1,2,3,4,5]))