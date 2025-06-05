# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node):
            if not node:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return getLeaves(node.left) + getLeaves(node.right)

        return getLeaves(root1) == getLeaves(root2)
        # r1_temp = []
        # if root1.left is None and root1.right is None:
        #     r1_temp.append(root1.val)
        # if root1.left:
        #     self.leafSimilar(root1.left)
        # if root1.right:
        #     self.leafSimilar(root1.right)
