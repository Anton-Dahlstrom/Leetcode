public class Solution
{
    public int SmallestBalancedIndex(int[] nums)
    {
        int n = nums.Length;
        long right = 1;
        long left = 0;
        for (int i = 0; i < n; i++)
        {
            left += nums[i];
        }

        for (int i = n - 1; i >= 0; i--)
        {
            left -= nums[i];
            if (right > left)
                return -1;
            else if (left == right)
                return i;
            right *= nums[i];
        }
        return -1;
    }
}