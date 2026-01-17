class Solution:
    def isPalindrome(self, x: int) -> bool:
        lx = list(str(x))

        for i in range(len(lx)//2):
            if not lx[i] == lx[-(i+1)]:
                return False
        return True

