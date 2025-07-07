from typing import List
from collections import Counter

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, r = 0, 0, 0
        zero_count = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left +=1

            r = max(right - left, r)
            right +=1                
                
        return r
    # -----------------------------------------------------------
    # 這跟1004的算法完全相同，
    # 核心重點：
        # 1. 建立一次固定滾動，例如right
        # 2. 識別窗口內，是否有滿足條件，例如不能超過多少 0
        # 3. 內部loop。如果違反，讓左側修正直到補上，不要兩側都前進



    # -----------------------------------------------------------
    # 使用Counter 的開銷太大
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, r = 0, 0, 0

        while right < len(nums):
            cc = Counter(nums[left:right+1])
            if  cc[0] <= 1:
                r = max(right - left, r)
                right +=1
            else:
                left +=1
                # right +=1    # 這邊只動一者，等待窗戶回歸合法狀態，不是一直開（也就是加上右邊）
        return r



# ----------------------------------------------------------------
# ll = [1,0,0,0,0,1,1,1,1,1]
# aa = Counter(ll)  # Counter({1: 6, 0: 4})
# print(aa[0]) # 4
