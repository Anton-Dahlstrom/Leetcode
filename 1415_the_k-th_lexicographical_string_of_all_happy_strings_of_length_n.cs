public class Solution
{
    public int Count = 0;
    public string GetHappyString(int n, int k)
    {
        List<char> chars = ['a', 'b', 'c'];
        string dfs(string cur)
        {
            if (cur.Length == n)
            {
                Count++;
                Console.WriteLine(cur);
                if (Count == k)
                {
                    return cur;
                }
                return "";
            }
            foreach (char chr in chars)
            {
                if (cur.Length > 0 && cur[^1] == chr)
                {
                    continue;
                }
                string res = dfs(cur + chr);
                if (res.Length > 0)
                {
                    return res;
                }
            }
            return "";
        }
        return dfs("");
    }
}
