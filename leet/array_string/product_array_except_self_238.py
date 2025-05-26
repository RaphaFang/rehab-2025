from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            result[i] *= right
            right *= nums[i]

        return result
    # --------------------------------------------------------
    # 整提的重點在於我要如何拆開for loop, turn into O(n), not square
    # 這時要做的，是設計機制不用逐一成上list中的物件
    # 所以，n的左側成績，會是n-1的左側成績再成上n-1，也就是
    # 左邊成完，再換右邊成完，就可以只要讓list掉頭
    # 完成
        
        
        
        
        
    # --------------------------------------------------------
    # ! 這速度是O(n square) for loop 內部還有 for loop
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     popped = []
    #     for n in range(len(nums)):
    #         temp = nums.copy()
    #         temp.pop(n)
    #         str_nums_list = '*'.join(str(i) for i in temp)
    #         popped.append(eval(str_nums_list))
    #     return popped

# --------------------------------------------------------
# 即使你在每次迴圈都寫 temp = nums，它只是：
# 「把 temp 指向和 nums 同一個記憶體位置」
# ! 我如果要建立一個新的，不重複，就需要透過copy()