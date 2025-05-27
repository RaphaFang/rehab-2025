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
# 我前面擔心會出現第一個是第二小，後續出現第一小，以及最大
    # 但情況是，他要的條件，同時要滿足index也要是小到大，
    # 所以我不用去排序，我只要一路篩選就好