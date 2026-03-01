public class Solution
{
    public int MinPartitions(string n)
    {
        int res = 0;
        foreach (var cha in n)
        {
            res = Math.Max(res, cha - '0');
        }
        return res;
    }
}