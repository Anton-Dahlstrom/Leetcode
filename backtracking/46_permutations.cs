// Convert the array of nums to a list. 
// Each time the Dfs function is called we remove a value from nums and add it to temporary list.
// This ensures the same number won't be added twice to the temporary list.
// After each function call the number is swapped back from the temporary list to nums allowing the
// next Dfs-call to have access to all numbers.


public class Solution
{
    public IList<int> temp = [];
    public IList<IList<int>> result = [];
    public IList<IList<int>> Permute(int[] nums)
    {
        Dfs([.. nums]);
        return result;
    }
    public void Dfs(IList<int> nums)
    {
        if (nums.Count <= 0)
        {
            IList<int> res = [.. temp];
            result.Add(res);
            return;
        }
        for (int i = 0; i < nums.Count; i++)
        {
            int val = nums[i];
            temp.Add(val);
            nums.RemoveAt(i);

            Dfs(nums);

            nums.Insert(i, val);
            temp.RemoveAt(temp.Count - 1);
        }
    }
}