from collections import deque, defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        num_dq = deque()
        ele_dq = deque()
        num_holder, ele_holder = [], []

        backward = False
        ele_dict = defaultdict()

        for ch in formula:
            if ch.isdigit():
                if backward == False:
                    rebuild = num_dq.pop()
                    if rebuild != 1:
                        num_dq.append(rebuild * 10 + int(ch))
                    else:
                        num_dq.append(int(ch))
                
                if backward:
                    if ele_dq[-1] == "(":
                        backward = False
                        break

                    num_holder.append(num_dq.pop() * int(ch))
                    ele_holder.append(ele_dq.pop())


            elif ch == ')':
                backward = True
                
            elif ch == '(':
                ele_dq.append('(')
            
            elif ch.isupper():
                ele_dq.append(ch)
                num_dq.append(1) # 至少會有1

            elif ch.islower():
                rebuild = ele_dq.pop()
                ele_dq.append(rebuild + ch)

            



             