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
public class Solution {
    public int SumRootToLeaf(TreeNode root) {
        return Dfs(root, 0);
    }
    public int Dfs(TreeNode node, int cur){
        cur <<= 1;
        cur += node.val;
        if(node.left == null && node.right == null){
            return cur;
        }
        int res = 0;
        if(node.left != null)
            res += Dfs(node.left, cur);
        if(node.right != null)
            res += Dfs(node.right, cur);
        return res;
    }
}