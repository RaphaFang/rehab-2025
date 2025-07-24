from collections import deque, defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        num_dq, ele_dq, num_holder, ele_holder = deque(), deque(), deque(), deque()
        backward = False

        for ch in formula:
            if ch.isdigit():
                if backward == False:
                    rebuild = num_dq.pop()
                    if rebuild != '1':

                        num_dq.append(rebuild * 10 + int(ch))
                    else:
                        num_dq.append(int(ch))
                
                if backward:
                    while ele_dq and ele_dq[-1] != "(":
                        num_holder.appendleft(int(num_dq.pop()) * int(ch))
                        ele_holder.appendleft(ele_dq.pop())
                    ele_dq.pop()
                    num_dq.extend(num_holder)
                    ele_dq.extend(ele_holder)
                    num_holder.clear()
                    ele_holder.clear()
                    backward = False

            elif ch == ')':
                backward = True
                
            elif ch == '(':
                ele_dq.append('(')
            
            elif ch.isupper():
                ele_dq.append(ch)
                num_dq.append('1') # 至少會有1

            elif ch.islower():
                rebuild = ele_dq.pop()
                ele_dq.append(rebuild + ch)

        print(ele_dq)
        print(num_dq)
        ele_dict = defaultdict(int)
        for i in range(len(ele_dq)):
            ele_dict[ele_dq[i]] += int(num_dq[i])

        result = ''
        for n in sorted(ele_dict.items()):
            if n[1] > 1:
                result += (n[0] + str(n[1]))
            else:
                result += n[0]
        print(result)
        return result


ss = Solution()
# ss.countOfAtoms("K4(ON(SO3)2)2")
# ss.countOfAtoms("Mg(OH)2")
ss.countOfAtoms("(NB3)33")
# ! 這邊會出問題，是因為我設定的backward 沒有讓數字建立好
# ! 應該要是雙位數的，但是只建立了一位數，就相成進去了
# ! 導致數子就算的不對了

# ss.countOfAtoms('H11He49NO35B7N46Li20')
