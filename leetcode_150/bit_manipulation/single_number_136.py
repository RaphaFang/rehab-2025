class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for n in nums:
            if not a.get(n,0):
                a[n] = 1
            else:
                a.pop(n)
        for n in a:
            return n
        


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]
        for num in nums[1:]:
            ret = (ret ^ num)
        return ret