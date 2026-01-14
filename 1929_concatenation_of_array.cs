public class Solution
{
    public int[] GetConcatenation(int[] nums)
    {
        var res = nums.Concat(nums).ToArray();
        return res;
    }
}