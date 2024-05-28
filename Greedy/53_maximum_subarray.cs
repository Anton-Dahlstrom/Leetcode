// The fundamental solution is to restart the count whenever the sum of all 
// the previous values is negative and to always store the largest sum found so far.
public class Solution
{
    public int MaxSubArray(int[] nums)
    {
        int cur = int.MinValue;
        int largest = int.MinValue;
        for (int i = 0; i < nums.Length; i++)
        {
            if (cur < 0)
            {
                cur = nums[i];
            }
            else { cur += nums[i]; }

            if (cur > largest)
            {
                largest = cur;
            }
        }
        return largest;
    }
}