class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

        # temp = []
        # while root:
        #     # temp
        #     if root.left:
        #         maxDepth(root.left)
        #         temp +=1
        #     if root.right:
        #         maxDepth(root.right)
        #         temp +=1
        #     if not root.left and maxDepth(root.right):
        #         temp = max(temp)
