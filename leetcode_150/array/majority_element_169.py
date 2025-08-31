from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = dict(Counter(nums))
        size = len(nums) / 2
        for n in target:
            if target[n] >= size:
                return n


ss = Solution()

ss.majorityElement([2,2,1,1,1,2,2])