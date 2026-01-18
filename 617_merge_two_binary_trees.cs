public class Solution
{
    public TreeNode MergeTrees(TreeNode root1, TreeNode root2)
    {
        TreeNode dummy = new();
        return Dfs(root1, root2);
    }
    private TreeNode? Dfs(TreeNode? n1, TreeNode? n2)
    {
        if (n1 == null && n2 == null)
            return null;
        TreeNode node = new();
        if (n1 != null)
            node.val += n1.val;
        if (n2 != null)
            node.val += n2.val;
        TreeNode? left = Dfs(n1?.left, n2?.left);
        if (left != null)
            node.left = left;
        TreeNode? right = Dfs(n1?.right, n2?.right);
        if (right != null)
            node.right = right;
        return node;
    }
}