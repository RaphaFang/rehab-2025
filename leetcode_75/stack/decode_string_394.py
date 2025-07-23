from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        str_dp = deque()
        num_dq = deque()
        cur_str = ''
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch) # 這邊的作法，如果多一位數，就將原先的變成多一位數，加上後面的 ch
                
            elif ch == '[':
                num_dq.append(num)
                str_dp.append(cur_str)
                cur_str = ''
                num = 0
            elif ch == ']':
                repeat = num_dq.pop()
                prev_str = str_dp.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += ch
        return cur_str
    
ss = Solution()
ss.decodeString("1[a2[bc3[de]]]")


# 分別會長這樣？

        # str_dp = deque() >> '', 'a', 'bc'
        # num_dq = deque() >> 1, 2, 3

# 接著cur_str 會是 'de' 接著會接續到 ']' 開始反向的pop


