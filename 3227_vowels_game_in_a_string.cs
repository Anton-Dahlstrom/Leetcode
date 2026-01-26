public class Solution
{
    public bool DoesAliceWin(string s)
    {
        HashSet<char> vowels = new HashSet<char> { 'a', 'e', 'i', 'o', 'u' };
        int n = s.Length;
        for (int i = 0; i < n; i++)
        {
            if (vowels.Contains(s[i]))
                return true;
        }
        return false;
    }
}