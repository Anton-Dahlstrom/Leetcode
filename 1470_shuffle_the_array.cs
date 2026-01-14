public class Solution
{
    public int[] Shuffle(int[] nums, int n)
    {
        List<int> res = [];
        for (int i = 0; i < n; i++)
        {
            res.Add(nums[i]);
            res.Add(nums[i + n]);
        }
        return res.ToArray();
    }
}