public class Solution
{
    public int MinPairSum(int[] nums)
    {
        Array.Sort(nums);
        int left = 0;
        int right = nums.Length - 1;
        int res = int.MinValue;
        while (left < right)
        {
            res = Math.Max(res, nums[left] + nums[right]);
            left++;
            right--;
        }
        return res;
    }
}