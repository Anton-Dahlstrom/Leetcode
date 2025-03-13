public class Solution
{
    public int MinZeroArray(int[] nums, int[][] queries)
    {
        int n = queries.Length;
        int[] events = new int[nums.Length + 1];
        int i = 0;
        int j = 0;
        int cur = 0;
        while (i < nums.Length)
        {
            cur += events[i];
            while (j < queries.Length && cur < nums[i])
            {
                if (queries[j][1] + 1 <= i)
                {
                    j++;
                    continue;
                }
                else if (queries[j][0] > i)
                {
                    events[queries[j][0]] += queries[j][2];
                    events[queries[j][1] + 1] -= queries[j][2];
                }
                else
                {
                    cur += queries[j][2];
                    events[queries[j][1] + 1] -= queries[j][2];
                }
                j++;
            }
            if (nums[i] > cur)
            {
                return -1;
            }
            i++;
        }
        return j;
    }
}
