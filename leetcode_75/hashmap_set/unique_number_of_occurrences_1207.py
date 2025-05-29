from typing import List

class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp_map = {}
        temp_set = set()

        for n in arr:
            temp_map[n]= temp_map.get(n, 0) + 1
            #  查找 key n 對應的值，若不存在則回傳預設值 0（不會報錯）

        for k, v in temp_map.items():
            if v in temp_set:
                return False
            temp_set.add(v)
        return True

    # ------------------------------------------------------------------------
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp_map = {}
        temp_set = set()
        for n in arr:
            # 我其實不用建立條件，可以直接用
            if temp_map.get(n) == None:
                temp_map[n] = arr.count(n)
                # ! 就是count的問題，用他在list，O(n²)
                # 有發現多數情況，設定條件使用可能造成square的方式，多數情況仍會慢
                # 思考模式可能要直接跳過這方式，用O(n)方式思考

        for k, v in temp_map.items():
            if v in temp_set:
                return False
            temp_set.add(v)
        return True




# aaa = Solution()
# aaa.uniqueOccurrences([1,2,2,1,1,3])