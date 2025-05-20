from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_amount = 0, len(height)-1, 0

        while left<right:
            bottom = right-left
            tall = min(height[left],height[right])
            max_amount = max(max_amount,bottom*tall)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_amount