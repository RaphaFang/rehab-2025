class Solution:
    def hammingWeight(self, n: int) -> int:
        nn = bin(n)[2:]
        holder = 0 
        for i in nn:
            if i != '0':
                holder +=1
        return holder