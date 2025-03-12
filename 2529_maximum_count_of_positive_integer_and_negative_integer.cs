public class Solution
{
    public int MaximumCount(int[] nums)
    {
        // Find first num larger than -1 and larger than 0.
        int BinarySearchFirstGreater(int lstart, int r, int target)
        {
            int mid = -1;
            int val;
            if (nums[r] <= target)
            {
                return r + 1;
            }
            int l = lstart;
            while (l <= r)
            {
                mid = l + ((r - l) / 2);
                val = nums[mid];
                if (val > target && (mid == lstart || nums[mid - 1] <= target))
                {
                    return mid;
                }
                else if (val <= target)
                {
                    l = mid + 1;
                }
                else
                {
                    r = mid - 1;
                }
            }
            return -1;
        }
        int n = nums.Length;
        int negend = BinarySearchFirstGreater(0, n - 1, -1);
        int posstart = BinarySearchFirstGreater(negend, n - 1, 0);
        return Math.Max(negend, n - posstart);
    }
}

internal class Program
{
    static void Main(string[] args)
    {
        int[] nums = [-3, -2, -1, 0, 0, 1, 2];
        int output = 3;

        Solution obj = new();
        int res = obj.MaximumCount(nums);
        Console.WriteLine(res);
        Console.WriteLine(output);
    }
}
