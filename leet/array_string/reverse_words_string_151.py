class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([n for n in s.split(" ") if n!=''][::-1])

        



aa = Solution()
aa.reverseWords("a good   example")


# .reverse() 又比 [::-1] 慢一點

# ! 0ms
# 第一次這麼快