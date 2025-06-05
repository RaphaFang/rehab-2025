class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        // if (root == null) return 0;
        // 可以寫成一行的

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.max(left, right) + 1;
    }
}