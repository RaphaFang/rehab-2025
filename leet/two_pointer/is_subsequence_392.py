class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp = 0
        for i in range(len(s)):
            if s[i] in t[i:]:
                dot = t.index(s[i]) + i
                print(t[i:], t.index(s[i]) , dot)
                if dot< temp:
                    return False
                else:
                    temp = dot
            else:
                return False
        return True
            # print(dot)

        # index_list = []
        # for _ in range(len(s)):
        #     if s[_] not in t:
        #         return False
        #     else:
        #         print(t[_:])
        #         print(_, type(t[_:].index(s[_])))
                
        #         index_list.append(t[_:].index(s[_]))

        # print(index_list)

        # for n in range(len(index_list)-1):
        #     if index_list[n] > index_list[n+1]:
        #         return False

        # return True


aa = Solution()
print(aa.isSubsequence(s = "aaaaaa", t = "bbaaa"))