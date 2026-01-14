public class Solution
{
    public int FindMaxConsecutiveOnes(int[] nums)
    {
        int cur = 0;
        int res = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == 1)
            {
                cur++;
                res = Math.Max(res, cur);
            }
            else
            {
                cur = 0;
            }
        }
        return res;
    }
}