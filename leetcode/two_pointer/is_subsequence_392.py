class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
    
    # ---------------------------------------------------------------
    # 這會是On square，因為 py 的in也要走過每元件
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