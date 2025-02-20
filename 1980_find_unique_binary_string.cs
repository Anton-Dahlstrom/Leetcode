public class Solution
{
    public string FindDifferentBinaryString(string[] nums)
    {
        int n = nums.Length;
        HashSet<string> set = nums.ToHashSet();
        char[] options = ['0', '1'];
        string dfs(string cur)
        {
            if (cur.Length == n)
            {
                if (!set.Contains(cur))
                {
                    return cur;
                }
                else
                {
                    return "";
                }
            }
            foreach (char option in options)
            {
                string res = dfs(cur + option);
                if (res.Length > 0)
                {
                    return res;
                }
            }
            return "";
        }
        string res = dfs("");
        return res;
    }
}
