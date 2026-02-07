public class Solution
{
    public int MinimumDeletions(string s)
    {
        int n = s.Length;
        int res = 0;
        int a = 0;
        int b = 0;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == 'a')
                a++;
            else
                b++;
            if (a > b)
            {
                res += b;
                b = 0;
                a = 0;
            }
        }
        res += a;
        return res;
    }
}