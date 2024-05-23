public class Solution
{
    public int Rob(int[] nums)
    {
        if (nums.Length < 2)
        {
            return nums[0];
        }
        if (nums.Length > 2)
        {
            nums[2] += nums[0];
        }
        int i = 3;
        while (i < nums.Length)
        {
            nums[i] += Math.Max(nums[i - 2], nums[i - 3]);
            i++;
        }
        return Math.Max(nums[^1], nums[^2]);
    }
}