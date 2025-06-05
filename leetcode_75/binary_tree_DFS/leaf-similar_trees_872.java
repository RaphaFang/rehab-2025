class SolutionWithStream {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        var leaves1 = getLeaves(root1).toList();
        var leaves2 = getLeaves(root2).toList();
        return leaves1.equals(leaves2);
    } // equals 這是比較內容物，不是比較資料地址

    private Stream<Integer> getLeaves(TreeNode node) {
        if (node == null)
            return Stream.empty();
        if (node.left == null && node.right == null)
            return Stream.of(node.val);
        return Stream.concat(getLeaves(node.left), getLeaves(node.right));
    } // concat 是兩個list的合併
}

class SolutionWithOri {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList<>();
        List<Integer> leaves2 = new ArrayList<>();

        getLeaves(root1, leaves1);
        getLeaves(root2, leaves2);

        return leaves1.equals(leaves2);
    }

    private void getLeaves(TreeNode node, List<Integer> leaves) {
        if (node == null)
            return;

        if (node.left == null && node.right == null) {
            leaves.add(node.val);
            return;
        }

        getLeaves(node.left, leaves);
        getLeaves(node.right, leaves);
    }
}

// class Solution {
// public boolean leafSimilar(TreeNode root1, TreeNode root2) {
// public int[] getLeave(TreeNode node) {
// if (node == null) return int[];
// if (node.left == null & node.right == null) return [node.val];
// return getLeaves(node.left) + getLeaves(node.right);
// }
// return getLeave(root1) == getLeave(root2);
// }
// }