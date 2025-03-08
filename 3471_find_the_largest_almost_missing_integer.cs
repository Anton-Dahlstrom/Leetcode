public class Solution
{
    public int LargestInteger(int[] nums, int k)
    {
        if (k == 1)
        {
            Dictionary<int, int> dict = [];
            foreach (int num in nums)
            {
                if (dict.ContainsKey(num))
                {
                    dict[num]++;
                    continue;
                }
                dict.Add(num, 0);
            }
            int best = -1;
            for (int i = 0; i < nums.Length; i++)
            {
                if (dict[nums[i]] == 0)
                {
                    best = Math.Max(best, nums[i]);
                }
            }
            return best;
        }
        if (k == nums.Length)
        {
            return nums.Max();
        }

        if (nums[0] == nums[^1] && k < nums.Length)
        {
            return -1;
        }

        HashSet<int> hset = [-1];
        hset.Add(nums[0]);
        hset.Add(nums[^1]);
        for (int i = 1; i < nums.Length - 1; i++)
        {
            hset.Remove(nums[i]);
        }
        return hset.Max();
    }
}
internal class Program
{
    static void Main(string[] args)
    {

        int[] nums = [0, 0];
        int k = 1;
        int output = -1;

        Solution obj = new();
        int res = obj.LargestInteger(nums, k);
        Console.WriteLine(res);
        Console.WriteLine(output);
    }
}
