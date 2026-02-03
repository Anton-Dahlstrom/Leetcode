public class Solution
{
    public bool IsTrionic(int[] nums)
    {
        int n = nums.Length;
        bool swap = false;
        if (nums[0] > nums[1] | nums[n - 2] > nums[n - 1] | nums[n - 1] == nums[n - 2])
            return false;
        for (int i = 1; i < n - 1; i++)
        {
            if (nums[i] == nums[i - 1])
                return false;
            if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1])
            {
                if (swap)
                    return false;
                swap = true;
            }
        }
        return swap;
    }
}