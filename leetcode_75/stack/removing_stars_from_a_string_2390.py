from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        dq = deque()
        for _ in s:
            if _ != "*":
                dq.append(_)
            else:
                dq.pop()
        return ''.join(list(dq))

ss = Solution()
ss.removeStars("erase*****")