# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ll = []
        rr = []

        def check(node, keep, order):
            if node is None:
                keep.append(None)
                return

            keep.append(node.val)

            if order:
                check(node.right, keep, True)
                check(node.left, keep, True)
            else:
                check(node.left, keep, False)
                check(node.right, keep, False)
        check(root.right, rr, False)
        check(root.left, ll, True)
        return ll == rr
        
                    




