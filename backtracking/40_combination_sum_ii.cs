public class Solution
{
    public IList<int> temp = [];
    public IList<IList<int>> result = [];
    public IList<IList<int>> CombinationSum2(int[] nums, int target)
    {
        Array.Sort(nums);
        Dfs([.. nums], 0, 0, target);
        return result;
    }
    public void Dfs(IList<int> nums, int index, int cur, int target)
    {
        if (index >= nums.Count)
        {
            return;
        }
        int rem = int.MinValue;
        for (int i = index; i < nums.Count; i++)
        {
            int val = nums[i];
            if (val == rem)
            {
                continue;
            }
            cur += val;
            temp.Add(val);
            if (cur == target)
            {
                IList<int> res = [.. temp];
                result.Add(res);
            }
            else if (cur < target)
            {
                Dfs(nums, i + 1, cur, target);
            }
            temp.RemoveAt(temp.Count - 1);
            cur -= val;
            rem = val;
        }
    }
}