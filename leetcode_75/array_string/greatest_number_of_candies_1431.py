from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        return [True if n+extraCandies >= max_c else False for n in candies]
    
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     tf = []
    #     max_c = max(candies)
    #     for n in candies:
    #         if n+extraCandies >= max_c:
    #             tf.append(True)
    #         else:
    #             tf.append(False)

    #     return tf


ss = Solution()
ss.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)