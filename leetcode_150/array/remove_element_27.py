class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k


ss = Solution()
ss.removeElement([3,2,2,3], 3)

# -----------------------------------------------------------------
# from collections import deque
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         res = 0
#         n_n = deque(nums)
#         for n in nums:
#             if n != val:
#                 res +=1
#             else:
#                 n_n.popleft()
#                 n_n.append("_")
