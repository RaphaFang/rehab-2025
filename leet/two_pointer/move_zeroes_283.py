class Solution(object):
    def moveZeroes(self, nums):
        zero_list = []
        c_list = []
        
        for i in range(len(nums)):
            zero_list.append(0) if nums[i]==0 else c_list.append(nums[i])                
             
        nums.clear()
        c_list.extend(zero_list)
        nums.extend(c_list)


aa = Solution()
aa.moveZeroes([0,1,0,3,12])


# c_list.pop(i) 
# 不能直接在複製的list推掉東西，會修改到這複製品的長度
# ! 這邊也可以用two pointer作