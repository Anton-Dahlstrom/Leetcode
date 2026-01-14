public class Solution
{
    public int[] SmallerNumbersThanCurrent(int[] nums)
    {
        int[] sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        int[] res = new int[nums.Length];
        Dictionary<int, int> dict = new();
        for (int i = 1; i < sorted.Length; i++)
        {
            if (sorted[i] > sorted[i0])
            {
                dict[sorted[i]] = i;
            }
        }
        for (int i = 0; i < nums.Length; i++)
        {
            res[i] = dict.GetValueOrDefault(nums[i], 0);
        }
        return res;
    }
}