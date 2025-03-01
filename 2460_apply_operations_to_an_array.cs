public class Solution
{
    public int[] ApplyOperations(int[] nums)
    {
        int n = nums.Length;
        int i = 0;
        int j = 0;
        int[] res = new int[n];

        while (i < n)
        {
            if (nums[i] > 0)
            {
                if (i < n - 1 && nums[i] == nums[i + 1])
                {
                    res[j] = nums[i] * 2;
                    i++;
                }
                else
                {
                    res[j] = nums[i];
                }
                j++;
            }
            i++;
        }
        return res;
    }
}
internal class Program
{
    static void Main(string[] args)

    {
        int[] arr = arr = [1, 2, 2, 1, 1, 0];
        int[] output = [1, 4, 2, 0, 0, 0];
        Solution obj = new();
        int[] res = obj.ApplyOperations(arr);
        Console.WriteLine(string.Join(" ", res));
        Console.WriteLine(string.Join(" ", output));
        Console.WriteLine(res == output);
    }
}
