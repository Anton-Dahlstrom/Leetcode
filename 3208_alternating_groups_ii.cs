public class Solution
{
    public int NumberOfAlternatingGroups(int[] colors, int k)
    {
        int n = colors.Length;
        int l = 0; int r = 1;
        int steps = 1;
        int res = 0;
        int prev = colors[0];
        int cur;
        int diff = 1;
        while (steps < n + k - 1)
        {
            Console.WriteLine($"{l} {r}");
            cur = colors[r];
            if (cur == prev)
            {
                l = r;
                diff = 0;
            }
            else if (diff == k - 1)
            {
                l++;
                res++;
                diff--;
            }
            prev = cur;
            steps++;
            diff++;
            r++;
            r %= n;
        }
        return res;
    }
}
