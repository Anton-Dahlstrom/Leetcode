public class Solution
{
    public int[] PivotArray(int[] nums, int pivot)
    {
        List<int> left = [];
        List<int> right = [];
        List<int> mid = [];
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] < pivot)
            {
                left.Add(nums[i]);
            }
            else if (nums[i] == pivot)
            {
                mid.Add(nums[i]);
            }
            else
            {
                right.Add(nums[i]);
            }
        }
        left.AddRange(mid);
        left.AddRange(right);
        return left.ToArray();
    }
}


internal class Program
{
    static void Main(string[] args)

    {
        int[] nums = [9, 12, 5, 10, 14, 3, 10];
        int pivot = 10;
        int[] output = [9, 5, 3, 10, 10, 12, 14];

        Solution obj = new();
        int[] res = obj.PivotArray(nums, pivot);
        Console.WriteLine("[" + string.Join(",", output.Select(row => "[" + string.Join(",", row) + "]")) + "]");
        Console.WriteLine("[" + string.Join(",", res.Select(row => "[" + string.Join(",", row) + "]")) + "]");
    }
}
