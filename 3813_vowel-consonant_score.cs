public class Solution
{
    public int VowelConsonantScore(string s)
    {
        var hset = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };
        int n = s.Length;
        int v = 0;
        int c = 0;
        for (int i = 0; i < n; i++)
        {
            if (!char.IsDigit(s[i]))
            {
                if (hset.Contains(s[i]))
                {
                    v++;
                }
                else if (!char.IsWhiteSpace(s[i]))
                {
                    c++;
                }
            }
        }
        if (c == 0)
            return 0;
        return v / c;
    }
}