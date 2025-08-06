class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 1
        c = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[k] = nums[i]
                c = 1
                k += 1

            elif nums[i] == nums[i-1]:
                if c < 2:
                    nums[k] = nums[i]
                    c += 1
                    k += 1
        print(k, nums)
            
ss = Solution()
ss.removeDuplicates([1,1,1,2,2,3])