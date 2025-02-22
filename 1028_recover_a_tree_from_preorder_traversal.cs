public class Solution
{
    public TreeNode RecoverFromPreorder(string traversal)
    {
        int findDepth(int j)
        {
            int cur = j;
            while (traversal[cur] == '-')
            {
                cur++;
            }
            return cur - j;
        }
        (int, int) findValue(int i)
        {
            string val = "";
            while (i < traversal.Length && char.IsDigit(traversal[i]))
            {
                val += traversal[i];
                i++;
            }
            return (i, int.Parse(val));
        }

        (int, int) dfs(TreeNode node, int depth, int i)
        {
            if (i >= traversal.Length)
            {
                return (i, depth);
            }
            int nextdepth = findDepth(i);
            i += nextdepth;
            if (nextdepth <= depth)
            {
                return (i, nextdepth);
            }
            int val;
            (i, val) = findValue(i);
            node.left = new(val);

            if (i >= traversal.Length)
            {
                return (i, nextdepth);
            }

            (i, nextdepth) = dfs(node.left, nextdepth, i);
            if (i >= traversal.Length || nextdepth <= depth)
            {
                return (i, nextdepth);
            }

            if (nextdepth <= depth)
            {
                return (i, nextdepth);
            }
            (i, val) = findValue(i);
            node.right = new(val);

            (i, nextdepth) = dfs(node.right, nextdepth, i);
            return (i, nextdepth);
        }
        int i = 0;
        string val = "";
        while (i < traversal.Length && char.IsDigit(traversal[i]))
        {
            val += traversal[i];
            i++;
        }
        TreeNode root = new(int.Parse(val));
        dfs(root, 0, i);
        return root;
    }
}
