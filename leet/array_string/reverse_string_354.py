class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u"}
        index_list = []
        v_list=[]

        for index, i in enumerate(s):
            if i.lower() in vowels:
                index_list.append(index)
                v_list.append(i)
        v_list.reverse()

        # for index, i in enumerate(s):
        #     if i.lower() in vowels:
        #         index_list.append(index)
        #         v_list.insert(0, i)

        s_list = list(s)
        for j in range(len(index_list)):
            s_list[index_list[j]]=v_list[j]
        return "".join(s_list)
    
    # def reverseVowels(self, s: str) -> str:
    #     vowels = {"a","e","i","o","u"}
    #     s_list = list(s)
    #     v_list=[]

    #     for index, i in enumerate(s):
    #         if i.lower() in vowels:
    #             s_list[index] = "_"
    #             v_list.insert(0, i)
    #     s_list_j = "".join(s_list)

    #     for j in v_list:
    #         s_list_j = s_list_j.replace("_", j, 1)
    #     return(s_list_j)


aa = Solution()
aa.reverseVowels("Ui")
# --------

#! 1. 11ms(沒有replace)
        #         v_list.append(i)
        # v_list.reverse()
    # 這也很快，未來不要用用insert了

#! 2. 127ms(沒有replace)
# 很慢，用insert(0, "a") 就可以塞到最前面

#! 3. 215ms(有replace)/107ms(沒有replace)
# 用repalce，慢的誇張
# 即便調整成reverse()，也需要107ms

# 7kyu_disemvowel.py
# 去看這邊的差異，那邊replace會比較快，是因為全部換，現在慢是因為換一個
#! 這是GPT說的，我不買帳
# 上一個例子中，只要跑10 次，就全部換完
# 現在要跑到list結束，但是是基於list長度，而非換一個吧？

