class Solution:
    def plusOne(self, digits):
        new_d = 1
        for i in range(len(digits)):
            real_digit = digits[i] * 10**(len(digits)-i-1)
            new_d += real_digit
        return [int(k) for k in str(new_d)]


ss = Solution()
ss.plusOne([9,9,9,9])