from types import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a = a^n
        return a
# XOR ------------------------------------------------

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        aa = list(Counter(nums).items())
        for n in aa:
            if n[1] == 1:
                return n[0]
