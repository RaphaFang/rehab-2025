class Solution:
    def reverseBits(self, n: int) -> int:
        aa = bin(n)[2:][::-1]
        left = 32 - len(aa)

        zero = ""
        if left:
            for i in range(left):
                zero += "0"
            re = aa + zero
            
        
        return int(re,2)
        