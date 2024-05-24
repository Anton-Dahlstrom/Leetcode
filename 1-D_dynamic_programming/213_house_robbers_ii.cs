public class Solution
{
    public int Rob(int[] nums)
    {
        if (nums.Length < 2)
        {
            return nums[0];
        }
        int val1 = 0;
        int val2 = 0;
        int temp;
        int i = 0;
        while (i < nums.Length - 1)
        {
            temp = Math.Max(nums[i] + val1, val2);
            val1 = val2;
            val2 = temp;
            i++;
        }
        int res = val2;
        val1 = 0;
        val2 = 0;
        i = 1;
        while (i < nums.Length)
        {
            temp = Math.Max(nums[i] + val1, val2);
            val1 = val2;
            val2 = temp;
            i++;
        }
        return Math.Max(res, val2);
    }
}