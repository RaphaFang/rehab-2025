class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = []

        def cc(root,count):
            if root:
                count.append(1)

                cc(root.left,count)
                cc(root.right,count)
            return
        cc(root,count)
        return len(count)
            

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def cc(node):
            if not node:
                return 0
            return 1 + cc(node.left) + cc(node.right)

        return cc(root)