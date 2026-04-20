public class Solution
{
    public int MaxDistance(int[] colors)
    {
        int n = colors.Length;
        int res = n;
        int start = colors[n - 1];
        for (int i = 0; i < n; i++)
        {
            if (colors[i] != start)
            {
                res = n - i - 1;
                break;
            }
        }
        start = colors[0];
        for (int i = n - 1; i >= 0; i--)
        {
            if (colors[i] != start)
            {
                res = Math.Max(res, i);
                break;
            }
        }
        return res;
    }
}