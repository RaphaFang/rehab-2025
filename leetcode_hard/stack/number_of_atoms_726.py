from collections import deque, defaultdict
import re
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        num_dq, ele_dq = deque(), deque()

        # data cleaning part
        print(formula)
        formula = re.sub(r'\)(?!\d)', ')1', formula)
        print(formula)


        for ch in formula:
            if ch.isdigit():
                rebuild = num_dq.pop()
                
                if rebuild == ')':
                    num_dq.append(rebuild)

                if rebuild == '1' or rebuild == '(' or rebuild == ')':
                    num_dq.append(int(ch))
                else:
                    num_dq.append(rebuild*10 + int(ch)) # 如果先拉出的是多數字，先拉出再放回

                if str(num_dq[-1]).isdigit() and ele_dq[-1] == ')':
                    ele_dq.append('nnn')

            elif ch == ')':
                ele_dq.append(')')
                num_dq.append(')')
                
            elif ch == '(':
                ele_dq.append('(')
                num_dq.append('(')
            
            elif ch.isupper():
                ele_dq.append(ch)
                num_dq.append('1')

            elif ch.islower():
                rebuild = ele_dq.pop()
                ele_dq.append(rebuild + ch)
        
        # 這邊還需要有對列，去處理 backward
        temp_dq = deque()
        backward_holder = deque()
        backward = False

        for i in range(len(ele_dq)):
            while temp_dq and backward == True:  # 要確保他跳到下一數字時再來處理backward
                h = temp_dq.pop()
                if h[0] == '(':
                    temp_dq.extend(backward_holder)
                    backward_holder.clear()
                    backward = False
                else:                    
                    backward_holder.appendleft((h[0], int(h[1]) * int(num_dq[i])))

            if ele_dq[i] == ')':
                backward = True
            elif ele_dq[i] == 'nnn':
                pass
            else:
                temp_dq.append((ele_dq[i], num_dq[i]))
        # print(temp_dq)

        r = defaultdict(int) #! 這邊要加入預設數值 (int, str, ...)，不然報錯
        for k, v in temp_dq:
            r[k] += int(v)

        result = ''
        for n in sorted(r.keys()):
            if int(r[n]) == 1:
                result += n
            else:
                result += (n + str(r[n]))
        print(result)
        return result


ss = Solution()
ss.countOfAtoms("Fe(CN)F6")
# ss.countOfAtoms("(((K4(ON(SO34)2)3(Fe(CN)F6)22)4(Mg(OH)2)10)2(H2O)5)13")
# ss.countOfAtoms("Mg(OH)1")
# ss.countOfAtoms("(Mg)(OH)")

# ss.countOfAtoms("(NB3)33")
# ! 這邊會出問題，是因為我設定的backward 沒有讓數字建立好
# ! 應該要是雙位數的，但是只建立了一位數，就相成進去了
# ! 導致數子就算的不對了

# ss.countOfAtoms('H11He49NO35B7N46Li20')
