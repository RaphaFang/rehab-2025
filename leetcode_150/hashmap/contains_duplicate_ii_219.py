from collections import Counter
class Solution:
    def ontainsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        aa = {}
        for i, n in enumerate(nums):
            if n in aa:
                if k >= abs(aa[n] - i):
                    return True
            aa[n] = i
        return False

    # ==== 上面大概快了 4 倍 ====
    def DEPRECATED_containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        aa = {}
        cn, fix_cn = Counter(nums), Counter(nums)
        for i, n in enumerate(nums):
            if fix_cn[n] == 1:
                continue

            if n not in aa:
                aa[n] = i
                cn[n] -= 1
            else:
                if k >= abs(aa[n] - i):
                    return True
                else:
                    if cn[n] >=1:
                       aa[n] = i 
        return False

