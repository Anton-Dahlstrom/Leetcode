public class Solution
{
    public int CountSubstrings(string s)
    {
        int count = 0;
        int l;
        int r;
        int i = 0;
        while (i < s.Length)
        {
            l = i - 1;
            r = i + 1;
            while (l >= 0 && r < s.Length && s[l] == s[r])
            {
                count++;
                l--;
                r++;
            }
            l = i - 1;
            r = i;
            while (l >= 0 && r < s.Length && s[l] == s[r])
            {
                count++;
                l--;
                r++;
            }
            count++;
            i++;
        }
        return count;
    }
}