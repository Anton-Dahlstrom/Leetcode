public class FindElements
{
    public TreeNode Root;
    public FindElements(TreeNode root)
    {
        Root = root;
        void dfsFill(TreeNode? node, int val)
        {
            if (node == null)
            {
                return;
            }
            node.val = val;
            dfsFill(node.left, val * 2 + 1);
            dfsFill(node.right, val * 2 + 2);
        }
        dfsFill(root, 0);
    }

    public bool Find(int target)
    {
        bool dfsFind(TreeNode node)
        {
            if (node == null || node.val > target)
            {
                return false;
            }
            if (node.val == target)
            {
                return true;
            }
            if (dfsFind(node.left) || dfsFind(node.right))
            {
                return true;
            }
            return false;
        }
        return dfsFind(Root);
    }
}
