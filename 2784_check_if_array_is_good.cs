public class Solution
{
    public bool IsGood(int[] nums)
    {
        Array.Sort(nums);
        int n = nums.Length;
        for (int i = 0; i < n - 1; i++)
        {
            if (nums[i] != i + 1)
                return false;
        }
        return nums[n - 1] == n - 1;
    }
}