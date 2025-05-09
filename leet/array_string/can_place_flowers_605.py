from typing import List
import re

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i - 1] == 0) and \
               (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1
        return count >= n

# 我下面的作法會花費太多時間在處理例外，反而沒有正面的處理問題
# 其實直接去思考可以變動的資料能調整成什麼樣子，會是最好的
# ---------------------------------------------
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         aa = ''.join(map(str, flowerbed))
#         len_aa = len(aa)
#         if len_aa==1:
#             if aa =="0":
#                 return True if n<=1 else False
#             else:
#                 return True if n==0 else False
#         what = len(re.findall(r'(?=(000))', aa))
#         if what&1:
#             what = (what+1)//2
#         else:
#             what = what//2
#         if aa[:3] == "001" :
#             what+=1
#         if aa[-3:] == "100":
#             what+=1
#         return True if what>=n else False
            
# tt = Solution()
# print(tt.canPlaceFlowers([1,0,0,0,0],2))


# ---------------------------------------------
# !key points
# map()
# re.findall(r'(?=(000))', aa)



