public class Solution
{
    public long MaxSumTrionic(int[] nums)
    {
        int n = nums.Length;
        int inc = 0;
        int dec = 0;
        int state = 0;
        long res = long.MinValue;
        long big = int.MinValue;
        long small = int.MinValue;
        for (int i = 1; i < n; i++)
        {
            if (nums[i] > nums[i - 1])
            {
                if (state != 1)
                    small = nums[i] + nums[i - 1];
                else
                {
                    small = Math.Max(small, nums[i - 1]);
                    small += nums[i];
                }
                if (inc == 1 && dec == 1)
                {
                    big += nums[i];
                    res = Math.Max(res, big);
                }
                inc = 1;
                state = 1;
            }
            else if (nums[i] < nums[i - 1])
            {
                if (state == 1)
                    big = small + nums[i];
                else if (inc == 1 && state == 2)
                {
                    big += nums[i];
                }
                if (inc == 0)
                    big = int.MinValue;
                else
                    dec = 1;
                small = int.MinValue;
                state = 2;
            }
            else if (nums[i] == nums[i - 1])
            {
                inc = 0;
                dec = 0;
                state = 0;
                big = int.MinValue;
                small = int.MinValue;
            }
        }
        return res;
    }
}