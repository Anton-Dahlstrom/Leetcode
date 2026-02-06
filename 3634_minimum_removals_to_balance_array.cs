public class Solution
{
    public int MinRemoval(int[] nums, int k)
    {
        int res = 0;
        Array.Sort(nums);
        int n = nums.Length;
        var cutleft = new int[n];
        int left = 0;
        var cutright = new int[n];
        int right = 0;
        for (int i = 0; i < n; i++)
        {
            while (left < n && (long)(nums[left] * k) < nums[i])
            {
                left++;
            }
            while (right < n && (long)nums[i] * (long)k >= nums[right])
            {
                right++;
            }
            cutleft[i] = left - 1;
            cutright[i] = right;
        }

        left = 0;
        right = n - 1;
        while (left < right && (long)nums[left] * (long)k < nums[right])
        {
            long cleft = cutleft[right] - left;
            long cright = right - cutright[left];
            if (cleft < cright)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return n - (right - left + 1);
    }
}