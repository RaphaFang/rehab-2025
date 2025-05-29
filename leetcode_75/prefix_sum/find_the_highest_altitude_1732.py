from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = [0]
        start = 0
        for h in gain:

            temp.append(start + h)
            start += h

        return max(temp)


aa = Solution()
print(aa.largestAltitude( [-5,1,5,0,-7]))