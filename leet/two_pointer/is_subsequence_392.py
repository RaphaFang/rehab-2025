class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = 0
        t_copy = list(t)

        for i in range(len(s)):
            if s[i] in t_copy[temp:]:
                dot = t_copy[temp:].index(s[i]) + temp
                t_copy[dot] = "0"

                if dot< temp:
                    return False
                else:
                    temp = dot
            else:
                return False
        return True
    

aa = Solution()
print(aa.isSubsequence(s = "aaaaa", t = "bbaaaa"))