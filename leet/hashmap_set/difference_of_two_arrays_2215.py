from typing import List

class Solution:
    # ------------------------------------------------------------------------
    # 3ms
    # 未來嘗試先畫圖，有圖片後的思緒更清晰
    # 原本還有想說用two pointer
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [[list(set(nums1)-set(nums2))],[list(set(nums1)-set(nums2))]]

    # ------------------------------------------------------------------------
    # 要有排序才可以推動elif區塊，另一機制推動前進
    # list1 = sorted([3, 1, 4, 2])  # ➜ [1, 2, 3, 4]
    # list2 = sorted([4, 6, 5, 3])  # ➜ [3, 4, 5, 6]
    # while i < len(list1) and j < len(list2):
    # if list1[i] == list2[j]:
    #     result.append(list1[i])
    #     i += 1
    #     j += 1
    # elif list1[i] < list2[j]:
    #     i += 1
    # else:
    #     j += 1
    # ------------------------------------------------------------------------
    # 401ms
    # 大概是最慢的作法，O n square
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        for i in nums1:
            if i not in result[0] and i not in nums2:
                result[0].append(i)
        for j in nums2:
            if j not in result[1] and j not in nums1:
                result[1].append(j)
        return result
