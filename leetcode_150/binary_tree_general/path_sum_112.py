class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, acc):
            if not node:
                return False

            acc += node.val

            if not node.left and not node.right:
                return acc == targetSum

            return dfs(node.left, acc) or dfs(node.right, acc)

        return dfs(root, 0)