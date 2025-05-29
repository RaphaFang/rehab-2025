class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            if str1 + str2 != str2 + str1:
                return ""
            a, b = len(str1), len(str2)
            result = 0
            while b:
                 a, b = b, a%b
                 result = a
            return str1[:result]

    def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]



tt = Solution()
tt.gcdOfStrings("aaa", "ABCABCABC")