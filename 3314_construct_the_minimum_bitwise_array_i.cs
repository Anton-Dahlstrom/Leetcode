public class Solution
{
    public int[] MinBitwiseArray(IList<int> nums)
    {
        int n = nums.Count;
        var res = new int[n];
        for (int i = 0; i < n; i++)
        {
            int num = nums[i];
            res[i] = -1;
            for (int j = 0; j < num; j++)
            {
                if ((j | j + 1) == num)
                {
                    res[i] = j;
                    break;
                }
            }
        }
        return res;
    }
}