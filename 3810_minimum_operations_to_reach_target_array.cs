public class Solution
{
    public int MinOperations(int[] nums, int[] target)
    {
        HashSet<int> hset = new();
        int n = nums.Length;
        for (int i = 0; i < n; i++)
        {
            if (nums[i] != target[i])
            {
                hset.Add(nums[i]);
            }
        }
        return hset.Count;
    }
}