# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 應該檢測目前數值，判斷大於還是小於？
    # 不用回頭走，也不用走全部
    # 樹的優勢在於，左小右大，你只要比較要查找對象，比較
    def searchBST(self, root, val): # 我自己覺得這寫法是最好的，因為一次表達三種可能的方式，就是這個數值，或是嘴邊有東西，或是右邊有東西
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return None
    # ---------------------------------------------
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)  # 這邊要記得加上self
        else:
            return self.searchBST(root.right, val)

    # ---------------------------------------------
    # 這是白癡窮舉法，我完全沒有用到樹的優勢
    def searchBST(self, root, val):
        qq = [root]
        for n in qq:
            if n.val == val:
                return n
            if n.left:
                qq.append(n.left)
            if n.right:
                qq.append(n.right)
        return None
