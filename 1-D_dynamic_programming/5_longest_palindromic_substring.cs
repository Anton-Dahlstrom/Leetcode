// Takes each individual char and each pair of matching chars next to each other
// and runs one pointer to the left and one to the right for as long as the pointers 
// chars are the same. Stores and returns result.
public class Solution
{
    public string LongestPalindrome(string s)
    {
        int l;
        int r;
        int longest = 1;
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
                longest += 1;
                while (l >= 0 && r < s.Length && s[l] == s[r])
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
                longest = 1;
            }

            l = i - 1;
            r = i + 1;
            while (l >= 0 && r < s.Length && s[l] == s[r])
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
            longest = 1;
        }
        string sub = s[index[0]..index[1]];
        return sub;
    }
}