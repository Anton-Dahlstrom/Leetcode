public class Solution
{
    public int MinimumRecolors(string blocks, int k)
    {
        int l = 0; int r = 0;
        int cur = 0;
        int res = 0;
        while (r < blocks.Length)
        {
            if (blocks[r] == 'B')
            {
                cur++;
            }
            if (r - l == k)
            {
                if (blocks[l] == 'B')
                {
                    cur--;
                }
                l++;
            }
            r++;
            if (cur > res)
            {
                res = cur;
                if (res == k)
                {
                    return 0;
                }
            }
        }
        return k - res;
    }
}
