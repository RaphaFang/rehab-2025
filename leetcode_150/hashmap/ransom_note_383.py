from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc, mc = Counter(ransomNote), Counter(magazine)
        if len(rc) > len(mc):
            return False
        

        for n in rc:
            temp = mc.get(n,0)
            if not rc[n] <= temp:
                return False
        return True
        