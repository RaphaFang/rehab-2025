from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # eval()
        popped_num_list = []

        print(len(nums))
        for n in range(len(nums)):
            copy_nums = nums
            copy_nums.pop(n)
            popped_num_list.append(copy_nums)
        print(popped_num_list)



# aa= eval("10*4*3")

# print(aa)
            
the = Solution()
the.productExceptSelf([1,2,3,4])

# [-1,1,0,-3,3]