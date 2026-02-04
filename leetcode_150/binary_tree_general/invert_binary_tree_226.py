class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return
            left = node.left
            right = node.right

            node.right = left
            node.left = right

            invert(node.right)
            invert(node.left)

            return node
        
        return invert(root)