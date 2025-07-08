from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        k1, v1 = set(word1), list(Counter(word1).values())
        k2, v2 = set(word2), list(Counter(word2).values())

        if k1 == k2:
            if (sorted(v1) == sorted(v2)): # ! 這邊用 sorted 還是 Counter 都可以
                return True
        return False


aa = Solution()
aa.closeStrings("abbzzca", "babzzcz")


# -----------------------------------------------------------------
# 取出第一組 key-value
# first_key, first_value = list(aa.items())
# # 如果你只想取出 value
# first_value = list(aa.values())
# # 如果你只想取出 key
# first_key = list(aa.keys())