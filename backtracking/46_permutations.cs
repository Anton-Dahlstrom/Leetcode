// Create a temporary list that starts as a copy of the array.
// Each time you search deeper you first remove a value from the copy,
// call the search function, and return the value you removed.
// Do this for each item in the temporary array.

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
            IList<int> res = [.. nums];
            result.Add(res);
            return;
        }
        for (int i = 0; i < nums.Count; i++)
        {
            int val = nums[i];
            temp.Add(val);
            // Console.WriteLine(nums[i]);
            nums.RemoveAt(i);
            // Dfs(nums);
            nums.Insert(i, val);
            temp.RemoveAt(temp.Count - 1);
            // Console.WriteLine(nums[i]);
        }

    }
}