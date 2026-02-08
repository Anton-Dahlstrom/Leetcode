/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution
{
    public bool test = true;
    public bool IsBalanced(TreeNode root)
    {
        Dfs(root);
        return this.test;
    }
    public int Dfs(TreeNode? node)
    {
        if (node == null)
            return 0;
        var left = Dfs(node.left);
        var right = Dfs(node.right);
        if (Math.Abs(left - right) > 1)
            this.test = false;
        return Math.Max(left, right) + 1;
    }
}