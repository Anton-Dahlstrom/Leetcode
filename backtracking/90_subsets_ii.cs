// Create a temporary list that starts as a copy of the array.
// When making arrays of the same length(same depth in the dfs) we need to 
// keep searching until we get a different number from the previously entered number.

public class Solution
{
    public IList<int> temp = [];
    public IList<IList<int>> result = [[]];
    public IList<IList<int>> SubsetsWithDup(int[] nums)
    {
        Array.Sort(nums);
        Dfs([.. nums], 0);
        return result;
    }
    public void Dfs(IList<int> nums, int index)
    {
        if (index >= nums.Count)
        {
            return;
        }
        int rem = int.MinValue;
        for (int i = index; i < nums.Count; i++)
        {
            int val = nums[i];
            if (i > 0 && val == rem)
            {
                continue;
            }
            temp.Add(val);
            IList<int> res = [.. temp];
            result.Add(res);
            Dfs(nums, i + 1);
            temp.RemoveAt(temp.Count - 1);
            rem = val;
        }
    }
}