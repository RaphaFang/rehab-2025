from typing import List
# from collections import Counter

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, zero_count, max_len = 0, 0, 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # 這邊是處理超過數量的 0 在裡面時
            while zero_count > k:
                if nums[left] ==0:
                    zero_count -= 1
                left += 1

            # 這邊可以合法計算 right - left 因為上面的流程處理了 
            max_len = max(max_len, right - left +1)
        return max_len


aa = Solution()
aa.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)

# | 類型     | 適用情境              | 左右移動邏輯                            |
# | ------ | ----------------- | --------------------------------- |
# | 固定長度   | 窗口大小已知，如平均值       | `right += 1`, `left += 1`         |
# | 可變長度   | 最長或最短滿足條件子陣列      | `right += 1` 持續擴大，必要時 `left += 1` |
# | 滿足條件縮小 | 找最短滿足條件的窗口        | 滿足後嘗試 `left += 1`                 |
# | 雙向動態   | 需要比較 pattern / 頻率 | `left`, `right` 控制範圍              |
