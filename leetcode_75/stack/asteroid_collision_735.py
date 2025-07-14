from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        dq = deque()
        # dq.append(asteroids[0])

        for _ in asteroids:
            alive = True
            while alive and dq and dq[-1] > 0 and _ < 0:
                if dq[-1] + _ < 0:
                    dq.pop()
                elif dq[-1] + _ == 0:
                    dq.pop()
                    alive = False
                else:  # 也就是目前stack內的大過飛進來的，所以不要把 - 的加進來
                    alive = False
            if alive:
                dq.append(_)
        # print(list(dq))
        return list(dq)

ss = Solution()
ss.asteroidCollision([-2, -2, 2, -2])

# 並且如果數字資開始進去是-，也沒有問題，會直接進入對列
# 如果出現 [-2, -2, 2, -2]
# 前 3 個會直接進入，第四個才會觸發碰撞，得到 [-2, -2]