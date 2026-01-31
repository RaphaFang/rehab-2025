class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}
        for i in range(nums):
            if target - nums[i] in holder:
                return [i, nums[target - nums[i]]]
            else:
                holder[nums[i]] = i
        


aa = (1,2)
print(sum(aa))