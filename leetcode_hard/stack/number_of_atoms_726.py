from collections import deque, defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        num_dq, ele_dq = deque(), deque()

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
        
            # if backward:
            #         while ele_dq and ele_dq[-1] != "(":
            #             num_holder.appendleft(int(num_dq.pop()) * int(ch))
            #             ele_holder.appendleft(ele_dq.pop())
            #         ele_dq.pop()
            #         num_dq.extend(num_holder)
            #         ele_dq.extend(ele_holder)
            #         num_holder.clear()
            #         ele_holder.clear()
            #         backward = False

        print(ele_dq)
        print(num_dq)

        temp_dq = deque()
        num_holder = deque()
        ele_dict = defaultdict(int)

        for i in range(len(ele_dq)):
            if ele_dq[i] in ('(', ')'):
                temp_dq.append(ele_dq[i])
            elif ele_dq[i] == 'nnn':
                num_holder.append(num_dq[i])
            ele_dict[ele_dq[i]] += int(num_dq[i])

        # result = ''
        # for n in sorted(ele_dict.items()):
        #     if n[1] > 1:
        #         result += (n[0] + str(n[1]))
        #     else:
        #         result += n[0]
        # print(result)
        # return result


ss = Solution()
# ss.countOfAtoms("K4(ON(SO3)2)27")
# ss.countOfAtoms("Mg(OH)2")
# ss.countOfAtoms("(NB3)33")
# ! 這邊會出問題，是因為我設定的backward 沒有讓數字建立好
# ! 應該要是雙位數的，但是只建立了一位數，就相成進去了
# ! 導致數子就算的不對了

ss.countOfAtoms('H11He49NO35B7N46Li20')
