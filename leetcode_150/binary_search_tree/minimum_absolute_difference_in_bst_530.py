# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        prev = None
        ans = float("inf")

        def dfs(node):
            nonlocal prev, ans
            if not node:
                return

            dfs(node.left)

            if prev is not None:
                ans = min(ans, node.val - prev)
            prev = node.val

            dfs(node.right)

        dfs(root)
        return ans
#         if not root:
#             return 0

#         dif = 10000
#         mm = root.val

#         def minb(node, dif, mm):
#             if node:
#                 dif = min(dif, abs(mm-node.val))
#                 mm = min()

#                 minb(root.left, dif, mm)
#                 minb(root.right, dif, mm)

#                 return min(mm, abs(mm-node.val))

