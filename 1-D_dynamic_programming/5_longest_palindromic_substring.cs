// Doesn't find "ccc" because it never looks forward and back if the chars are all the same.

public class Solution
{
    public string LongestPalindrome(string s)
    {
        int l;
        int r;
        int longest = 0;
        int res = 0;
        int[] index = [0, 1];
        for (int i = 0; i < s.Length; i++)
        {
            l = i - 1;
            r = i + 1;
            if (l < 0)
            {
                continue;
            }
            if (s[l] == s[i])
            {
                l--;
                longest++;
            }
            while (l >= 0 && r < s.Length - 1 && s[l] == s[r])
            {
                longest += 2;
                l--;
                r++;
            }
            if (longest > res)
            {
                res = longest;
                index = [l + 1, r];
            }
            longest = 0;
        }
        string sub = s[index[0]..index[1]];
        Console.WriteLine(sub);
        Console.WriteLine(res);
        return sub;
    }
}