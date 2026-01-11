class Solution:
    def isPalindrome(self, s: str) -> bool:
        holder = [n.lower() for n in s if n.isalnum()]
        ll = len(holder)
        if ll ==0:
            return True

        for i in range(ll//2):
            if not holder[i] == holder[ll-i-1]:
                return False
        return True

ss = Solution()
print(ss.isPalindrome("0P"))
# aa = [0,1,2]
# print(aa[::-1])

