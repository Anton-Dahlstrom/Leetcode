public class Solution
{
    public int FindBottomLeftValue(TreeNode root)
    {
        int maxdepth = -1;
        int res = 0;
        void dfs(TreeNode node, int depth)
        {
            if (node == null)
            {
                return;
            }
            if (depth > maxdepth)
            {
                res = node.val;
                maxdepth = depth;
            }
            dfs(node.left, depth + 1);
            dfs(node.right, depth + 1);

        }
        dfs(root, 0);
        return res;
    }
}

