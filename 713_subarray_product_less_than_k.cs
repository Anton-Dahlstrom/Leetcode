public class Solution
{
    public int NumSubarrayProductLessThanK(int[] nums, int k)
    {
        if (k < 2)
        {
            return 0;
        }

        int res = 0; int cur = 1;
        int l = 0; int r = 0;

        while (r < nums.Length)
        {
            if (cur * nums[r] < k)
            {
                cur *= nums[r];
                r++;
                res += r - l;
            }
            else
            {
                cur = Math.Max(1, cur / nums[l]);
                l++;
                r = Math.Max(l, r);
            }
        }
        return res;
    }
}
internal class Program
{
    static void Main(string[] args)

    {
        int[] nums = [10, 5, 2, 6];
        int k = 100;
        int output = 8;

        Solution obj = new();
        long res = obj.NumSubarrayProductLessThanK(nums, k);
        Console.WriteLine(res);
        Console.WriteLine(output);
    }
}
