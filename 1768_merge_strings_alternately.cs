public class Solution
{
    public string MergeAlternately(string word1, string word2)
    {
        int n = word1.Length;
        int m = word2.Length;
        var builder = new System.Text.StringBuilder(n + m);
        for (int i = 0; i < Math.Max(n, m); i++)
        {
            if (i < n)
                builder.Append(word1[i]);
            if (i < m)
                builder.Append(word2[i]);
        }
        return builder.ToString();
    }
}