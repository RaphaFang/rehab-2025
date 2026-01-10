class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ll = len(prices)
        if ll < 2:
            return 0
        
        left, right = 0, 1
        holder = 0

        while right < ll:
            temp = prices[right] - prices[left]
            if temp > 0:
                holder += temp
            left += 1
            right += 1
        return holder

            


            
