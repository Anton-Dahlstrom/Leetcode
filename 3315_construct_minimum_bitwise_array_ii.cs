public class Solution
{
    public int[] MinBitwiseArray(IList<int> nums)
    {
        // if nums[i] is even it's impossible
        // find the last sequential bit starting from 0
        // res[i] = nums[i] ^ last seq bit
        int n = nums.Count;
        int[] res = new int[n];
        for (int i = 0; i < n; i++)
        {
            if (nums[i] % 2 == 1)
            {
                int bigbit = 1;
                while (bigbit < nums[i] && ((bigbit & nums[i]) == bigbit))
                {
                    bigbit <<= 1;
                }
                bigbit >>= 1;
                res[i] = nums[i] ^ bigbit;
            }
            else
            {
                res[i] = -1;
            }
        }
        return res;
    }
}