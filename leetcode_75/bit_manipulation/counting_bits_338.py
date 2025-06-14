from typing import List
from collections import Counter
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)

        for i in range(1,n+1):
            dp[i] = dp[i & (i-1)] + 1
            # or
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp

# ------------------------------------------------------------
# bin(i) 這作法會是 log(n)
# 我再用上 for loop，總體時間會是 (n log n)
class Solution:
    def countBits(self, n: int) -> List[int]:

        result = [0]
        for i in range(1,n+1):
            result.append(list(Counter(bin(i)[2:]).items())[0][1])
        return result


aa = Solution()
aa.countBits(10)