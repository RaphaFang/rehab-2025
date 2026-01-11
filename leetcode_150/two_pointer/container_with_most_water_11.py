class Solution:
    def maxArea(self, height: List[int]) -> int:
        ll = len(height)
        left, right = 0, ll-1
        temp = 0
        while left < right:
            d = right - left
            hl, hr = height[left], height[right]
            tall = min(hl, hr)
            temp = max(temp, d * tall)

            if hl < hr:
                left += 1
            else:
                right-=1
        return temp


