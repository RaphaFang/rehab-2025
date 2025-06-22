from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, counter = 0, len(nums)-1, 0

        while i < j:
                if nums[i] + nums[j] < k:
                    i+=1
                elif nums[i] + nums[j] > k:
                    j-=1
                elif nums[i] + nums[j] == k:
                    counter+=1
                    i+=1
                    j-=1
        return counter
    
# 使用 sort() 時間複雜度就至少會是n log n

# ------------------------------------------------------------------------
# 想降低，需要透過hashtable來處理

# 這邊可以線性的解決找不到數值的問題，並且不會重複查找，例如[1,9,9,1]
# 只會跑一次完整的 nums list
from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0

        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                res += 1
                freq[complement] -= 1
            else:
                freq[num] += 1

        return res

aa = Solution()
aa.maxOperations([3,1,3,4,3],6)

# ------------------------------------------------------------------------
from collections import defaultdict
freq = defaultdict(int)
freq["a"] = 1
freq["b"] = 100
freq["c"] = 0
freq["d"] = 'str'

freq["a"]+=1
print(freq)
print(freq['complement']) # 輸出 0，因為沒設定過 key="a"，會觸發 int() = 0
print(freq['b'])
print(freq['c'])
print(freq["d"])
print(freq["e"])  # 輸出 "str"，雖然 default 是 int，但你直接覆蓋了

