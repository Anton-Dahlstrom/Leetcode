public class Solution
{
    public int MinimizeMax(int[] nums, int p)
    {
        int n = nums.Length;
        if (p == 0)
            return 0;
        Array.Sort(nums);
        // binary search ans
        // see how many pairs you can make with a given difference
        int left = 0;
        int right = (int)Math.Pow(10, 9);
        while (left <= right)
        {
            int mid = left + ((right - left) / 2);
            if (CanFit(nums, mid, p))
                right = mid - 1;
            else
                left = mid + 1;
        }
        return right + 1;
    }
    private bool CanFit(int[] nums, int target, int p)
    {
        int count = 0;
        for (int i = 1; i < nums.Length; i++)
        {
            if (nums[i] - nums[i - 1] <= target)
            {
                count++;
                i++;
            }
            if (count >= p)
                return true;
        }
        return false;
    }
}