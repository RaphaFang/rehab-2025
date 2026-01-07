class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ll = len(prices)
        if ll <=1:
            return 0

        holder = 0
        left, right = 0, 1

        while ll > right:
            temp = prices[right] - prices[left]
            if temp >= 0:
                if temp > holder:
                    holder = temp
                right +=1
            else:
                left += 1

        return holder
