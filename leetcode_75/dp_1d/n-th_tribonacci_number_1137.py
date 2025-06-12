class Solution:
    def tribonacci(self, n: int) -> int:
        ll = [0]*(n+3)
        ll[0],ll[1],ll[2] = 0, 1, 1
        for n in range(3, n+1):
            ll[n] = ll[n-1] + ll[n-2] + ll[n-3]
        return ll[n]