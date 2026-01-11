class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        p1, p2 = 0, 0
        while p2 < len(s) and p1 < len(t):
            if t[p1] == s[p2]:
                p2+=1
                if p2 == len(s):
                    return True
            p1+=1
        return False