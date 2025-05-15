from typing import List
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = math.inf
        sec = math.inf

        for n in nums:
            if n <= first:
                first = n
            elif n <= sec:
                sec = n
            else:
                return True
        return False
        


# --------------------------------------------------------
# 是練習 if, else if, else 的好機會
# 要<= ，不然極端案例中，整個政列都是等大的，就會直接跳躍到第三個條件，回傳true
