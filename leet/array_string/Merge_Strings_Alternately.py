import itertools as it

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        bb = []
        for w1, w2 in it.zip_longest(list(word1), list(word2), fillvalue=''):
            bb.append(w1+w2)
        return "".join(bb)
       
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in it.zip_longest(word1, word2, fillvalue=''))  



ob = Solution()
ob.mergeAlternately("abcdef", "123")