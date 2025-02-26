public class Solution
{
    public int MaxAbsoluteSum(int[] nums)
    {
        int maxres = 0;
        int minres = 0;
        int curmax = 0;
        int curmin = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            curmin += nums[i];
            minres = Math.Min(minres, curmin);
            if (curmin > 0)
            {
                curmin = 0;
            }
            curmax += nums[i];
            maxres = Math.Max(maxres, curmax);
            if (curmax < 0)
            {
                curmax = 0;
            }
        }
        return Math.Max(minres * -1, maxres);
    }
}
internal class Program
{
    static void Main(string[] args)

    {
        int[] nums = [2, -5, 1, -4, 3, -2];
        int output = 8;

        Solution obj = new();
        int res = obj.MaxAbsoluteSum(nums);
        Console.WriteLine(res);
        Console.WriteLine(output);
        Console.WriteLine(res == output);
    }
}
