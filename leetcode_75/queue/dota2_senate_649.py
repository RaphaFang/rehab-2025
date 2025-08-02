from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qD, qR = deque(), deque()

        for i, ch in enumerate(senate):
            (qD if ch == 'D' else qR).append(i)
        # 這邊先建立分別理者的 index 對列，因為沒有被ban的選手，是可以繼續在場上的，直到下一次

        while qD and qR:
            d, r = qD.popleft(), qR.popleft()
            if d < r:
                qD.append(d + n)   # D 先出手，ban 一名 R
            else:
                qR.append(r + n)   # R 先出手，ban 一名 D
                
        return "Dire" if qD else "Radiant"
