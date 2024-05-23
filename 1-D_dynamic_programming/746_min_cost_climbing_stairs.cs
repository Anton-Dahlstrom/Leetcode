public class Solution
{
    public int MinCostClimbingStairs(int[] cost)
    {
        int i = 2;
        while (i < cost.Length)
        {
            cost[i] += Math.Min(cost[i - 1], cost[i - 2]);
            i++;
        }
        return Math.Min(cost[^1], cost[^2]);
    }
}