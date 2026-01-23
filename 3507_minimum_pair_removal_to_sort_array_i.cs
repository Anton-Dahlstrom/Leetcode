public class Solution
{
    public int MinimumPairRemoval(int[] nums)
    {
        bool sorted;
        int index = -1;
        int minsum;
        int res = 0;
        while (nums.Length > 0)
        {
            sorted = true;
            minsum = int.MaxValue;
            int[] temp = new int[nums.Length - 1];
            for (int i = 0; i < nums.Length - 1; i++)
            {
                if (nums[i] > nums[i + 1])
                    sorted = false;
                if (nums[i] + nums[i + 1] < minsum)
                {
                    minsum = nums[i] + nums[i + 1];
                    index = i;
                }
            }
            if (sorted)
                return res;
            int inserted = 0;
            for (int i = 0; i < nums.Length; i++)
            {
                if (i == index)
                {
                    temp[i] = minsum;
                    i++;
                    inserted = 1;
                    continue;
                }
                temp[i - inserted] = nums[i];
            }
            nums = temp;
            res++;
        }
        return res;
    }
}