class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ns = s.split()
        return len(ns[-1])
    

ss = Solution()
ss.lengthOfLastWord("Today is a nice day")