public class Solution
{
    public int[] FindFrequentTreeSum(TreeNode root)
    {
        Dictionary<int, int> counter = [];
        int dfs(TreeNode node)
        {
            if (node == null)
            {
                return 0;
            }
            int treeSum = node.val;
            treeSum += dfs(node.left);
            treeSum += dfs(node.right);
            if (counter.TryGetValue(treeSum, out int count))
            {
                counter[treeSum] = count + 1;
            }
            else
            {
                counter[treeSum] = 1;
            }
            return treeSum;
        }
        dfs(root);
        int maxCount = counter.Values.Max();
        var res = counter.Where(x => x.Value == maxCount).Select(x => x.Key).ToArray();
        return res;
    }
}
