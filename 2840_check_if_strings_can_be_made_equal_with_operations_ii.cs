public class Solution
{
    public bool CheckStrings(string s1, string s2)
    {
        int n = s1.Length;
        char[] even1 = new char[n / 2 + n % 2];
        char[] even2 = new char[n / 2 + n % 2];
        char[] odd1 = new char[n / 2];
        char[] odd2 = new char[n / 2];

        for (int i = 0; i < n; i++)
        {
            if (i % 2 == 0)
            {
                even1[i / 2] = s1[i];
                even2[i / 2] = s2[i];
            }
            else
            {
                odd1[i / 2] = s1[i];
                odd2[i / 2] = s2[i];
            }
        }
        Array.Sort(even1);
        Array.Sort(even2);
        Array.Sort(odd1);
        Array.Sort(odd2);
        for (int i = 0; i < even1.Length; i++)
        {
            if (even1[i] != even2[i])
                return false;
        }
        for (int i = 0; i < odd1.Length; i++)
        {
            if (odd1[i] != odd2[i])
                return false;
        }
        return true;
    }
}