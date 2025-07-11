from typing import List
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        counter = 0
        col = [tuple([k[i] for k in grid]) for i in range(len(grid)) ]
        ccol = Counter(col)

        for j in grid:
            counter += ccol[tuple(j)]
        
        return counter

aa = Solution()
aa.equalPairs([[3,1,2,2],
               [1,4,4,4],
               [2,4,2,2],
               [2,5,2,2]])

# key points
# 1. 要變成 tuple 才可以轉變成 hashable，並且tuple不像是set()，不會把重複吃掉
# 2. Counter資料查找，如果沒有，會得到0，不會報錯