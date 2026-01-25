public class Solution
{
    public int MinimumDifference(int[] nums, int k)
    {
        Array.Sort(nums);
        int res = int.MaxValue;
        for (int i = 0; i < nums.Length - k + 1; i++)
        {
            res = Math.Min(res, nums[i + k - 1] - nums[i]);
        }
        return res;
    }
}