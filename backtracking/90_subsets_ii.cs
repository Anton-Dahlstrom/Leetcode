// Create a temporary list that starts as a copy of the array.
// When making arrays of the same length we need to keep searching until we get a number
// that's different from the previously entered value.
// If that's the case how do we ever add [1,2,2] from [1,2,2,2,2,3]?
// We only need to ensure that the number we're adding is different from the number we last 
// removed.


public class Solution
{
    public IList<int> temp = [];
    public IList<IList<int>> result = [];
    public IList<IList<int>> SubsetsWithDup(int[] nums)
    {
        // 1, 2, 2, 3 = [1], [1,2], [1,2,2], [1,2,2,3], [1,3]
        Array.Sort(nums);
        Dfs([.. nums], 0);
        foreach (IList<int> l in result)
        {
            foreach (int num in l)
            {
                Console.Write(num);
            }
            Console.WriteLine("--");
        }
        return result;
    }
    public void Dfs(IList<int> nums, int index)
    {
        if (index >= nums.Count)
        {
            return;
        }
        int rem = int.MinValue;
        for (int i = index + 1; i < nums.Count; i++)
        {
            int val = nums[i];
            if (i > 0 && val == rem)
            {
                continue;
            }
            temp.Add(val);
            IList<int> res = [.. temp];
            result.Add(res);
            Dfs(nums, i);
            temp.RemoveAt(temp.Count - 1);
            rem = val;
        }
    }
}