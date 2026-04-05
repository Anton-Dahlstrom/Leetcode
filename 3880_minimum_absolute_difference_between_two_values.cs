public class Solution
{
    public int MinAbsoluteDifference(int[] nums)
    {
        int n = nums.Length;
        List<int> ones = new();
        List<int> twos = new();

        for (int i = 0; i < n; i++)
        {
            if (nums[i] == 1)
                ones.Add(i);
            else if (nums[i] == 2)
            {
                twos.Add(i);
            }
        }
        int res = int.MaxValue;
        for (int i = 0; i < ones.Count; i++)
        {
            for (int j = 0; j < twos.Count; j++)
            {
                res = Math.Min(res, Math.Abs(ones[i] - twos[j]));
            }
        }
        if (res == int.MaxValue)
            return -1;
        return Math.Abs(res);
    }
}