public class Solution
{
    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars)
    {
        int vmax = 0;
        int hmax = 0;
        int count = 0;
        Array.Sort(hBars);
        Array.Sort(vBars);
        for (int i = 0; i < hBars.Length; i++)
        {
            if (hBars[i] == 1 || hBars[i] == n + 2)
            {
                continue;
            }
            if (i > 0 && hBars[i] == hBars[i - 1] + 1)
            {
                count++;
            }
            else { count = 1; }
            hmax = Math.Max(hmax, count);
        }
        count = 0;

        for (int i = 0; i < vBars.Length; i++)
        {
            if (vBars[i] == 1 || vBars[i] == m + 2)
            {
                continue;
            }
            if (i > 0 && vBars[i] == vBars[i - 1] + 1)
            {
                count++;
            }
            else { count = 1; }
            vmax = Math.Max(vmax, count);
        }
        int len = Math.Min(vmax, hmax) + 1;
        return len * len;
    }
}